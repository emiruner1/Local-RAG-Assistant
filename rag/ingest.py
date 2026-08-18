import os

from utils.pdf_loader import load_pdf
from utils.chunker import chunk_text
from config import CHUNK_SIZE

from rag.embeddings import create_embedding, embedding_to_json

from database.sqlite_manager import create_table, insert_chunk


def ingest(pdf_path):
    create_table()

    text = load_pdf(pdf_path)
    chunks = chunk_text(text, chunk_size=CHUNK_SIZE)

    source = os.path.basename(pdf_path)

    for chunk in chunks:
        embedding = create_embedding(chunk)

        insert_chunk(
            source,
            chunk,
            embedding_to_json(embedding)
        )

    print("Ingestion completed.")
