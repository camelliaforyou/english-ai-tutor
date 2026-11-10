import httpx

from app.core.config import get_settings
from app.schemas.chat import Message

SYSTEM_PROMPT = """
You are a friendly English conversation tutor.

Your student is a Korean adult learning spoken English.

Rules:
1. Speak in natural, conversational English.
2. Use vocabulary appropriate for a beginner.
3. Keep your response to 1-3 short sentences.
4. Ask one relevant follow-up question.
5. Do not interrupt the conversation to correct every mistake.
6. When the student requests feedback, explain mistakes in Korean.
7. Never pretend you are a human.
"""


class LLMService:
    async def generate(self, messages: list[Message]) -> str:
        settings = get_settings()

        payload = {
            "model": settings.ollama_model,
            "stream": False,
            "think": False,
            "keep_alive": -1,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                *[message.model_dump() for message in messages],
            ],
            "options": {
                "temperature": 0.7,
                "num_predict": 120,
            },
        }

        async with httpx.AsyncClient(timeout=settings.ollama_timeout) as client:
            response = await client.post(
                f"{settings.ollama_base_url}/api/chat",
                json=payload,
            )
            response.raise_for_status()

        return response.json()["message"]["content"]
