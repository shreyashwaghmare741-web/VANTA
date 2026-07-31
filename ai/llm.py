from ollama import chat # type: ignore
from core.config import MODEL_NAME


def ask_eon(prompt: str) -> str:

    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are EON (Enhanced Operations Nexus). "
                    "You are professional, intelligent and concise."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response["message"]["content"]