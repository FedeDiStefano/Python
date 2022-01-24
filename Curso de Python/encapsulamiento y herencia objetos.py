class celular: 
    marca = ""
    color = ""
    modelo = ""
    __prendido = False 
    


    def __init__(self, marca, color, modelo):
        self. marca = marca
        self. color = color
        self. modelo = modelo

    def prender (self):
        self.__prendido = True 
    
    def get_prendido(self):
        return self.__prendido



class CelularBueno(celular):
    GB = 60


    def __init__(self, marca, color, modelo, GB):
        self. marca = marca
        self. color = color
        self. modelo = modelo
        self. GB =  GB 


celular1 = celular("samsung","blanco", "galaxy J9")
#celular1.prender()
#celular1.__encendido = True

print(f'marca: {celular1.marca}, color: {celular1.color}, modelo: {celular1.modelo}')
print(f'prendido: {celular1.get_prendido()}')


celular_alta_gama = CelularBueno("samsung", "negro", "galaxy s21 ultra", 512)
print(f'marca: {celular_alta_gama.marca}, color: {celular_alta_gama.color}, modelo: {celular_alta_gama.modelo}, GB: {celular_alta_gama.GB}')






