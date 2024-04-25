from productos import Pelicula

class Resultado():
  def __init__(self, recomendaciones):
    self.recomendaciones = recomendaciones
    self.cantidad = len(recomendaciones)
    for numero self.cantidad:
    self.pelicula = Pelicula(self.recomendaciones[0][0],
                             self.recomendaciones[0][1],
                             self.recomendaciones[0][2],
                             self.recomendaciones[0][3],
                             self.recomendaciones[0][4],
                             self.recomendaciones[0][5],
                             self.recomendaciones[0][6],
                             self.recomendaciones[0][7],
                             self.recomendaciones[0][8],
                             self.recomendaciones[0][9])  

  def mostrar_resultado(self, pelicula):
    self.pelicula.mostrar_detalles()