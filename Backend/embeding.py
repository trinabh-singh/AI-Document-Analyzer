from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

embedding_model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def create_vector_store(final_chunks):

    texts_to_embed = [
        chunk["content"]
        for chunk in final_chunks
    ]

    embeddings = embedding_model.encode(
        texts_to_embed
    ).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index