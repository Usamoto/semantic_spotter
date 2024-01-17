from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from embedding_generator import model, generate_embeddings

def find_most_relevant_chunk(query, chunks, embeddings):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)
    most_relevant_chunk_index = np.argmax(similarities)
    return chunks[most_relevant_chunk_index]
