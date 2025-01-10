# How to Run the Project Locally

## Voorbereidingen

### Clone de repository:

```bash
git clone https://github.com/yannicklansink/central-search-engine-toeslagen
```

### Installeer vereiste software:

- **Python 3.11 of hoger**
- **Poetry**: Voor dependency management en virtual environments.
- **.NET SDK**: Voor het draaien van de Blazor WebAssembly applicatie.

## Stap 1: Configureer de Omgevingsvariabelen

### Maak een .env bestand:

1. Kopieer de inhoud van `env.example` naar een nieuw bestand genaamd `.env`.

```bash
cp env.example .env
```

2. Vul de juiste API-sleutels in voor Pinecone, OpenAI en LangChain Tracing.

```bash
PINECONE_API_KEY=<your-pinecone-api-key>
PINECONE_INDEX_NAME=langchain-unstructured-data
OPENAI_API_KEY=<your-openai-api-key>
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=<your-langchain-api-key>
```

## Stap 2: Start de Backend (RAG-service)

1. Navigeer naar de `RAG-service` directory:

```bash
cd RAG-service
```

2. Installeer de afhankelijkheden met Poetry:

```bash
poetry install
```

3. Start de RAG-service:

```bash
poetry run langchain serve
```

## Stap 3: Start de Frontend (Blazor WebAssembly)

1. Navigeer naar de `client/WebApp` directory:

```bash
cd client/WebApp
```

2. Start de Blazor WebAssembly applicatie:

```bash
dotnet run
```

## Opmerkingen

**Upload Functionaliteit**: Om gebruik te maken van de upload functionaliteit, moet je verbinding maken met het Azure account van yannick.lansink@live.nl. Dit is momenteel niet mogelijk aangezien het een persoonlijk account is.

## Samenvatting

1. Clone de repository en installeer vereiste software.
2. Configureer de omgevingsvariabelen in een `.env` bestand.
3. Start de backend door naar de `RAG-service` directory te navigeren en `poetry run langchain serve` uit te voeren.
4. Start de frontend door naar de `client/WebApp` directory te navigeren en `dotnet run` uit te voeren.

Met deze stappen zou je de applicatie lokaal moeten kunnen draaien. Veel succes!
