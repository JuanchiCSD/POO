from claseLista import Lista
from GestorCasa import gestorCasa
from GestorDpto import gestorDepto



def InsertarInmu(lista,inmueble):
    if inmu == "Casa":
        casa = gestorCasa()
        lista.insertar(casa.crearCasa())
    elif inmu == ("Depto"):
        depto = gestorDepto()
        lista.insertar(depto.crearDepto())
    else:
        print("inmueble no existente\n")
    return


if __name__ == '__main__':
	lista = Lista()
	GD= gestorDepto()
	op = int(input("""Ingrese opcion: 
					1_Insertar dato
					2_
					3_
					4_
					5_
					6_
					7
					0_Para finalizar
					"""))
      
	while op != 0:
		if op == 1:
			inmu= input("Ingrese tipo de Inmueble: Casa o Depto: ")
			InsertarInmu(lista,inmu)		
		elif op == 2:
			lista.agregarInmu()
			for inmu in lista:
				print(inmu)
		elif op == 3:
			cantidad= int(input("\nIngrese cantidad de dormitorios: "))
			lista.mostrarDpto(lista,cantidad)
		elif op == 4:
			lista.mostrarCasa(lista)
		elif op == 5:
			pass
		else:
			print("\nNUmero Incorrecto\n")
		op = int(input("""Ingrese opcion: 
					1_Insertar dato
					2_
					3_
					4_
					5_
					6_
					7
					0_Para finalizar
					"""))
           
            
"""
1
Casa
Rivadavia
San Lorenzo
20
15
1
Depto
Capital
Mitre
20
5
10
5
3
2
Casa
2
Depto
3
3
4
"""
