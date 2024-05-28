from ClaseInmueble import Inmueble

class Casa(Inmueble):
    __metros: int

    def __init__(self, loc, dire, sup,metros):
        super().__init__(loc, dire, sup)
        self.__metros= int(metros)
    
    def impoVenta(self):
        importe= 0.0
        precio= 0.0
        precio= self.__metros * 1.80 * 20000
        importe= super().getSup() * 15 * precio
        return importe

        
    def getMetros(self):
        return self.__metros
    
    def __str__(self):
        return super().__str__() + f"\nMetros: {self.__metros}\n"