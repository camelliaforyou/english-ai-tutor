import httpx
from fastapi import APIRouter, HTTPException

from app.core.config import get_settings
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.llm import LLMService

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    service = LLMService()

    try:
        reply = await service.generate(request.messages)
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=503,
            detail="LLM service is unavailable",
        ) from exc

    return ChatResponse(
        reply=reply,
        model=get_settings().ollama_model,
    )
