import os

directorio = os.getcwd()
with os.scandir(path=directorio) as itr:
    for i in itr:
        if i.is_file():
            print("es un archivo -> ", i.name)
        elif i.is_dir():
            print("es una carpeta -> ", i.name)
