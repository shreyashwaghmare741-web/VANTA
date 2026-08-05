from ai.llm import ask_vanta
from core.config import WELCOME_MESSAGE, GOODBYE_MESSAGE
from ui.spinner import Spinner
from memory.session import SessionMemory
from router.intent_router import IntentRouter
from skills.skill_manager import SkillManager


def main():

    print(WELCOME_MESSAGE)

    session_memory = SessionMemory()

    router = IntentRouter()

    skill_manager = SkillManager()

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