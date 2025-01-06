# Project Requirements Document

[Technisch Ontwerp Document](/technisch-ontwerp-document.md)

[Functioneel Ontwerp Document](/functioneel-ontwerp-document.md)

## Project Overzicht

**Doel van de App:**  
De chatapplicatie is ontworpen om medewerkers van Integratie Business Services (IBS) Toeslagen te ondersteunen bij het vinden van informatie. Door gebruik te maken van een redeneringsmodel, een vector database en een Large Language Model (LLM), kan de applicatie complexe vraagstukken direct en nauwkeurig beantwoorden. Dit verhoogt de efficiëntie en tevredenheid van de medewerkers.

## Gebruikers

- Medewerkers van IBS Toeslagen
- Nieuwe medewerkers die snel toegang nodig hebben tot informatie
- Ervaren medewerkers die ondersteuning nodig hebben bij complexe vraagstukken

## Voordelen

- Verhoogde efficiëntie en effectiviteit van teams
- Snellere toegang tot benodigde informatie
- Verhoogde tevredenheid onder medewerkers
- Ondersteuning bij het beantwoorden van complexe vraagstukken

## Functionaliteiten

### Schermen

- **Home:** Welkomstpagina van de applicatie.
- **RAG Invoke:** Chatinterface waar gebruikers vragen kunnen stellen en antwoorden ontvangen.
- **Upload:** Interface voor het uploaden van documenten naar de blob storage.

### Features

- Chatfunctionaliteit met real-time antwoorden
- Document upload functionaliteit
- Opslag en ophalen van chatgeschiedenis
- Integratie met Pinecone vector database en OpenAI embeddings

### Functionaliteiten

- Real-time chat met ondersteuning voor complexe vraagstukken
- Documenten uploaden en opslaan in Azure Blob Storage
- Genereren van embeddings voor documenten
- Zoeken in de vector database op basis van embeddings
- Opslaan en ophalen van chatgeschiedenis in de browser

## Technische Specificaties

### Platform

- Azure voor cloud services
- Blazor WebAssembly voor de frontend
- FastAPI voor de backend
- Pinecone voor de vector database
- Langsmith voor monitoring en logging llm calls

### Technologieën

- Azure Blob Storage voor documentopslag
- Pinecone voor de vector database
- OpenAI voor embeddings en LLM
- Blazor voor de frontend
- FastAPI voor de backend

### API's

- Azure Storage API voor blob opslag
- Pinecone API voor vector database interacties
- OpenAI API voor embeddings en LLM

## Designvereisten

### UI

- Gebruiksvriendelijke interface met duidelijke navigatie
- Responsief ontwerp voor verschillende schermformaten
- Intuïtieve chatinterface met real-time updates

### UX

- Snelle en nauwkeurige antwoorden op vragen
- Eenvoudige uploadfunctionaliteit voor documenten
- Duidelijke feedback aan gebruikers bij interacties

## Hoofdstromen

- **Gebruiker stelt een vraag in de chatinterface:** De vraag wordt verwerkt en een antwoord wordt gegenereerd op basis van de context in de vector database.
- **Gebruiker uploadt een document:** Het document wordt opgeslagen in Azure Blob Storage, waardoor er een trigger afgaat, dan pakt een azure functie het op en converteert het naar een embedding en slaat het op in Pinecone.

**Reden:** Het ontwerp is gericht op het verbeteren van de efficiëntie en tevredenheid van medewerkers door hen snel en nauwkeurig toegang te geven tot benodigde informatie.

## Data Opslag

### Hoe slaan we data op

- Documenten worden opgeslagen in Azure Blob Storage.
- Embeddings van documenten worden opgeslagen in Pinecone vector database.
- Chatgeschiedenis wordt opgeslagen in de browser's localStorage.

### Vector Database

- Pinecone wordt gebruikt als vector database voor het opslaan en doorzoeken van embeddings.

## Hoofdstructuur en Mappenstructuur

### Hoofdstructuur

- **Frontend:** Blazor WebAssembly applicatie
- **Backend:** FastAPI applicatie voor het beschikbaar stellen van de RAG-service
- **Database:** Pinecone vector database
- **Storage:** Azure Blob Storage

### Mappenstructuur

Dit Project Requirements Document biedt een overzicht van de doelstellingen, functionaliteiten, technische specificaties, designvereisten, data opslag en de hoofdstructuur van de applicatie.
