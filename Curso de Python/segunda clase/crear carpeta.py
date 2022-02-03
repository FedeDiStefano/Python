import os

nueva_carpeta = input("el nombre de la nueva carpeta: ")
directorio_actual = os.getcwd()
print("este es su directorio:", directorio_actual)
# PS E:\Python
path = os.path.join(directorio_actual, nueva_carpeta)
#print("nueva carpeta ruta:", path)
os.mkdir(path)
