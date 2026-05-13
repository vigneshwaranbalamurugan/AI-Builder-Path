from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.retriever import retrieve
from app.prompts import build_prompt
from app.llm import generate

app = FastAPI()

# mount static directory
app.mount("/static", StaticFiles(directory="./app/static"), name="static")

class ChatRequest(BaseModel):
    question: str


@app.get("/", response_class=HTMLResponse)
def index():
    with open("app/static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


@app.post("/chat")
def chat(req: ChatRequest):

    results = retrieve(req.question)

    docs = results["documents"][0]

    prompt = build_prompt(
        docs,
        req.question
    )
    print(docs)
    answer = generate(prompt)

    return {
        "answer": answer,
        "sources": results["metadatas"][0]
    }