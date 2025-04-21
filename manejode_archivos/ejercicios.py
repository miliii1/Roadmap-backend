# Ejercicio 1: Cargar nombres desde archivo con verificación
"""
Intentá abrir un archivo llamado "nombres.txt".
Si existe, mostrás el contenido línea por línea.
Si no existe, mostrá "El archivo no fue encontrado".

Bonus: agregá un finally que diga "Fin del programa".

"""

"""try:
    with open("nombres.txt", "r") as archivo:
        for nombre in archivo:
            archivo.readline()
            print(nombre.strip())
except FileNotFoundError:
    print("El archivo no fue encontrado")
finally:
    print("Fin del programa")
"""


# Ejercicio 2: Calculadora segura
"""
Pedí 2 números al usuario.
Luego pedí una operación: +, -, *, /.
Realizá la operación elegida.
Usá try / except para manejar estos errores:
División por 0 (ZeroDivisionError)
Entrada inválida (ValueError)
Operación no reconocida (else o mensaje personalizado)

Bonus: mostrá un mensaje al final con finally diciendo "Gracias por usar la calculadora".

"""

"""try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operacion = input("Enter the operation (+, -, *, /): ")

    if operacion == "+":
        print(f"The result sum is: {num1 + num2}")
    elif operacion == "-":
        print(f"The result substraction is: {num1 - num2}")
    elif operacion == "*":
        print(f"The result multiplication is: {num1 * num2}")
    elif operacion == "/":
        print(f"The result division is: {num1 / num2}")
    else:
        print("Invalid operation. Please enter one of the following: +, -, *, /")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
finally:
    print("Thanks for using the calculator.")"""


# Desafío: Edad válida. Escribí un programa que: Pida al usuario que ingrese su edad.

"""
Verifique que sea un número entero.

Si la edad es válida (entre 0 y 120), mostrá "Edad válida: X años".

Si la edad es inválida (número negativo, o mayor a 120), mostrá "Edad fuera de rango válido".

Si escribe algo que no es número, mostrá "Entrada inválida, ingresá un número entero".

Mostrá "Programa finalizado" con un finally.

"""

try:
    edad = int(input("Enter your age: "))

    if 0 <= edad <= 120:
        print("Valid age: ", edad, "years")
    else:
        print("Age out of valid range")

except ValueError:
    print("Invalid input, please enter an intenger number")
finally:
    print("Program finished.")
