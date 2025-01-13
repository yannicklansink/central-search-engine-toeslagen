# Functioneel Ontwerp Document (RAG-Service)

## Overzicht

**Doel van de Backend:**  
De backend van de RAG-service is ontworpen om de chatapplicatie te ondersteunen die medewerkers van Integratie Business Services (IBS) Toeslagen helpt bij het vinden van informatie. De backend verwerkt verzoeken, voert zoekopdrachten uit in een vector database, en genereert antwoorden met behulp van een Large Language Model (LLM).

## Belangrijke Kern Functionaliteiten uitgewerkt in passend functionele requirements

### Functionele Requirements

#### Document Upload Functionaliteit

- **FR1.1:** Gebruikers moeten in staat zijn om documenten te uploaden via de frontend interface. Dit stelt gebruikers in staat om relevante informatie beschikbaar te maken voor verdere verwerking en analyse.
- **FR1.2:** De applicatie moet verschillende bestandsformaten ondersteunen, zoals .txt, .pdf en .html. Dit zorgt voor flexibiliteit en gebruiksgemak voor de gebruikers.
- **FR1.3:** Na het uploaden moet de gebruiker een bevestiging ontvangen dat het document succesvol is geüpload. Dit biedt duidelijkheid en zekerheid aan de gebruiker.

#### Realtime Vraag-Antwoord API

- **FR2.1:** Gebruikers moeten vragen kunnen stellen via de frontend interface. Dit maakt interactie met de applicatie mogelijk en verbetert de gebruikerservaring.
- **FR2.2:** De applicatie moet real-time antwoorden kunnen geven op basis van de geüploade documenten. Dit zorgt voor snelle en relevante informatieverstrekking.
- **FR2.3:** De antwoorden moeten relevant en nauwkeurig zijn. Dit verhoogt de betrouwbaarheid en bruikbaarheid van de applicatie.

#### Slimme Document Zoekfunctie

- **FR3.1:** De zoekfunctionaliteit moet semantische overeenkomsten kunnen vinden, zelfs als trefwoorden niet exact overeenkomen. Dit verbetert de nauwkeurigheid en relevantie van de zoekresultaten.
- **FR3.2:** De zoekresultaten moeten relevant en nauwkeurig zijn. Dit verhoogt de tevredenheid en efficiëntie van de gebruikers.

#### Automatische Documentanalyse met Embeddings

- **FR4.1:** Bij het uploaden moeten documenten automatisch worden geanalyseerd. Dit zorgt voor een efficiënte en effectieve verwerking van documenten.
- **FR4.2:** De applicatie moet embeddings genereren met behulp van AI (OpenAI). Dit verbetert de mogelijkheden voor verdere analyse en zoekfunctionaliteit.
- **FR4.3:** De gegenereerde embeddings moeten worden effectief worden opgeslagen in chunks. Dit zorgt voor een efficiënte opslag en verwerking van embeddings.

#### Persoonlijke Chatervaring met Geschiedenis

- **FR5.1:** Gebruikers moeten chatgesprekken kunnen voeren via de frontend interface. Dit verbetert de interactie en gebruikerservaring.
- **FR5.2:** De chatgeschiedenis moet lokaal worden opgeslagen zodat gebruikers kunnen terugkijken. Dit verhoogt de bruikbaarheid en functionaliteit van de applicatie.
- **FR5.3:** De chatgeschiedenis moet veilig en privé worden opgeslagen. Dit zorgt voor de privacy en veiligheid van de gebruikersgegevens.

## Wireframe

### Overzicht pagina'

- **Home:** Welkomstpagina van de applicatie.
- **Chat:** Chatinterface waar gebruikers vragen kunnen stellen en antwoorden ontvangen.
- **Upload:** Interface voor het uploaden van documenten naar de blob storage.

### Schets van chat interface

![Wireframe van de chatinterface](/resources//img/image-wireframe-chat.png)

### Schets van upload interface

![Wireframe van uploadinterface](/resources/img/image-upload-interface.png)

## Technologiestack

- **Programmeertaal:** Python
- **Web Framework:** FastAPI
- **Vector Database:** Pinecone
- **Embeddings:** OpenAI
- **Cloud Storage:** Azure Blob Storage
- **Dependency Management:** Poetry en requirements.txt files

## Architectuur

### Belangrijke Componenten

- **FastAPI:** Voor het opzetten van de API-server en het verwerken van verzoeken.
- **Pinecone:** Voor het opslaan en doorzoeken van vectorrepresentaties van documenten.
- **OpenAI:** Voor het genereren van embeddings en het beantwoorden van vragen.
- **Azure Blob Storage:** Voor het opslaan van geüploade documenten.
- **LangChain:** Voor het opzetten van de keten van bewerkingen die nodig zijn om een antwoord te genereren.

### Third-Party Integraties

- **Azure:** Voor blob storage.
- **Pinecone:** Voor vector database functionaliteit.
- **OpenAI:** Voor het genereren van embeddings en het beantwoorden van vragen.

## API Specificaties

### Endpoints

- `GET /`: Redirect naar de API-documentatie.
- `POST /RAG/stream`: Verwerkt een vraag en streamt het antwoord terug naar de client.

## Database Structuur

### Vector Database

- **Pinecone:** Slaat vectorrepresentaties van documenten op. Deze vectoren worden gebruikt om snel relevante informatie te vinden op basis van de semantische inhoud van de vraag.

### Wat slaan we op

- **Documenten:** Geüploade documenten worden opgeslagen in Azure Blob Storage voor een tijdelijke duur.
- **Embeddings:** Vectorrepresentaties van documenten worden opgeslagen in Pinecone.
- **Chatgeschiedenis:** Opslaan van chatgeschiedenis in de browser's localStorage.

## Azure Function

### Waarom we deze gebruiken

Azure Functions worden gebruikt om serverless computing mogelijk te maken, wat schaalbaarheid en kostenbesparing biedt. Ze worden gebruikt om specifieke taken uit te voeren, zoals het verwerken van geüploade bestanden.

### Hoe het werkt met triggers

Azure Functions worden geactiveerd door triggers, zoals het uploaden van een bestand naar een specifieke container in Azure Blob Storage. Wanneer een bestand wordt geüpload, wordt de functie geactiveerd om het bestand te verwerken en op te slaan.

## Monitoring en Logging

### Hoe loggen we met LangSmith

LangSmith is een tool die wordt gebruikt voor het loggen en monitoren van API-aanroepen naar een Large Language Model (LLM). Het helpt bij het bijhouden van de keten van bewerkingen die worden uitgevoerd om een antwoord te genereren. Dit omvat het loggen van verzoeken, antwoorden en eventuele fouten die optreden tijdens de verwerking. Hierdoor kunnen ontwikkelaars beter inzicht krijgen in de prestaties en betrouwbaarheid van hun LLM-integraties.

**Voorbeeldcode voor logging:**
![alt text](/resources//img/image.png)

Dit Backend Structure Document biedt een overzicht van de doelstellingen, technologieën, architectuur, API-specificaties, database-structuur, Azure Functions, en monitoring en logging van de RAG-service.
