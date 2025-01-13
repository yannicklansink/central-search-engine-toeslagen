# Project Requirements Document

[Technisch Ontwerp Document](/technisch-ontwerp-document.md)

[Functioneel Ontwerp Document](/functioneel-ontwerp-document.md)

Technische uitleg: https://www.youtube.com/watch?v=Gk66Wk0aq-c

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

### Kern Functionaliteiten

Documentbeheer en Slimme Opslag

Functionaliteit: Klanten kunnen documenten uploaden, die veilig worden opgeslagen in een schaalbare Azure Blob Storage. Deze documenten worden automatisch geanalyseerd en voorbereid voor verdere verwerking.
Klantvraag: "Hoe kan ik mijn documenten veilig opslaan en eenvoudig terugvinden?"
Realtime Vraag-Antwoord API

Functionaliteit: De frontend verwerkt vragen van klanten via API-endpoints die direct relevante informatie uit documenten halen en terugsturen naar de gebruiker.
Klantvraag: "Kan ik vragen stellen over mijn documenten en snel antwoorden krijgen?"
Slimme Document Zoekfunctie

Functionaliteit: Klanten kunnen zoeken in documenten met behulp van een krachtige vector-gebaseerde zoekfunctionaliteit, waarmee semantische overeenkomsten worden gevonden, zelfs als trefwoorden niet exact overeenkomen.
Klantvraag: "Hoe kan ik snel informatie vinden in mijn documenten, zelfs als ik niet weet hoe het exact is geformuleerd?"
Automatische Documentanalyse met Embeddings

Functionaliteit: Bij het uploaden worden documenten automatisch geanalyseerd en embeddings gegenereerd met behulp van AI (OpenAI). Dit maakt semantische zoekopdrachten en geavanceerde data-extractie mogelijk.
Klantvraag: "Kan het systeem automatisch patronen of verbanden in mijn documenten herkennen?"
Persoonlijke Chatervaring met Geschiedenis

Functionaliteit: Klanten kunnen chatgesprekken voeren die specifieke informatie uit hun documenten halen. De chatgeschiedenis wordt lokaal opgeslagen zodat gebruikers kunnen terugkijken zonder zorgen over privacy.
Klantvraag: "Kan ik een gepersonaliseerde chatervaring hebben met toegang tot mijn eerdere vragen en antwoorden?"

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
