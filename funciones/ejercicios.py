# 🔹 Ejercicio 1 – Función suma segura. Hacé una función llamada sumar_seguro que reciba dos números como parámetros. La función debe:
"""
Validar que los valores sean números (usá try / except)

Retornar la suma si está todo bien

Si hay error, retornar "Error: valores inválidos"

"""

def sumar_seguro(a, b):
    try:
        a = float(a)
        b = float(b)
        return a + b
    except ValueError:
        return "Error: valores inválidos"

print(sumar_seguro("5", 10))  # ➡️ 15
print(sumar_seguro("hola", 10))  # ➡️ Error

# Ejercicio 2 – Validar edad. Hacé una función validar_edad que reciba una edad como parámetro. Debe:
"""
Validar que sea un entero

Esté entre 0 y 120

Retornar "Edad válida" o "Edad inválida" según el caso

"""
def validar_edad(edad):
    try:
        edad = int(edad)
        if 0 <= edad <= 120:
            return "Valid age"
        else:
            return "Age out of range"
        
    except ValueError:
        return "Invalid age"
    
print(validar_edad(25))
print(validar_edad(130))
print(validar_edad("hola"))