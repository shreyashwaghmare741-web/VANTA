from ai.llm import ask_eon
from core.config import WELCOME_MESSAGE
from ui.spinner import Spinner


def main():

    print(WELCOME_MESSAGE)

    while True:

        user_input = input("\nYou > ")

        if user_input.lower() in ["exit", "quit"]:

            print("\nEON > Goodbye. Systems shutting down.")

            break

        try:

            spinner = Spinner("Thinking")

            try:
                spinner.start()
                reply = ask_eon(user_input)
            finally:
                spinner.stop()

            print(f"\nEON > {reply}")

        except Exception as e:

            print("\nEON Error:", e)


if __name__ == "__main__":

    main()