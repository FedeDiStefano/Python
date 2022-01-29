class celular: 
    marca = ""
    color = ""
    modelo = ""
    prendido = False 
    volumen = 0


    def __init__(self, marca, color, modelo):
        self. marca = marca
        self. color = color
        self. modelo = modelo

    def prender (self):
        self.prendido = True 

    def set_volumen(self, volumen):
        self.volumen = volumen 


celular1 = celular("samsung","negro", "galaxy s21 ultra")
celular1.color = "blanco"
celular1.prender ()
celular1.set_volumen(10) 
print(f'marca: {celular1.marca}, color: {celular1.color}, modelo: {celular1.modelo}')

if celular1.prendido:
                    print(f'el celular esta prendido y su volumen es {celular1.volumen}')
                    celular1.set_volumen(8) 
                    print(f'el celular esta prendido y su volumen es {celular1.volumen}')
else:
    print ('el celular esta apagado')

