from skills.calculator import calculate
from skills.system import battery, cpu, ram, disk, system_info
from skills.automation import open_target


class SkillManager:

    def execute(self, intent: str, user_input: str):

        # -------------------------
        # Calculator
        # -------------------------
        if intent == "calculator":
            return calculate(user_input)

        # -------------------------
        # System Monitoring
        # -------------------------
        elif intent == "battery":
            return battery()

        elif intent == "cpu":
            return cpu()

        elif intent == "ram":
            return ram()

        elif intent == "disk":
            return disk()

        elif intent == "system":
            return system_info()

        # -------------------------
        # Desktop Automation
        # -------------------------
        elif intent == "open":
            return open_target(user_input)

        # -------------------------
        # AI Required
        # -------------------------
        return None