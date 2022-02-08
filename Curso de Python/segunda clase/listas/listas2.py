import random
lista = []
for i in range(9):
    lista.append(i)
    print(lista)


lista2 = [i for i in range(9)]
print(lista2)


lista3 = [i for i in range(9) if i % 2 == 0]
print(lista3)


lista4 = [i/2 for i in range(9)]
print(lista4)


nombres = ["Juan", "Fede",
           "Beni", "Lucho"]
print(nombres)
nombres = [i.upper() for i in nombres]
print(nombres)
nombres = [i.lower() for i in nombres]
print(nombres)


class estudiante ():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota


estudiantes = list()

for i in nombres:
    nota = random.randint(0, 11)
    e = estudiante(i, nota)
    estudiantes.append(e)
print(estudiantes)
suma = sum(e.nota for e in estudiantes)
print(suma)
maximo = max(e.nota for e in estudiantes)
print(maximo)
minimo = min(e.nota for e in estudiantes)
print(minimo)
