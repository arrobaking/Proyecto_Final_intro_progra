from productos import Pelicula

class Resultado():
  def __init__(self, recomendaciones):
    self.recomendaciones = recomendaciones
    self.cantidad_propuestas = len(recomendaciones)
    
  def mostrar_resultado(self):
    
    if self.cantidad_propuestas == 0:
      print("No se encontraron propuestas que concuerden con sus criterios. :-(")
    else:
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
