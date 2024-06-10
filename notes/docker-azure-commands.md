https://fastapi.tiangolo.com/deployment/docker/

# Dockerfile
    # Use the official Python 3.9 image as the base image
    FROM python:3.9

    # Set the working directory in the container to /code
    WORKDIR /code

    # Copy the requirements.txt file from the local machine to the container at /code/requirements.txt
    COPY ./requirements.txt /code/requirements.txt

    # Install the Python dependencies specified in the requirements.txt file
    RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

    # Copy the contents of the local app directory to the container at /code/app
    COPY ./app /code/app

    # Command to run the FastAPI application, but there is a mistake in the command.
    CMD ["fastapi", "run", "app/main.py", "--port", "80"]


## Build docker image, make sure that you are in the directory the Dockerfile is located:
docker build -t myimage .

## Run a container based on the image
docker run -d --name mycontainer -p 80:80 myimage

## Login op docker hub
docker login

## Tag Docker image
docker tag langchain-server yannicklansink/langchain-server:latest

## Push image to Docker hub
docker push yannicklansink/langchain-server:latest


# Azure

## Login to Azure CLI
azure login

## Create resource group
az group create --name langchainServer --location westeurope

## Create container instance
az container create --resource-group langchainServer --name server-container --image yannicklansink/langchain-server:latest --dns-name-label 
mylangchainserver --ports 80

az container create --resource-group langchainServer --name server-container2 --image yannicklansink/langchain-server:latest  --dns-name-label mylangchainserver --restart-policy OnFailure --ports 80 --environment-variables ADD ENVIRONMENT_VARIABLES

