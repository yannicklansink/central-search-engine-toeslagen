# Technisch Ontwerp Document (RAG-Service)

## Overzicht

**Doel van de Tech Stack:** De gekozen tech stack is ontworpen om een efficiënte, schaalbare en veilige chatapplicatie te ondersteunen die medewerkers van Integratie Business Services (IBS) Toeslagen helpt bij het vinden van informatie. De tech stack omvat zowel frontend- als backend-technologieën, hostingoplossingen en beveiligingsmaatregelen om een robuuste en gebruiksvriendelijke applicatie te leveren.

## Frontend

**Programmeertaal:**

- C#

**Frameworks:**

- Blazor WebAssembly: Voor het bouwen van interactieve webapplicaties met behulp van C# en .NET.

**Styling:**

- CSS: Voor het stylen van de gebruikersinterface.
- Bootstrap: Voor het gebruik van kant-en-klare stijlen en componenten.

**Build Tools:**

- .NET SDK: Voor het bouwen en publiceren van de Blazor WebAssembly applicatie.

## Backend

**Programmeertaal:**

- Python

**Frameworks:**

- FastAPI: Voor het opzetten van de API-server en het verwerken van verzoeken.
- LangChain: Voor het opzetten van de keten van bewerkingen die nodig zijn om een antwoord te genereren.
- Uvicorn: ASGI server voor het draaien van de FastAPI applicatie.

**Database:**

- Pinecone: Voor het opslaan en doorzoeken van vectorrepresentaties van documenten.

## Hosting

**Azure Functie:**

- Azure Functions: Voor het uitvoeren van serverless functies die specifieke taken uitvoeren, zoals het verwerken van geüploade bestanden.

**Vector Database:**

- Pinecone: Voor het hosten van de vector database die wordt gebruikt voor het opslaan en doorzoeken van vectorrepresentaties van documenten.

**Source Code:**

- GitHub: Voor het beheren van de broncode en versiebeheer.

**Azure Blob Storage:**

- Azure Blob Storage: Voor het opslaan van geüploade bestanden.

## Beveiliging

**Huidige status:** Momenteel wordt nog weinig gedaan op het gebied van beveiliging omdat het om een prototype gaat.

**Toekomstige maatregelen:** In de toekomst worden de volgende maatregelen genomen om ervoor te zorgen dat onze data veilig blijft:

- Data Encryptie: Alle data die wordt opgeslagen in Azure Blob Storage en Pinecone wordt versleuteld om ongeautoriseerde toegang te voorkomen.
- Veilige API-aanroepen: Gebruik van HTTPS voor alle API-aanroepen om ervoor te zorgen dat de data tijdens het transport wordt versleuteld.
- Beveiligingsprotocollen: Implementatie van strikte beveiligingsprotocollen en best practices om ervoor te zorgen dat gevoelige informatie niet toegankelijk is voor onbevoegde partijen.
- Regelmatige Beveiligingsaudits: Voeren van regelmatige beveiligingsaudits en penetratietests om potentiële kwetsbaarheden te identificeren en te verhelpen.
- Gebruik van Secure Credentials: Gebruik van veilige methoden voor het opslaan en beheren van API-sleutels en andere gevoelige informatie, zoals Azure Key Vault.
- LLM op eigen servers draaien: Het draaien van de Language Learning Models (LLM) op eigen servers om data in huis te houden.

Dit Tech Stack Document biedt een overzicht van de technologieën en beveiligingsmaatregelen die worden gebruikt voor de ontwikkeling en hosting van de chat app.
