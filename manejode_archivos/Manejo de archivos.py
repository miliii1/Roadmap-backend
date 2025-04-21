#MANEJO DE ARCHIVOS

names = ["Mili", "Juan", "Pedro", "Lucia"]

with open("names.txt", "w") as archivo:
    for name in names:
        archivo.write(name + "\n")
        #archivo.close()


with open("names.txt", "r") as archivos:
    for name in archivos:
        mejor = name.strip()  # Eliminar el salto de línea al final
        longitud = len(mejor)
        print(f"{name} => {longitud} letras")