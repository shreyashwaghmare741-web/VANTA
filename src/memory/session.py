from typing import TypedDict


class Message(TypedDict):
    role: str
    content: str


class SessionMemory:

    def __init__(self):
        self.messages: list[Message] = []

    def add_user(self, message: str) -> None:
        self.messages.append({
            "role": "user",
            "content": message
        })

    def add_assistant(self, message: str) -> None:
        self.messages.append({
            "role": "assistant",
            "content": message
        })

    def get_messages(self) -> list[Message]:
        return self.messages[-20:]