from claseTransporte import Trans

class gestorTrans():
    def cargarTrans(lista):
        print("\nCREANDO SERVICIO TRANSPORTE...\n")
        transpo = Trans(str(input("Nombre Empresa: ")),str(input("Nombre Contratante: ")),str(input("Direccion: ")),str(input("Fecha: ")),float(input("Comision: ")),float(input("Precio por hora: ")),int(input("Horas: ")),float(input("Peso de la carga: ")),str(input("Direccion de entrega: ")))
        print("\nSERVICIO TRANSPORTE CARGADO\n")
        return transpo