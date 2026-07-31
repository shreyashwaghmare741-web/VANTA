def calculate(expression: str) -> str:
    try:
        result = eval(expression)
        return str(result)
    except Exception:
        return "Invalid expression."