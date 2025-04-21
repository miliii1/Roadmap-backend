with open("nombres.txt", "r") as archivo:
    nombres = archivo.readlines()

nombres = [n.strip() for n in nombres]
# Si quisieras hacerlo más flexible (aceptar también "a" minúscula), podrías poner: lambda x: x.lower().startswith("a")
largos = list(filter(lambda x: x[0] == "A", nombres))

with open("filtrados.txt", "w") as archivo:
    for nombre in largos:
        archivo.write(nombre + "\n")