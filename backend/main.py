
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(title="AI Response Quality Evaluator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class EvaluationInput(BaseModel):
    question: str = Field(min_length=1, max_length=10000)
    answer: str = Field(min_length=1, max_length=30000)
    reference: str | None = Field(default=None, max_length=30000)


@app.get("/")
def home():
    return {
        "message": "AI Response Quality Evaluator API is running"
    }


@app.get("/api/health")
def health_check():
    return {"status": "healthy"}


@app.post("/api/evaluate")
def evaluate_response(data: EvaluationInput):
    return {
        "message": "Evaluation input received successfully",
        "question": data.question,
        "answer_length": len(data.answer),
        "reference_provided": bool(
            data.reference and data.reference.strip()
        ),
        "status": "received",
    }
