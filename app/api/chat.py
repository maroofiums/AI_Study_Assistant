from fastapi import APIRouter

from app.services.rag import ask_question

router = APIRouter()

@router.post("/chat")
def chat(
    query: str
):
    answer = ask_question(
        query
    )

    return {
        "question": query,
        "answer": answer
    }