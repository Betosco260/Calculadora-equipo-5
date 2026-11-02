def leer_numero(numero_entrada):
    while True:
        entrada = input(numero_entrada).strip()

        if not entrada:
            print("Error: introduce un numero.")
            continue

        try:
            numero = float(entrada)
        except ValueError:
            print("Error: introduce un numero valido.")
            continue

        return numero


def obtener_numeros():
    a = leer_numero("Introduce el primer numero: ")
    b = leer_numero("Introduce el segundo numero: ")

    return a, b