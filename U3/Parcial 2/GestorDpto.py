from ClaseDepto import Dpto
class gestorDepto:
  def crearDepto(self):
    print("\nCREANDO DEPTO...\n")
    depto = Dpto(str(input("Localidad: ")),str(input("Direccion: ")),float(input("Superficie: ")),int(input("Cantidad Dormitorios: ")),int(input("Numero Monoblock:")),int(input("Numero de Depto:")),int(input("Numero de Piso:")))
    print("\nDEPTO CARGADO\n")
    return depto