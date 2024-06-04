from dotenv import load_dotenv
import os

# Laad de variabelen uit het .env bestand
load_dotenv()

# Gebruik de variabelen
tracing = os.getenv('LANGCHAIN_TRACING_V2')
endpoint = os.getenv('LANGCHAIN_ENDPOINT')
api_key = os.getenv('LANGCHAIN_API_KEY')

print(f'Tracing: {tracing}')
print(f'Endpoint: {endpoint}')
print(f'API Key: {api_key}')

import openai
from langsmith.wrappers import wrap_openai
from langsmith import traceable

# Auto-trace LLM calls in-context
client = wrap_openai(openai.Client())

@traceable # Auto-trace this function
def pipeline(user_input: str):
    result = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}],
        model="gpt-3.5-turbo"
    )
    return result.choices[0].message.content

pipeline("Hello, world!")
print("test")
# Out:  Hello there! How can I assist you today?