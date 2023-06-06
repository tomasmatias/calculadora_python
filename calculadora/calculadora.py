# Calculadora básica


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre CEROS"


# Función principal


def main():
    print("Calculadora")

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    print("Elige una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Ingrese una opción: ")

    resultado = 0

    if opcion == "1":
        resultado = sumar(num1, num2)
    elif opcion == "2":
        resultado = restar(num1, num2)
    elif opcion == "3":
        resultado = multiplicar(num1, num2)
    elif opcion == "4":
        resultado = dividir(num1, num2)
    else:
        print("Opción Inválida.")
        return

    print("El resultado es:", resultado)


# Llamada a la función principal
main()
