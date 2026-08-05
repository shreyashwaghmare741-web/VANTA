from skills.registry import get
from skills.loader import load_skills


class SkillManager:

    def __init__(self):

        # Import every skill automatically
        load_skills()

    def execute(self, intent: str, user_input: str):

        handler = get(intent)

        if handler is None:
            return None

        if intent == "calculator":
            return handler(user_input)

        elif intent == "open":
            target = user_input.replace("open", "", 1).strip()
            return handler(target)

        return handler()