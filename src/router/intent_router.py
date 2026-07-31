class IntentRouter:

    def route(self, text: str) -> str:

        text = text.lower().strip()

        if any(op in text for op in ["+", "-", "*", "/"]):
            return "calculator"

        return "chat"