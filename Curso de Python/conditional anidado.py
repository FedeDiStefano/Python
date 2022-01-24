edad = int(input("introduce tu edad: "))
mes = int(input("introduce el numero de tu mes de nacimiento: "))


if edad >=18: 
    print("sos mayor de edad")
    if mes == 1:
        print("naciste en ENERO")
    elif mes == 2: 
        print("naciste en FEBRERO")
else: 
    print("sos menor de edad")
    if(mes == 3): 
        print("naciste en MARZO")



