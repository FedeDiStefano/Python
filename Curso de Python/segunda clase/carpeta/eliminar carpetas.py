import os

eliminar_carpeta = input(
    "introduzca el nombre de la carpeta que vas a eliminar: ")

directorio_actual = os.getcwd()

path = os.path.join(directorio_actual, eliminar_carpeta)

if os.path.exists(path):
    os.rmdir(path)
    print("la carpeta se elimino correctamente")
else:
    print("la carpeta no existe")
