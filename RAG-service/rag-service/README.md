## Pinecone-Serverless

### Links

[Langchain templates for fast production](https://github.com/langchain-ai/langchain/blob/master/templates/README.md)

[Langsmith login](https://smith.langchain.com/o/902964b8-7f5f-5be6-9f1f-9bcbfce6c119/projects?paginationState=%7B%22pageIndex%22%3A0%2C%22pageSize%22%3A10%7D)

![chain](https://github.com/langchain-ai/pinecone-serverless/assets/122662504/454266ba-727c-4ce0-ae56-7d004c0fb5d4)

### Index

Follow [instructions from Pinecone](https://www.pinecone.io/blog/serverless/) on setting up your serverless index.

### API keys

Ensure these are set:

- PINECONE_API_KEY
- PINECONE_ENVIRONMENT
- PINECONE_INDEX_NAME
- OPENAI_API_KEY

Note: the choice of embedding model may require additional API keys, such as:

- COHERE_API_KEY

### Notebook

For prototyping:

```
poetry run jupyter notebook
```

### Deployment

This repo was created by following these steps:

**(1) Create a LangChain app.**

Run:

```
langchain app new .
```

This creates two folders:

```
app: This is where LangServe code will live
packages: This is where your chains or agents will live
```

It also creates:

```
Dockerfile: App configurations
pyproject.toml: Project configurations
```

Add your app dependencies to `pyproject.toml` and `poetry.lock` to support Pinecone serverless:

```
poetry add pinecone-client==3.0.0.dev8
poetry add langchain-community==0.0.12
poetry add cohere
poetry add openai
poetry add jupyter
```

Update enviorment based on the updated lock file:

```
poetry install
```

**(2) Add your runnable (RAG app)**

Create a file, `chain.py` with a runnable named `chain` that you want to execute.

This is our RAG logic (e.g., that we prototyped in our notebook).

Add `chain.py` to `app` directory.

Import the LCEL object in `server.py`:

```
from app.chain import chain as pinecone_wiki_chain
add_routes(app, pinecone_wiki_chain, path="/pinecone-wikipedia")
```

Run locally

```
poetry run langchain serve
```

**(3) Deploy it with hosted LangServe**

Go to your LangSmith console.

Select `New Deployment`.

Specify this Github url.

Add the abovementioned API keys as secrets.

### Poetry commando's

Hier zijn enkele veelvoorkomende Poetry-commando's met een korte beschrijving van wat ze doen:

```
poetry install
```

Installeert alle afhankelijkheden die zijn gedefinieerd in de pyproject.toml en poetry.lock bestanden.

<br>

```
poetry add <package>
```

Voegt een nieuwe afhankelijkheid toe aan het project en installeert deze. De afhankelijkheid wordt toegevoegd aan de pyproject.toml file.
poetry update

Werkt alle afhankelijkheden bij naar de nieuwste versies die voldoen aan de versiebeperkingen in de pyproject.toml file en werkt het poetry.lock bestand bij.

<br>

```
poetry remove <package>
```

Verwijdert een afhankelijkheid uit het project en werkt de pyproject.toml en poetry.lock bestanden bij.

<br>

```
poetry init
```

Initialiseert een nieuw Poetry-project door een pyproject.toml bestand aan te maken met de door jou opgegeven instellingen.

<br>

```
poetry shell
```

Start een nieuwe shell met de virtuele omgeving van het project geactiveerd.

<br>

```
poetry run <command>
```

Voert een commando uit binnen de context van de virtuele omgeving van het project.

<br>

```
poetry lock
```

Genereert of vernieuwt het poetry.lock bestand met de exacte versies van de afhankelijkheden die zijn gedefinieerd in de pyproject.toml file.

<br>

```
poetry show
```

Toont informatie over de geïnstalleerde afhankelijkheden. Voeg -v toe voor meer gedetailleerde informatie.

<br>

```
poetry check
```

Controleert of de pyproject.toml en poetry.lock bestanden geldig zijn en of de afhankelijkheden correct kunnen worden opgelost.

<br>

```
poetry build
```

Bouwt de source en wheel distributiepakketten van het project.

<br>

```
poetry publish
```

Publiceert het pakket naar een pakketindex (zoals PyPI). Dit vereist dat je de juiste configuratie hebt ingesteld in je pyproject.toml.

<br>

```
poetry config <key> <value>
```

Stelt een configuratieoptie in voor Poetry. Bijvoorbeeld: poetry config virtualenvs.in-project true om de virtuele omgeving in de projectmap te maken.

<br>

```
poetry export -f requirements.txt --output requirements.txt
```

Exporteert de afhankelijkheden naar een requirements.txt bestand dat compatibel is met pip.

<br>

```
poetry cache:clear
```

Leegt de cache van Poetry.

<br>

```
poetry env list
```

Lijst alle virtuele omgevingen die door Poetry zijn aangemaakt voor het project.

<br>

```
poetry env use <python>
```

Wijzigt de Python-versie die wordt gebruikt door de virtuele omgeving van het project.
