from langchain_community.vectorstores import FAISS

VECTOR_DB_PATH = "vector_db"

def create_vector_store(
    chunks,
    embeddings
):
    
    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    db.save_local(
        VECTOR_DB_PATH
    )

    return db

def load_vector_store(embeddings):

    return FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )