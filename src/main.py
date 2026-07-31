from ai.llm import ask_eon
from core.config import WELCOME_MESSAGE
from ui.spinner import Spinner
from memory.session import SessionMemory

from router.intent_router import IntentRouter
from skills.calculator import calculate


def main():

    print(WELCOME_MESSAGE)

    session_memory = SessionMemory()

    router = IntentRouter()

    while True:

        user_input = input("\nYou > ")

        if user_input.lower() in ["exit", "quit"]:

            print("\nEON > Goodbye. Systems shutting down.")

            break

        # -----------------------------
        # Step 1 : Decide what to do
        # -----------------------------
        intent = router.route(user_input)

        # -----------------------------
        # Step 2 : Calculator Skill
        # -----------------------------
        if intent == "calculator":

            result = calculate(user_input)

            print(f"\nEON > {result}")

            continue

        # -----------------------------
        # Step 3 : AI Chat
        # -----------------------------
        try:

            spinner = Spinner("Thinking")

            session_memory.add_user(user_input)

            messages = session_memory.get_messages()

            try:

                spinner.start()

                reply = ask_eon(messages)

                session_memory.add_assistant(reply)

            finally:

                spinner.stop()

            print(f"\nEON > {reply}")

        except Exception as e:

            print("\nEON Error:", e)


if __name__ == "__main__":

    main()