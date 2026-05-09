from fastapi import FastAPI
from fastapi import UploadFile, File
from pydantic import BaseModel

from ragpipeline import ask_question
from ragpipeline import load_pdf

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "RAG API Running"}

@app.post("/query")
async def query_rag(data: QueryRequest):

    answer = ask_question(data.query)

    return {
        "query": data.query,
        "answer": answer
    }

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_location = file.filename

    with open(file_location, "wb") as f:
        f.write(await file.read())

    load_pdf(file_location)

    return {
        "message": "PDF uploaded successfully"
    }