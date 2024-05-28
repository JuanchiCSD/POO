from ClaseCasa import Casa
class gestorCasa:
  def crearCasa(self):
    print("\nCREANDO CASA...\n")
    casa = Casa(str(input("Localidad: ")),str(input("Direccion: ")),float(input("Superficie: ")),int(input("Metros: ")))
    print("\nCASA CARGADA\n")
    return casa