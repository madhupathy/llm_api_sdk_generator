from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with new SDK
client = OpenAI(api_key=openai_api_key)

# Initialize FastAPI app
app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Request model
class ContextRequest(BaseModel):
    context: str

# GPT query function
def query_gpt(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# POST endpoint for API generation
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

# GET health check endpoint
@app.get("/")
async def root():
    return {"message": "Backend is up and running!"}
