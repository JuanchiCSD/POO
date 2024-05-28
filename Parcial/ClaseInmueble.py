class Inmueble:
    __localidad: str
    __direccion: str
    __superficie: float

    def __init__(self,loc,dire,sup):
        self.__localidad= loc
        self.__direccion= dire
        self.__superficie= float(sup)
    
    def getLoc(self):
        return self.__localidad
    
    def getDire(self):
        return self.__direccion
    
    def getSup(self):
        return self.__superficie
    
    def __str__(self):
        return f"Localidad: {self.__localidad}\nDireccion: {self.__direccion}\nSuperficie: {self.__superficie}"