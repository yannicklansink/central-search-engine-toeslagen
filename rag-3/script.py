from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
import getpass
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Laad de variabelen uit het .env bestand
load_dotenv()

# Gebruik de variabelen
tracing = os.getenv('LANGCHAIN_TRACING_V2')
endpoint = os.getenv('LANGCHAIN_ENDPOINT')
api_key_langchain = os.getenv('LANGCHAIN_API_KEY')
api_key_openai = os.getenv('OPENAI_API_KEY')

# print(f'Tracing: {tracing}')
# print(f'Endpoint: {endpoint}')
# print(f'Langchain API Key: {api_key_langchain}')
# print(f'OpenAI API Key: {api_key_openai}')

model = ChatOpenAI(model="gpt-4")
parser = StrOutputParser()

# messages = [
#     SystemMessage(content="Translate the following from English into Italian"),
#     HumanMessage(content="hi!"),
# ]


# Chain -> RunnableSequence
# chain = model | parser 
# chain.invoke(messages)

#ChatPromptTemplate
system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
# result = prompt_template.invoke({"language": "italian", "text": "hi"})

chain = prompt_template | model | parser
result = chain.invoke({
        "language": "italian",
        "text": "hi"
    })


print(result)