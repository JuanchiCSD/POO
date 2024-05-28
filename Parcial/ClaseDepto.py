from ClaseInmueble import Inmueble
class Dpto(Inmueble):
    __cantD: int
    __numeroM: int
    __numeroDpto: int
    __numeroP: int

    def __init__(self, loc, dire, sup,cantD,numM,numD,numP):
        super().__init__(loc, dire, sup)
        self.__cantD= int(cantD)
        self.__numeroM= int(numM)
        self.__numeroDpto= int(numD)
        self.__numeroP= int(numP)

    def importe(self):
        importe= 0.0
        precio= 0.0

        precio= self.__cantD * 17000
        importe= super().getSup() * 15 * precio
        return importe
    
    def getCantD(self):
        return self.__cantD
    
    def getNumM(self):
        return self.__numeroM
    
    def getnumD(self):
        return self.__numeroDpto
    
    def getNumP(self):
        return self.__numeroP
    

    def __str__(self):
        return super().__str__() + f"\nCantidad Dormitorios: {self.__cantD}\nNumero de Monoblock: {self.__numeroM}\nNumero Dpto: {self.__numeroDpto}\nNumero de Piso: {self.__numeroP}\n"
        