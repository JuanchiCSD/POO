from ClaseInmueble import Inmueble

class Nodo:
    __Inmueble: Inmueble # un atributo del tipo calefactores
    __siguiente: object
    def __init__(self, inmueble):
        self.__Inmueble= inmueble
        self.__siguiente= None
    
    def getSig(self):
        return self.__siguiente
        
    def setSig(self, siguiente):
        self.__siguiente= siguiente
  
    def getInmueble(self): #devuelve el objeto
        return self.__Inmueble