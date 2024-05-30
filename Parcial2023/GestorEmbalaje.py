from claseEmbalaje import Embalaje

class gestorEmba():
    def cargarEmbalaje(lista):
        print("\nCREANDO SERVICIO DE EMBALAJE...\n")
        emba = Embalaje(str(input("Nombre Empresa: ")),str(input("Nombre Contratante: ")),str(input("Direccion: ")),str(input("Fecha: ")),float(input("Comision: ")),float(input("Precio por unidad:")),int(input("Horas: ")),float(input("Peso por unidad: ")),int(input("Cantidad de unidades: ")))
        print("\nSERVICIO DE EMBALAJE CARGADO\n")
        return emba