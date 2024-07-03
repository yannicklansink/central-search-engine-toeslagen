import os
from dotenv import load_dotenv
import uuid
import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient
from pinecone import Index, Pinecone
from langchain_core.documents import Document
# from langchain.embeddings import OpenAIEmbeddings
# from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from unstructured_client import UnstructuredClient
from unstructured_client.models import shared
from unstructured_client.models.errors import SDKError
from unstructured.staging.base import dict_to_elements
from unstructured.chunking.title import chunk_by_title

# Load environment variables from .env file
load_dotenv()

# Initialize clients
unstructured_api_key = os.getenv('UNSTRUCTURED_API_KEY')
pinecone_api_key = os.getenv('PINECONE_API_KEY')
connection_string = os.getenv('bestandenstorage_STORAGE')

unstructured_client = UnstructuredClient(api_key_auth=unstructured_api_key)
pinecone_client = Pinecone(api_key=pinecone_api_key)
index_name = 'langchain-unstructured-data'
index = pinecone_client.Index(index_name)

# Initialize OpenAI embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", 
                  path="bestandentrigger/{name}",
                  connection="bestandenstorage_STORAGE") 
def toeslagendataprocessor(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob "
                 f"Name: {myblob.name} "
                 f"Blob Size: {myblob.length} bytes")

    # Extract blob name from the path
    blob_name = myblob.name.split('/')[-1]  # Get the actual blob name
    container_name = "bestandentrigger"

    # Read blob content
    blob_content = myblob.read()
    if not blob_content:
        logging.error(f"Blob content is empty for blob: {blob_name}")
        return

    # Update document in Pinecone vector database
    try:
        update_document(blob_content, blob_name, index_name, embeddings)
    except Exception as e:
        logging.error(f"Failed to update document: {e}")
        return

    # Delete the blob
    try:
        delete_blob(connection_string, container_name, blob_name)
    except Exception as e:
        logging.error(f"Failed to delete blob: {e}")


def generate_id(prefix):
    return f"{prefix}#{uuid.uuid4()}"

def is_valid_file_type(blob_name):
    valid_extensions = {'.pdf', '.txt', '.html'}
    file_extension = os.path.splitext(blob_name)[1].lower()
    return file_extension in valid_extensions

def update_document(blob_content, blob_name, index_name, embeddings):

    if not is_valid_file_type(blob_name):
        logging.error(f"Unsupported file type for {blob_name}. Supported file types are: .pdf, .txt, .html")
        return
    
    prefix = blob_name  # Use the blob name as prefix
    logging.info(f'filename: {blob_name} en prefix: {prefix}')

    # Delete existing embeddings based on the prefix
    ids_to_delete = []
    for ids in index.list(prefix=f"{prefix}#", namespace=''):
        ids_to_delete.extend(ids)
    if ids_to_delete:
        index.delete(ids=ids_to_delete, namespace='')
        logging.info(f"Existing embeddings for {blob_name} removed: {ids_to_delete}")
    else:
        logging.info(f"No existing embeddings found for filename: {blob_name}")

    # Process the new blob content and add the new embeddings
    files = shared.Files(content=blob_content, file_name=blob_name)

    req = shared.PartitionParameters(
        files=files,
        strategy="hi_res",
    )
    try:
        resp = unstructured_client.general.partition(req)
        elements = dict_to_elements(resp.elements)
    except SDKError as e:
        logging.error(f"Failed to partition document: {e}")
        return

    chunked_elements = chunk_by_title(elements, 
                                      max_characters=512, combine_text_under_n_chars=250)

    documents = []
    ids = []
    for element in chunked_elements:
        metadata = element.metadata.to_dict()
        del metadata["languages"]
        doc_id = generate_id(metadata["filename"])
        ids.append(doc_id)
        documents.append(Document(page_content=element.text, metadata=metadata))

    # Add the new documents to the Pinecone vector store
    try:
        vectorstore = PineconeVectorStore.from_existing_index(
            index_name=index_name,
            embedding=embeddings
        )

        vectorstore.add_texts(
            texts=[doc.page_content for doc in documents],
            metadatas=[doc.metadata for doc in documents],
            ids=ids
        )
        logging.info(f"New embeddings for {blob_name} added.")
    except Exception as e:
        logging.error(f"Failed to add new embeddings: {e}")


def delete_blob(connection_string, container_name, blob_name):
    """Delete a blob from the given container using the provided connection string."""
    
    if not connection_string:
        logging.error("Azure Blob Storage connection string is missing.")
        return

    logging.info(f"Using connection string: {connection_string}")

    # Create a BlobServiceClient using the connection string
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        logging.info("BlobServiceClient created successfully.")
    except Exception as e:
        logging.error(f"Failed to create BlobServiceClient. Error: {e}")
        return

    # Get the blob client
    try:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        logging.info(f"Blob client created for container: {container_name}, blob: {blob_name}")
    except Exception as e:
        logging.error(f"Failed to get blob client. Error: {e}")
        return

    # Attempt to delete the blob
    try:
        blob_client.delete_blob()
        logging.info(f"Blob {blob_name} deleted successfully.")
    except Exception as e:
        logging.error(f"Failed to delete blob {blob_name}. Error: {e}")
