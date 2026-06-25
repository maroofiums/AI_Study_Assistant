from fastapi import APIRouter

from app.services.rag import ask_question

router = APIRouter()

@router.post("/chat")
def chat(
    query: str
):
    return ask_question(query)