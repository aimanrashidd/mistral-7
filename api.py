from fastapi import FastAPI
from pydantic import BaseModel
import ollama

# Initialize FastAPI
app = FastAPI()

# Request structure
class ChatRequest(BaseModel):
    prompt: str  # User input prompt

# API Endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Use `stream=False` to avoid errors
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": request.prompt}], stream=False)

        # Extract response text
        final_response = response["message"]

        # Return both input and output
        return {
            "prompt": request.prompt,
            "response": final_response
        }
    
    except Exception as e:
        return {"error": str(e)}
