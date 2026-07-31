from ai.llm import ask_eon
from core.config import WELCOME_MESSAGE
from ui.spinner import Spinner
from memory.session import SessionMemory

def main():

    print(WELCOME_MESSAGE)

    session_memory = SessionMemory()  # type: ignore

    while True:

        user_input = input("\nYou > ")

        if user_input.lower() in ["exit", "quit"]:

            print("\nEON > Goodbye. Systems shutting down.")

            break

        try:

            spinner = Spinner("Thinking")

            try:
                spinner.start()
                session_memory.add_user(user_input)

                messages = session_memory.get_messages()

                reply = ask_eon(messages)
                session_memory.add_assistant(reply)
            finally:
                spinner.stop()

            print(f"\nEON > {reply}")

        except Exception as e:

            print("\nEON Error:", e)


if __name__ == "__main__":

    main()