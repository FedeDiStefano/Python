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