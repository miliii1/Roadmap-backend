try:
    edad = int(input("Enter your age: "))
    if edad > 18:
        print("Puede ingresar.")
    elif edad < 0:
        print("La edad no puede ser negativa. ")
    else:
        print("No puedes ingresar. Eres menor de edad")
except ValueError:
    print ("No es un número válido.")
except Exception as e:
    print("Ocurrió un error inesperado:", e)

