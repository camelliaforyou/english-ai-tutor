from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.schemas.chat import Message
from app.services.llm import LLMService


@pytest.mark.asyncio
async def test_llm_service_builds_correct_payload() -> None:
    mock_response = MagicMock()
    mock_response.json.return_value = {"message": {"content": "Nice to meet you!"}}

    mock_client = AsyncMock()
    mock_client.post.return_value = mock_response

    with patch("app.services.llm.httpx.AsyncClient") as client_class:
        client_class.return_value.__aenter__.return_value = mock_client

        service = LLMService()

        result = await service.generate([Message(role="user", content="Hello!")])

    assert result == "Nice to meet you!"

    _, kwargs = mock_client.post.call_args
    payload = kwargs["json"]

    assert payload["model"] == "qwen3.5:9b"
    assert payload["stream"] is False
    assert payload["think"] is False
    assert payload["keep_alive"] == -1

    assert payload["messages"][0]["role"] == "system"
    assert payload["messages"][1] == {
        "role": "user",
        "content": "Hello!",
    }
