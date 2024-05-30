from claseLista import Lista
from GestorEmbalaje import gestorEmba
from GestorTrans import gestorTrans

def agregarS(lista,tipo):
    if tipo == 'Trans':
        trans = gestorTrans()
        servicio=trans.cargarTrans()
        lista.agregar(servicio)
    elif tipo == 'Embalaje':
        emba = gestorEmba()
        servicio2= emba.cargarEmbalaje()
        lista.agregar(servicio2)
    else:
        print("Tipo de Servicio Inexistente\n")    
        

if __name__ == '__main__':
    lista = Lista()
	
    op = int(input("""Ingrese opcion: 
					1_Insertar dato
					2_Mostrar Servicios de Transporte
					3_Mostrar cantidad de servicios de embalaje
					4_Ingresar una fecha y mostrar el servicio con mas contrataciones para la misma
					0_Para finalizar
					"""))
      
    while op != 0:
        if op == 1:
            tipo= input("\nIngrese tipo de servicio para agregar: Transporte o Embalaje: ")
            agregarS(lista,tipo)
            lista.mostrar()
        elif op == 2:
            lista.mostrarT()
        elif op == 3:
            lista.mostrarE()
        elif op == 4:
            fecha= str(input("\nIngrese una fecha: "))
            lista.fecha(fecha)
        else:
            print("\nError: Numero Incorrecto\n")
        op = int(input("""Ingrese opcion: 
					1_Insertar dato
					2_Mostrar Servicios de Transporte
					3_Mostrar cantidad de servicios de embalaje
					4_Ingresar una fecha y mostrar el servicio con mas contrataciones para la misma
					0_Para finalizar
					"""))
        

"""
1
Trans
Lucas
Buloz
casa arquerito
12m
7777
10
5
501
casa gordo
1
Trans
Boca
Ribera
laboca
12m
1000
10
5
200
nunez
1
Embalaje
Martino
Ortega
casa tute
20m
2333
10
5
200
5
1
Embalaje
Manuel
Ortega
facu
12m
1000
10
5
60
5
"""