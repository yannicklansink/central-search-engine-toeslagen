de stack die wordt gebruikt:

- Mongodb Atlas Vector Search: https://cloud.mongodb.com/v2/662ba1d382be592767f03c59#/overview | yannick.lansink@outlook.com
- Model used to generate vector embedding during index en query time: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- Model used to generate vector embedding during query time: text-embedding-ada-002

In movie-recs.py heb ik met de hugging face api, via een token, de embedding model MiniLM-L6-v2 gebruikt. Een 384 dimensionale vector. Hiermee heb zijn de eerste 50 gevonden velden van het 'plot' record gebruikt om een embedding te maken, daarna heb ik daarop een query met de nearest neibour algorime gebruikt om de meest relevante documenten terug te krijgen.

Ook heb ik Atlas Vector Search gebruikt om embeddings te genereren.

Daarnaast heb ik de al geembedde document database van Movies gebruikt met open ai text-embedding-ada-002 model om daar queries op te doen.
Dit zit in movie-recs-openai-embedding.py file.
