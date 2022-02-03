import os

nueva_carpeta = input("el nombre de la nueva carpeta: ")
directorio_actual = os.getcwd()
print("este es su directorio:", directorio_actual)
path = os.path.join(directorio_actual, nueva_carpeta)

if os.path.exists(path):
    print("la carpeta ya existe")
else:
    os.mkdir(path)
    print("carpeta creada")
