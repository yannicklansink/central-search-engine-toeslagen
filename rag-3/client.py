from langserve import RemoteRunnable

# This client interacts with the serve.py api

remote_chain = RemoteRunnable("http://localhost:8000/chain/")
remote_chain.invoke({"language": "italian", "text": "hi"})