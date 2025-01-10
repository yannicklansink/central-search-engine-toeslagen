import os
import asyncio
from dotenv import load_dotenv
# from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import CohereEmbeddings
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Pinecone
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from pinecone import Pinecone as PineconeClient
import requests
import langchain_core
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain


load_dotenv()

# Keys
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
PINECONE_INDEX_NAME = os.environ["PINECONE_INDEX_NAME"]

# pinecone = PineconeClient(api_key=PINECONE_API_KEY)

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
# embeddings = CohereEmbeddings(model="multilingual-22-12")
vectorstore = Pinecone.from_existing_index(index_name=PINECONE_INDEX_NAME,
                                           embedding=embeddings)

retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold", 
    search_kwargs={
        "score_threshold": 0.85, 
        "k": 3,
        }
)

# modes to use: gpt-4o-mini, 
model = ChatOpenAI(temperature=0, model="gpt-4o-mini", streaming=True)

# RAG prompt
template = """Beantwoord de vraag uitsluitend op basis van de volgende context.
                Geef daarnaast ook aan het einde de bestandsnamen van de bronnen die je hebt ontvangen terug in bullet points, doe dit alleen als het relevante bestanden zijn,
                met daarbij het paginanummer als dit beschikbaar is achter de bestandsnaam. Doe dat zoals dit:
                - example.txt (p. 2)

{context}
Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# Chain is de runnable that will be executed
chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough(),
    }
    | prompt
    | model
    | StrOutputParser()
)



    
# asyncio.run(main())