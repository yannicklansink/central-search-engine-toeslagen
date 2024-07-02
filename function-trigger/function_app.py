import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.blob_trigger(arg_name="myblob", 
                  path="bestandentrigger/{name}",
                  connection="bestandenstorage_STORAGE") 
def blob_trigger_vector(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob\n"
                f"Name: {myblob.name}\n"
                f"Blob Size: {myblob.length} bytes")
