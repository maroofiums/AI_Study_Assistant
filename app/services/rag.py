import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.services.embeddings import embedding_model
from app.services.vector_store import load_vector_store
from app.services.llm import llm
from app.services.schemas import StudentResponse

load_dotenv()

parser = PydanticOutputParser(
    pydantic_object=StudentResponse
)


prompt = ChatPromptTemplate.from_template(
    """
        You are an AI Study Assistant.

        Answer ONLY from the provided context.

        If the answer is not present in the context:

        - topic_title: "Not Found"
        - definition: "Information not available in the uploaded documents."
        - explanation: "Information not available in the uploaded documents."
        - examples: []

        Context:
        {context}

        Question:
        {question}

        {format_instructions}
    """
)

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

    chain = prompt | llm | parser

    result = chain.invoke(
        {
            "context": context,
            "question": query,
            "format_instructions": (
                parser.get_format_instructions()
            ),
        }
    )

    return result.model_dump()