import os

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from app.services.pdf_loader import load_pdf
from app.services.chunker import load_chunks
from app.services.embeddings import embedding_model
from app.services.vector_store import create_vector_store

router = APIRouter()

@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=404, detail="Only PDF Allows")

    UPLOAD_DIR = "uploads"

    os.makedirs(UPLOAD_DIR,exist_ok=True)

    pdf_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(pdf_path,"wb") as f:
        f.write(
            await file.read()
        )

    documents = load_pdf(pdf_path)

    chunks = load_chunks(documents)

    create_vector_store(
        chunks,
        embedding_model
    )

    return {
        "message": "PDF Upload Successfully...",
        "chunks": len(chunks)
    }