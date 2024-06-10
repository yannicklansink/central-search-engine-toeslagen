# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# Kopieer het .env bestand naar de werkdirectory in de container
# COPY .env /code/.env 
# 
# CMD ["fastapi", "run", "app/serve.py", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
CMD ["uvicorn", "app.serve:app", "--host", "0.0.0.0", "--port", "80"]