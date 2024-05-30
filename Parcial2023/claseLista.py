from claseNodo import Nodo
from claseTransporte import Trans
from claseEmbalaje import Embalaje

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    def __init__(self):
        self.__comienzo= None
        self.__actual= None
        self.__tope = 0# hace referencia a la cantidad de elementos en la lista, como su nombre lo dice es un tope a la hora de iterar
        self.__indice = 0 #hace referencia a la posicion en la lista

    def __iter__(self):
        self.__actual = self.__comienzo
        self.__indice = 0
        return self
    
    def __next__(self):
        if self.__actual is None or self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            dato = self.__actual.getServi()
            self.__actual = self.__actual.getSig()
            self.__indice += 1
            return dato
    
    def mostrar(self):
        print("-"*30)
        print("Elementos de la lista:")
        for servi in self:
            print(servi)
    
    
    def agregar(self,servicio):
        nodo = Nodo(servicio)
        if self.__comienzo is None:
            self.__comienzo = nodo
        else:
            aux = self.__comienzo
            while aux.getSig() is not None:
                aux = aux.getSig()
            aux.setSig(nodo)
        self.__tope += 1
        
    def mostrarT(self):
        total= 0.0
        for servi in self:
            if isinstance(servi, Trans):
                print("\nSERVICIOS DE TRANSPORTE REALIZADOS\n")
                print("Contratante         Costo Total\n")
                print(f"{servi.getNomC():<25}{servi.getCosto()}")
                total+= servi.getCosto()
                
            else:
                print("-"*30)
        print(f"{total:>20}\n")
    
    
    def mostrarE(self):
        cont= 0
        for servi in self:
            if isinstance(servi, Embalaje):
                if servi.getPeso() > 50:
                    cont+= 1
                else:
                    continue   
            else:
                continue
        print(f"La cantidad de Servicios de Embalaje con peso mayor a 50kg es: {cont}")
        

    def fecha(self, fecha):
        cont1 = 0  # Contador para Embalaje
        cont2 = 0  # Contador para Transporte

        for servi in self:
            if servi.getFecha() == fecha:
                if isinstance(servi, Embalaje):
                    cont1 += 1
                elif isinstance(servi, Trans):
                    cont2 += 1

        if cont1 == 0 and cont2 == 0:
            print(f"No hay ninguna contratación para la fecha: {fecha}\n")
        else:
            if cont1 > cont2:
                print(f"El servicio con más contrataciones para la fecha {fecha} es de tipo Embalaje\n")
            elif cont2 > cont1:
                print(f"El servicio con más contrataciones para la fecha {fecha} es de tipo Transporte\n")
            else:
                print(f"Ambos servicios tienen la misma cantidad de contrataciones para la fecha {fecha}\n")

