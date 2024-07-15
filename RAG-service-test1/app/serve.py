#!/usr/bin/env python
from typing import List

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os

# Laad de variabelen uit het .env bestand
load_dotenv()

# Gebruik de variabelen
tracing = os.getenv('LANGCHAIN_TRACING_V2')
endpoint = os.getenv('LANGCHAIN_ENDPOINT')
api_key_langchain = os.getenv('LANGCHAIN_API_KEY')
api_key_openai = os.getenv('OPENAI_API_KEY')



# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model
model = ChatOpenAI()

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser


# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Adding a simple root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the LangChain Server!!!!!!!"}

# 5. Adding chain route
add_routes(
    app,
    chain,
    path="/chain",
)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) # Host veranderen naar "0.0.0.0" en niet localhost