import os
import openai  # For version check only
from openai import OpenAI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

print("OpenAI SDK version:", openai.__version__)  # Debug check


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class ContextRequest(BaseModel):
    context: str

def query_gpt(prompt: str) -> str:
    chat_completion = client.chat.completions.create(
        model="gpt-4",
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
