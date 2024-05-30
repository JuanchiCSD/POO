from claseServicio import Servicio

class Trans(Servicio):
    __precio: float
    __hora: int
    __peso: float
    __direccion_d: str
    
    def __init__(self, nomE, nomC, dire, fecha, comi,precio,hora,peso,di):
        super().__init__(nomE, nomC, dire, fecha, comi)
        self.__precio= precio
        self.__hora= hora
        self.__peso= peso
        self.__direccion_d= di
        self.__costo= (self.__precio * self.__hora) + super().getComi()
        
    def getPrecio(self):
        return self.__precio
    
    def getHora(self):
        return self.__hora
    
    def getPeso(self):
        return self.__peso
    
    def getDire_D(self):
        return self.__direccion_d
    
    def getCosto(self):
        if self.__peso > 500:
            return self.__costo + ((self.__costo * 10) /100)
        else:
            return self.__costo
    
    
    def __str__(self):
        return super().__str__() + f"\nPrecio por hora: {self.__precio}\nHora: {self.__hora}\nPeso: {self.__peso}\nDireccion de entrega: {self.__direccion_d}\n"