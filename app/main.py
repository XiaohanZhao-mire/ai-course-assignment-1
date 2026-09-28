"""Module 3 API, extended with a word-embedding endpoint for Assignment 1."""

from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query, Request
from pydantic import BaseModel, Field, StringConstraints

from app.bigram_model import BigramModel
from app.embedding_model import EmbeddingModel

corpus = [
    "The Count of Monte Cristo is a novel written by Alexandre Dumas. "
    "It tells the story of Edmond Dantès, who is falsely imprisoned and later seeks revenge.",
    "this is another example sentence",
    "we are generating text based on bigram probabilities",
    "bigram models are simple but effective",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.bigram_model = BigramModel(corpus)
    app.state.embedding_model = EmbeddingModel()
    yield


app = FastAPI(title="Assignment 1: Word Embeddings API", version="0.1.0", lifespan=lifespan)

Word = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=100)]


class TextGenerationRequest(BaseModel):
    start_word: Annotated[Word, Field(pattern=r"^\w+$")]
    length: Annotated[int, Field(strict=True, ge=1, le=200)] = 20


class TextGenerationResponse(BaseModel):
    generated_text: str


class EmbeddingResponse(BaseModel):
    word: str
    model: str
    dimensions: int
    embedding: list[float]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/generate", response_model=TextGenerationResponse)
def generate_text(body: TextGenerationRequest, request: Request):
    return {"generated_text": request.app.state.bigram_model.generate_text(body.start_word, body.length)}


@app.get("/embedding", response_model=EmbeddingResponse)
def get_embedding(request: Request, word: Annotated[Word, Query(description="One English word", examples=["apple"])]):
    """Return the complete spaCy vector. Unknown vocabulary returns HTTP 404."""
    try:
        return request.app.state.embedding_model.calculate_embedding(word)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
