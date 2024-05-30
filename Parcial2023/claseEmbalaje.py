from claseServicio import Servicio

class Embalaje(Servicio):
    __precio_u: float
    __horas: int
    __peso_c: float
    __cant_u: int
    __costoo: float
    
    def __init__(self, nomE, nomC, dire, fecha, comi,precio,hora,peso,cant):
        super().__init__(nomE, nomC, dire, fecha, comi)
        self.__precio_u= float(precio)
        self.__horas= int(hora)
        self.__peso_c= float(peso)
        self.__cant_u= int(cant)
        self.__costoo= float(self.__precio_u * self.__cant_u) + super().getComi()
        
    def getPrecio(self):
        return self.__precio_u
    
    def getHori(self):
        return self.__horas
    
    def getPeso(self):
        return self.__peso_c
    
    def getDire_D(self):
        return self.__cant_u
    
    def getCostoo(self):
        if self.__peso_c > 50:
            return self.__costoo + ((self.__costoo * 10)/ 100)
        else:
            return self.__costoo
    
    def __str__(self):
        return super().__str__() + f"\nPrecio por unidad: {self.__precio_u}\nHora: {self.__horas}\nPeso de la unidad: {self.__peso_c}\nCantidad de unidades: {self.__cant_u}\n"