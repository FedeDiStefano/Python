a = "hola mundo"
for i in a:
    print(i)

listas = ["hola", 12, 12, 12]
print("\n\n ", len(listas))
for i in range(13):
    print(i)


for i in range(len(listas)):
    print("el valor de las listas es {} en la posicion {}".format(
        listas[i], i))
print("\n\n\n")
for val in listas:
    print(val)
