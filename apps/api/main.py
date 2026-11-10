import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="English AI Tutor API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "english-ai-tutor",
    }


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


SYSTEM_PROMPT = """
You are a friendly English conversation tutor.

Rules:
- Speak in natural English.
- Keep responses to 1-3 short sentences.
- Ask one follow-up question.
- Adapt your vocabulary to the student's level.
- Do not explain grammar unless asked.
"""


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    async with httpx.AsyncClient(timeout=120) as client:
        response = await client.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "qwen3.5:9b",
                "stream": False,
                "think": False,
                "keep_alive": -1,
                "messages": [
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT,
                    },
                    {
                        "role": "user",
                        "content": request.message,
                    },
                ],
                "options": {
                    "num_predict": 120,
                    "temperature": 0.7,
                },
            },
        )

        response.raise_for_status()
        result = response.json()

    return ChatResponse(reply=result["message"]["content"])
