from claseNodo import Nodo
from ClaseDepto import Dpto
from ClaseCasa import Casa

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__tope = 0# hace referencia a la cantidad de elementos en la lista, como su nombre lo dice es un tope a la hora de iterar
        self.__indice = 0 #hace referencia a la posicion en la lista

    def __iter__(self):
        return self #retorna el iterador de un objeto, es decir el actual
    
    def __next__(self):
        if self.__indice==self.__tope: #si el indice es igual al tope, entonces se detiene la iteracion
            self.__actual=self.__comienzo 
            self.__indice=0 
            raise StopIteration # raise fuerza el lanzamiento de esta excepcion
        else:  #si el indice es distinto al tope
            self.__indice+=1 #aumentamos el indice en 1 por cada iteracion
            dato = self.__actual.getInmueble() #dato va a tener el objeto de la posicion actual
            self.__actual=self.__actual.getSig() # a la posicion actual le asignamos el siguiente para seguir iterando
            return dato # retornamos nuestro objeto
        
    
    def insertar(self,inmueble):
        nodo = Nodo(inmueble) #se crea un nodo con la publicacion
        nodo.setSig(self.__comienzo) #al siguiente nodo se le asigna None
        self.__comienzo=nodo #se asigna el nodo como comienzo
        self.__actual=nodo #se asigna el nodo como actual
        self.__tope+=1 # se aumenta en 1 la cantidad de elementos en la lista

    
    def agregarInmu(self): #POR COLA
        tipo = input("Ingrese el tipo de inmueble a agregar (Casa o Depto): ")
        if tipo == 'Casa':
            inmueble = Casa("Rivadavia", "Guemes", 10, 10)
        elif tipo == 'Depto':
            inmueble = Dpto("Capital", "Mitre", 10, 2, 10, 5, 3)
        else:
            print("Tipo de inmueble no reconocido.")
            return
        
        nodo = Nodo(inmueble)
        if self.__comienzo is None:
            self.__comienzo = nodo
        else:
            aux = self.__comienzo
            while aux.getSig() is not None:
                aux = aux.getSig()
            aux.setSig(nodo)
        self.__tope += 1
    
    def mostrarDpto(self,lista,cant):
        for inmu in lista:
            if isinstance(inmu, Dpto) and inmu.getCantD() < cant:
                importe=inmu.importe()
                print(f"\nDatos del departamento con dormitorios menor a {cant}:\n{inmu}Importe de Venta: {importe}\n")
            elif isinstance(inmu, Dpto) and inmu.getCantD() >= cant:
                print("\nEl Dpto actual tiene igual o mas dormitorios \n")

    def mostrarCasa(self,lista):
        for inmu in lista:
            if isinstance(inmu, Casa):
                importe=inmu.impoVenta()
                print(f"Los datos de las Casas de la empresa en Venta son:\n{inmu}Importe de Venta: {importe}\n")

    
    
    
    # def agregar(self): ES PARA INSERTAR EN UNA POSICION INGRESADA
    #     dato= input("\nIngrese el Inmueble a insertar Casa o Depto: ")
    #     if dato == 'Casa':
    #         elementoC= Casa("Rivadavia", "Guemes", 30, 20)
    #         nodo= Nodo(elementoC)
    #     elif dato == 'Depto':
    #         elementoD= Dpto("Capital", "Mitre", 10, 2, 10, 5, 3)
    #         nodo= Nodo(elementoD)
        

    #     if self.__comienzo == None or pos == 1:
    #         nodo.setSig(self.__comienzo)
    #         self.__actual = nodo
    #         self.__comienzo = nodo

    #     elif 0 < pos <= self.__tope:
    #         aux = self.__actual
    #         for _ in range(pos-2):
    #             aux = aux.getSig()
    #         nodo.setSig(aux.getSig())
    #         aux.setSig(nodo)
        
    #     else:
    #         raise IndexError('La posicion indicada se encuentra fuera de rango.')
    #     self.__tope += 1