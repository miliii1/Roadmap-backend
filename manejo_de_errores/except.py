try:
    numero = int(input("Ingresá un número: "))
    print(100 / numero)
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except ValueError:
    print("Eso no es un número válido.")