
from numeros import obtener_numeros
from operaciones import sumar, restar, multiplicar, dividir
from resultados import mostrar_resultados


def menu():
    print("\n=== Calculadora Equipo 5 ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    return input("Elige una opcion: ").strip()


def main():
    operaciones = {
        "1": ("Suma", sumar),
        "2": ("Resta", restar),
        "3": ("Multiplicacion", multiplicar),
        "4": ("Division", dividir),
    }

    while True:
        opcion = menu()

        if opcion == "5":
            print("Hasta luego!")
            break

        if opcion not in operaciones:
            print("Opcion no valida, intenta de nuevo.")
            continue

        nombre, funcion = operaciones[opcion]
        a, b = obtener_numeros()

        try:
            resultado = funcion(a, b)
            mostrar_resultados(nombre, a, b, resultado)
        except ZeroDivisionError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
