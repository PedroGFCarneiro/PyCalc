import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Nao e possivel dividir por zero.")
    return a / b


def power(a, b):
    result = a ** b

    if isinstance(result, complex):
        raise ValueError("Resultado complexo nao suportado.")

    if not math.isfinite(result):
        raise ValueError("Resultado muito grande.")

    return result


def square_root(a):
    if a < 0:
        raise ValueError("Nao existe raiz real de numero negativo.")
    return math.sqrt(a)


def percentage(a, b):
    return (a * b) / 100