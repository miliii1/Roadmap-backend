from datetime import datetime

try:
    name = input("Enter your name: ")
    
    if not name.strip():
        print("Invalid name. Please enter a valid name.")
    else:
        age = int(input("Enter your age: "))
        valor = ""

        if age < 0:
            valor = "Access denied. Age cannot be negative."
        elif age > 18:
            valor = "Access valid! :)"
        else:
            valor = "Access denied. You age underage."

        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("registro.txt", "a") as archivo:
            archivo.write(f"Nombre: {name}  |  Edad: {age}  |  Resultado: {valor} |  Date: {fecha_hora}\n")


except ValueError:
    print("No es un número válido.")
except KeyboardInterrupt:
    print("\nSe canceló la entrada.")
except Exception as e:
    print("Ocurrió un error inesperado:", e)


    
