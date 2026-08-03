from typing import Any, Callable

from ai.llm import ask_vanta
from core.config import WELCOME_MESSAGE, GOODBYE_MESSAGE
from ui.spinner import Spinner
from memory.session import SessionMemory
from router.intent_router import IntentRouter

from skills.calculator import calculate
from skills.system import battery, cpu, ram, disk, system_info
from skills.automation import open_target


class VantaSkillManager:
    """Registers and executes all built-in VANTA skills."""

    def __init__(self):
        self._skills: dict[str, Callable[..., Any]] = {}

        self.register_skill("calculator", calculate)
        self.register_skill("battery", battery)
        self.register_skill("cpu", cpu)
        self.register_skill("ram", ram)
        self.register_skill("disk", disk)
        self.register_skill("system", system_info)
        self.register_skill("open", open_target)

    def register_skill(self, name: str, handler: Callable[..., Any]) -> None:
        self._skills[name.lower()] = handler

    def execute(self, intent: str, user_input: str):

        handler = self._skills.get(intent.lower())

        if handler is None:
            return None

        if intent == "calculator":
            return handler(user_input)

        elif intent == "open":
            target = user_input.replace("open", "", 1).strip()
            return handler(target)

        else:
            return handler()


def main():

    print(WELCOME_MESSAGE)

    session_memory = SessionMemory()

    router = IntentRouter()

    skill_manager = VantaSkillManager()

    while True:

        user_input = input("\nYou > ")

        if user_input.lower() in ["exit", "quit"]:

            print(GOODBYE_MESSAGE)

            break

        # -----------------------------
        # Decide Intent
        # -----------------------------
        intent = router.route(user_input)

        # -----------------------------
        # Execute Local Skill
        # -----------------------------
        result = skill_manager.execute(intent, user_input)

        if result is not None:

            print(f"\nVANTA > {result}")

            continue

        # -----------------------------
        # AI Chat
        # -----------------------------
        try:

            spinner = Spinner("Thinking")

            session_memory.add_user(user_input)

            messages = session_memory.get_messages()

            try:

                spinner.start()

                reply = ask_vanta(messages)

                session_memory.add_assistant(reply)

            finally:

                spinner.stop()

            print(f"\nVANTA > {reply}")

        except Exception as e:

            print(f"\nVANTA Error: {e}")


if __name__ == "__main__":

    main()