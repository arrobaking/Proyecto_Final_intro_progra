from productos import Pelicula

class Resultado():
  def __init__(self, recomendaciones, formato):
    self.recomendaciones = recomendaciones
    self.cantidad_propuestas = len(recomendaciones)
    self.formato = formato
    
  def mostrar_resultado(self):
    
    if self.cantidad_propuestas == 0:
      print("No se encontraron propuestas que concuerden con sus criterios. :-(")
    else:
      if self.formato == 1:
        self.mostrar_res_pelicula()
      elif self.formato == 2:
        self.mostrar_res_animacion()
      elif self.formato == 3:
        self.mostrar_res_serie()

  def mostrar_res_pelicula(self):
    print("\nBasado en sus criterios, las recomendaciones de películas serían:")
    for numero in range(self.cantidad_propuestas):
      self.pelicula = Pelicula(self.recomendaciones[numero][0],
                               self.recomendaciones[numero][1],
                               self.recomendaciones[numero][2],
                               self.recomendaciones[numero][3],
                               self.recomendaciones[numero][4],
                               self.recomendaciones[numero][5],
                               self.recomendaciones[numero][6],
                               self.recomendaciones[numero][7],
                               self.recomendaciones[numero][8],
                               self.recomendaciones[numero][9])
      print(f"---------- Propuesta número {numero+1} ----------")
      self.pelicula.mostrar_detalles()
      print("")

  def mostrar_res_animacion(self):
    print("\nBasado en sus criterios, las recomendaciones de películas serían:")
    for numero in range(self.cantidad_propuestas):
      self.pelicula = Pelicula(self.recomendaciones[numero][0],
                               self.recomendaciones[numero][1],
                               self.recomendaciones[numero][2],
                               self.recomendaciones[numero][3],
                               self.recomendaciones[numero][4],
                               self.recomendaciones[numero][5],
                               self.recomendaciones[numero][6],
                               self.recomendaciones[numero][7],
                               self.recomendaciones[numero][8],
                               self.recomendaciones[numero][9])
      print(f"---------- Propuesta número {numero+1} ----------")
      self.pelicula.mostrar_detalles()
      print("")

  def mostrar_res_serie(self):
    print("\nBasado en sus criterios, las recomendaciones de películas serían:")
    for numero in range(self.cantidad_propuestas):
      self.pelicula = Pelicula(self.recomendaciones[numero][0],
                               self.recomendaciones[numero][1],
                               self.recomendaciones[numero][2],
                               self.recomendaciones[numero][3],
                               self.recomendaciones[numero][4],
                               self.recomendaciones[numero][5],
                               self.recomendaciones[numero][6],
                               self.recomendaciones[numero][7],
                               self.recomendaciones[numero][8],
                               self.recomendaciones[numero][9])
      print(f"---------- Propuesta número {numero+1} ----------")
      self.pelicula.mostrar_detalles()
      print("")