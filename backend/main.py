from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import openai

# Set OpenAI API key from Render environment variable
openai.api_key = os.environ["OPENAI_API_KEY"]

# FastAPI app setup
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class ContextRequest(BaseModel):
    context: str

# Use OpenAI Chat API
def query_gpt(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

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
