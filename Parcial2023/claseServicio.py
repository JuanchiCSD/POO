class Servicio:
    __nombre_E: str
    __nombre_C: str
    __direccion: str
    __fecha: str
    __comision: float
    
    def __init__(self,nomE,nomC,dire,fecha,comi):
        self.__nombre_E= nomE
        self.__nombre_C= nomC
        self.__direccion= dire
        self.__fecha= fecha
        self.__comision= float(comi)
    
    def getNomE(self):
        return self.__nombre_E
    
    def getNomC(self):
        return self.__nombre_C
    
    def getDire(self):
        return self.__direccion
    
    def getFecha(self):
        return self.__fecha
    
    def getComi(self):
        return self.__comision
    
    def __str__(self):
        return f"\nNombre Empresa: {self.__nombre_E}\nNombre Contratante: {self.__nombre_C}\nDireccion: {self.__direccion}\nFecha: {self.__fecha}\nComision: {self.__comision}"