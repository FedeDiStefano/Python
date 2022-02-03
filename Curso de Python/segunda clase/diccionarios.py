dic = {
    "1": "araña",
    "2": "escolopendra",
    "3": "king cobra"
}

'''''
print(dic["Fede"][2])
'''

''''
for llave, valor in dic.items():
    print(llave, valor)
'''
''''
for value in dic.values():
    print(value)
    for i in value:
        print(i)
'''
dic = {
    "Fede": {
        "informatica": [12.12, 13.13, 14.14],
        "deporte": [13.13, 12.24, 77.65, 146.9],
        "matematicas": [18.95, 27.47, 2745.85, 86.09],
    },
    "lucho": {
        "informatica": [12.12, 13.13, 14.14],
        "deporte": [13.13, 12.24, 77.65, 146.9],
        "matematicas": [18.95, 27.47, 2745.85, 86.09],
    },
    "juan": {
        "informatica": [12.12, 13.13, 14.14],
        "deporte": [13.13, 12.24, 77.65, 146.9],
        "matematicas": [18.95, 27.47, 2745.85, 86.09],
    },
}
for llave, valor in dic. items():
    for i, j in valor.items():
        for nota in j:
            print(llave, i, nota)
