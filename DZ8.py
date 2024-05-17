import re


def safe_calculator(func):
    def wrapper(expression):
        # Перевірка на недопустимі символи
        if not re.match(r'^[\d+\-*/(). ]+$', expression):
            return "Error: Invalid characters in expression."

        try:
            result = func(expression)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero."
        except SyntaxError:
            return "Error: Syntax error in expression."
        except Exception as e:
            return f"Error: {str(e)}"

    return wrapper


@safe_calculator
def calculate(expression):
    return eval(expression)


# Приклади використання:
print(calculate("2 + 3 * 4"))
print(calculate("10 / 0"))
print(calculate("2 + (3 * 4"))
print(calculate("2 + 3 * 4 &"))
