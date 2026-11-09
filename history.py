history = []


def add_history(operation, result):
    history.append({
        "operation": operation,
        "result": result
    })


def show_history():
    if not history:
        print("\nNenhuma operacao realizada ainda.")
        return

    print("\n========== HISTORICO ==========")

    for index, item in enumerate(history, start=1):
        print(f"{index}. {item['operation']} = {item['result']}")

    print("===============================")


def clear_history():
    history.clear()
    print("Historico apagado com sucesso!")