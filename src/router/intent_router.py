class IntentRouter:

    def route(self, text: str) -> str:

        text = text.lower().strip()

        # Calculator
        if any(op in text for op in ["+", "-", "*", "/"]):
            return "calculator"

        # Battery
        if any(word in text for word in [
            "battery",
            "charge",
            "charging"
        ]):
            return "battery"

        # CPU
        if any(word in text for word in [
            "cpu",
            "processor"
        ]):
            return "cpu"

        # RAM
        if any(word in text for word in [
            "ram",
            "memory"
        ]):
            return "ram"

        # Disk
        if any(word in text for word in [
            "disk",
            "storage",
            "drive"
        ]):
            return "disk"

        # System Info
        if any(word in text for word in [
            "system",
            "computer",
            "pc"
        ]):
            return "system"

        return "chat"