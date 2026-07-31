import itertools
import threading
import time


class Spinner:
    def __init__(self, text: str = "Thinking"):
        self.text = text
        self.running = False
        self.thread = None

    def spin(self):

        for symbol in itertools.cycle(["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]):

            if not self.running:
                break

            print(f"\r[EON] {self.text} {symbol}", end="", flush=True)

            time.sleep(0.1)

        print("\r" + " "*60 + "\r", end="")

    def start(self):

        self.running = True

        self.thread = threading.Thread(target=self.spin)

        self.thread.start()

    def stop(self):

        self.running = False

        self.thread.join() # type: ignore