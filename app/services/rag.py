import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.vectorstores import FAISS

from app.services.embeddings import embedding_model
from app.services.vector_store import load_vector_store

load_dotenv()

llm = ChatMistralAI()

def ask_question(query):
    db = load_vector_store(
        embedding_model
    )

    retriever = db.as_retriever(
        search_type="mmr", 
        search_kwargs={
            "k": 5, 
            "fetch_k": 50
        }
    )

    docs = retriever.invoke(query)

    context = "\n\n".join(
        doc.page_content 
        for doc in docs
    )

    prompt = f"""
        Answer only using the provided context.

        Context:
        {context}

        Question:
        {query}
    """

    res = llm.invoke(prompt)

    return res.content