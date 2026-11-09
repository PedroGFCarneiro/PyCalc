import calculator
import history


def show_menu():
    print("\n" + "=" * 40)
    print("          PYCALC - CALCULADORA")
    print("=" * 40)
    print("[1] Adicao")
    print("[2] Subtracao")
    print("[3] Multiplicacao")
    print("[4] Divisao")
    print("[5] Potenciacao")
    print("[6] Raiz quadrada")
    print("[7] Porcentagem")
    print("[8] Historico")
    print("[9] Limpar historico")
    print("[0] Sair")
    print("=" * 40)


def get_number(message):
    while True:
        try:
            return float(input(message).replace(",", "."))
        except ValueError:
            print("ERRO: Digite um numero valido.")


def format_result(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return round(value, 10)


def execute_calculation(option):
    operations = {
        "1": ("Adicao", calculator.add, "+"),
        "2": ("Subtracao", calculator.subtract, "-"),
        "3": ("Multiplicacao", calculator.multiply, "*"),
        "4": ("Divisao", calculator.divide, "/"),
        "5": ("Potenciacao", calculator.power, "^"),
        "7": ("Porcentagem", calculator.percentage, "%")
    }

    if option == "6":
        number = get_number("Digite o numero: ")
        result = format_result(calculator.square_root(number))
        operation = f"Raiz quadrada de {number}"
    else:
        _, function, symbol = operations[option]
        first = get_number("Primeiro numero: ")
        second = get_number("Segundo numero: ")
        result = format_result(function(first, second))
        operation = f"{first} {symbol} {second}"

    history.add_history(operation, result)

    print("\n========== RESULTADO ==========")
    print(f"Operacao: {operation}")
    print(f"Resultado: {result}")
    print("===============================")


def main():
    print("\nBem-vindo ao PyCalc!")

    while True:
        show_menu()
        option = input("Escolha uma opcao: ").strip()

        if option == "0":
            print("Obrigado por utilizar o PyCalc!")
            break

        elif option in ["1", "2", "3", "4", "5", "6", "7"]:
            try:
                execute_calculation(option)
            except (ValueError, ZeroDivisionError) as error:
                print(f"ERRO: {error}")
            except OverflowError:
                print("ERRO: Resultado muito grande.")

        elif option == "8":
            history.show_history()

        elif option == "9":
            history.clear_history()

        else:
            print("Opcao invalida!")


if __name__ == "__main__":
    main()