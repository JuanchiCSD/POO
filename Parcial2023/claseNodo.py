from claseServicio import Servicio

class Nodo:
    __Servicio: Servicio # un atributo del tipo calefactores
    __siguiente: object
    def __init__(self, servicio):
        self.__Servicio= servicio
        self.__siguiente= None
        
    def getServi(self): #devuelve el objeto
        return self.__Servicio
    
    def getSig(self):
        return self.__siguiente
        
    def setSig(self, siguiente):
        self.__siguiente= siguiente
  