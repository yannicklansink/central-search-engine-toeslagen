import requests
import json

# Test the RAG-service by sending a POST request to the server

# Define the URL of the server
url = "http://127.0.0.1:8000/RAG/stream"

# Define the payload
payload = {
    "input": "wie is yannick?"
}

# Convert the payload to a JSON string
json_payload = json.dumps(payload)

# Set the headers for the request
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, headers=headers, data=json_payload, stream=True)

# Check if the request was successful
if response.status_code == 200:
    print("Streaming response from server:")
    for chunk in response.iter_content(chunk_size=None):
        if chunk:
            print(chunk.decode('utf-8'), end="", flush=True)
else:
    print(f"Error: {response.status_code}")
    print(response.text)