import os
import uuid

from loader import load_document
from chunker import chunk_text
from embeddings import create_embedding
from db import collection

DOCS_PATH = "./documents"

files = os.listdir(DOCS_PATH)

for file in files:

    path = os.path.join(DOCS_PATH, file)

    print(f"Processing {file}")

    text = load_document(path)

    chunks = chunk_text(text)

    for chunk in chunks:

        embedding = create_embedding(chunk)

        collection.add(
            ids=[str(uuid.uuid4())],
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[{
                "source": file
            }]
        )

print("Documents indexed successfully")