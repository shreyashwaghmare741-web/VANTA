import os
import subprocess
import webbrowser

from utils.app_database import APP_DATABASE


def open_target(target: str):

    target = target.lower().strip()

    if target not in APP_DATABASE:
        return f"I couldn't find '{target}'."

    value = APP_DATABASE[target]

    if value.startswith("http"):
        webbrowser.open(value)
        return f"Opening {target}..."

    if value == "downloads":
        os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))
        return "Opening Downloads..."

    if value == "documents":
        os.startfile(os.path.join(os.path.expanduser("~"), "Documents"))
        return "Opening Documents..."

    if value == "pictures":
        os.startfile(os.path.join(os.path.expanduser("~"), "Pictures"))
        return "Opening Pictures..."

    subprocess.Popen(value, shell=True)

    return f"Opening {target}..."