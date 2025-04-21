with open("numeros.txt", "r") as archivo:
    numeros = archivo.readlines()

numeros = list(map(lambda x: int(x.strip()), numeros))
cuadrados = list(map(lambda x: round(x**0.5, 2), numeros))

with open("cuadrados.txt", "w") as archivo:
    for num in cuadrados:
        archivo.write(str(num) + "\n")