from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from app.chain import chain as RAG_chain
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

# When a request is send to /RAG endpoint, FastAPI routes this request to appropriate handler (RAG_chain)
add_routes(app, RAG_chain, path="/RAG")

if __name__ == "__main__":
    import uvicorn
    # Uvicorn is an ASGI server for running FastAPI applications. 

    # host="0.0.0.0": This specifies that the server should be accessible on all available 
    #                 IP addresses of the machine. It's commonly used for allowing external access.
    uvicorn.run(app, host="0.0.0.0", port=8000)
