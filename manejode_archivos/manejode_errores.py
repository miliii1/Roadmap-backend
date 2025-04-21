# Ejercicio sugerido
# Escribí un programa que: Le pida al usuario un número. Lo convierta a entero. Divida 100 entre ese número. Maneje estos errores: ZeroDivisionError, ValueError, Muestre un mensaje final con finally.

try:
    numero = int(input("Enter a number: "))
    resultado = int(100 / numero)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print(f"The result is: {resultado}")
finally:
    print("Exexution completed.")