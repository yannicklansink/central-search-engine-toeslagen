import pymongo
import os
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from os.path import join, dirname
from dotenv import load_dotenv
import requests

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("MONGO_DB_ACC")
hf_token = os.environ.get("HF_TOKEN")
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

client = pymongo.MongoClient(SECRET_KEY)
db = client.sample_mflix
collection = db.movies

# CODE TO GENERATE THE EMBEDDINGS FROM A COLLECTION IN MONGODB ATLAS DATABASE
def generate_embedding(text: str) -> list[float]:
  response = requests.post(
    embedding_url,
    headers={"Authorization": f"Bearer {hf_token}"},
    json={"inputs": text})

  if response.status_code != 200:
    raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

  return response.json()

# for doc in collection.find({'plot':{"$exists": True}}).limit(50):
#   doc['plot_embedding_hf'] = generate_embedding(doc['plot']) # Adding a new field with the embedding to the document DB
#   collection.replace_one({'_id': doc['_id']}, doc) 

# TRY OUT AND USE THE CREATED EMBEDDINGS FROM ABOVE
query = "imaginary characters from outer space at war"

results = collection.aggregate([
  {"$vectorSearch": {
    "queryVector": generate_embedding(query),
    "path": "plot_embedding_hf",
    "numCandidates": 100,
    "limit": 4,
    "index": "PlotSemanticSearch",
      }}
]);

for document in results:
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')