import openai
import pymongo
import os
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from os.path import join, dirname
from dotenv import load_dotenv
import requests
from openai import OpenAI


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("MONGO_DB_ACC")
OPENAI_KEY = os.environ.get("OPENAI_KEY")

# OpenAI.api_key = OPENAI_KEY
client = OpenAI(api_key=OPENAI_KEY)
openai.api_key = OPENAI_KEY

client = pymongo.MongoClient(SECRET_KEY)
db = client.sample_mflix
collection = db.embedded_movies

# CODE TO GENERATE THE EMBEDDINGS FROM A COLLECTION IN MONGODB ATLAS DATABASE
def generate_embedding(text: str) -> list[float]:
  response = openai.embeddings.create(
        model="text-embedding-ada-002", 
        input=text
    )
  return response.data[0].embedding

# for doc in collection.find({'plot':{"$exists": True}}).limit(50):
#   doc['plot_embedding_hf'] = generate_embedding(doc['plot']) # Adding a new field with the embedding to the document DB
#   collection.replace_one({'_id': doc['_id']}, doc) 

# TRY OUT AND USE THE CREATED EMBEDDINGS FROM ABOVE
query = "imaginary characters from outer space at war"

results = collection.aggregate([
  {"$vectorSearch": {
    "queryVector": generate_embedding(query),
    "path": "plot_embedding",
    "numCandidates": 100,
    "limit": 4,
    "index": "PlotSemanticSearch",
      }}
]);

for document in results:
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')