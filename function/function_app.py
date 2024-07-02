import azure.functions as func
import logging
from azure.storage.blob import BlobServiceClient

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", 
                  path="bestandentrigger/{name}",
                  connection="bestandenstorage_STORAGE") 
def toeslagendataprocessor(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob "
                 f"Name: {myblob.name} "
                 f"Blob Size: {myblob.length} bytes")

    
