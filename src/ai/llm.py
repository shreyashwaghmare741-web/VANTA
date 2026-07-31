from typing import TypedDict

from ollama import chat  # type: ignore
from core.config import MODEL_NAME


class ChatMessage(TypedDict):
    role: str
    content: str


def ask_eon(messages: list[ChatMessage]) -> str:
    response = chat(
        model=MODEL_NAME,
        messages=messages,
    )

    return response["message"]["content"]