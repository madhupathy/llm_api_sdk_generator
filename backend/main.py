from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class ContextRequest(BaseModel):
    context: str

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def query_gpt(prompt: str) -> str:
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}]
    )
    return chat_completion.choices[0].message.content.strip()

@app.post("/generate")
def generate_api_content(req: ContextRequest):
    context = req.context
    prompts = {
        "openapi": f"Generate OpenAPI 3.0 documentation for the following API context:\n{context}",
        "grpc": f"Generate a .proto file with gRPC service and messages for:\n{context}",
        "sdk": f"Generate a Python SDK class that wraps around the REST endpoints for:\n{context}"
    }
    result = {k: query_gpt(v) for k, v in prompts.items()}
    return result

@app.get("/")
async def root():
    return {"message": "Backend is up and running!"}
