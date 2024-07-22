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

retriever = vectorstore.as_retriever()

model = ChatOpenAI(temperature=0, model="gpt-4-1106-preview", streaming=True)

# system_prompt = (
#     "You are an assistant for question-answering tasks. "
#     "Use the following pieces of retrieved context to answer "
#     "the question. If you don't know the answer, say that you "
#     "don't know. Use three sentences maximum and keep the "
#     "answer concise."
#     "\n\n"
#     "{context}"
# )

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_prompt),
#         ("human", "{input}"),
#     ]
# )

# # RAG prompt
template = """Beantwoord de vraag uitsluitend op basis van de volgende context.
                Geef daarnaast ook aan het einde de bestandsnamen van de bronnen die je hebt ontvangen terug in bullet points,
                met daarbij het paginanummer als dit beschikbaar is achter de bestandsnaam.

{context}
Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# Chain is de runnable that will be executed
chain = (
    # RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    {
        "context": retriever,
        "question": RunnablePassthrough(),
    }
    | prompt
    | model
    | StrOutputParser()
)



    
# asyncio.run(main())