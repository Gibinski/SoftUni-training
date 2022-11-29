def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError("Zero Division")

def pow(a, b):
    return a ** b


def calculate(a: float, b: float, op: str):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return sub(a, b)
    elif op == "*":
        return mul(a, b)
    elif op == "/":
        return div(a, b)
    elif op == "^":
        return pow(a, b)
    else:
        raise ValueError("Not supported operation")
    

def calculate_expression(expression):
    first, operator, second = expression.split()
    return calculate(float(first), float(second), operator)