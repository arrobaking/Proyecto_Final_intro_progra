

import csv

from productos import Pelicula #, Animacion, Serie

class Inventario():
  
  def __init__(self, archivo_peliculas, archivo_animaciones, archivo_series):
    self.archivo_peliculas    = archivo_peliculas
    self.archivo_animaciones  = archivo_animaciones
    self.archivo_series       = archivo_series

    self.pelicula   = Pelicula("a", "b", "c", "1", "d", "1", "e", "f", "g", "h")
    #self.animacion   = Animacion("", "", "", "", "")
    #self.serie   = Serie("", "", "", "", "", "")
    #self.criterios = [formato, self.genero, self.tipo_artista, self.artista]
    #ID,Titulo,Anyo,Genero,Calificacion,Plataformas,Director,Actor1,Actor2,Duracion

  def buscar(self, criterios):
    self.criterios = criterios
    if self.criterios[0] == 1: #formato es película
      self.buscar_peliculas()
    elif self.criterios[0] == 2: #formato es animación
      self.buscar_animacion()
    elif self.criterios[0] == 3: #formato es serie
      self.buscar_serie()
    
    return resultados
  
  def buscar_peliculas(self):
    self.info_peliculas = open(self.archivo_peliculas, mode="r+")
    self.reader_peliculas  = csv.reader(self.info_peliculas,delimiter=",")
    self.previo_1 = open("previo_1.csv", mode="w+", newline="")
    self.writer_previo_1 = csv.writer(self.previo_1,delimiter=",")
    for fila in self.reader_peliculas:
      if fila[3] == self.criterios[1]: #género
        self.writer_previo_1.writerow(fila)
    self.info_peliculas.close()
    self.previo_1.close()

    self.previo_1 = open("previo_1.csv", mode="r+")
    self.reader_previo_1  = csv.reader(self.previo_1,delimiter=",")
    self.previo_2 = open("previo_2.csv", mode="w+", newline="")
    self.writer_previo_2 = csv.writer(self.previo_2,delimiter=",")
    if self.criterios[2] == 1: #tipo de artista es actor
      for fila in self.reader_previo_1:
        if (fila[7] == self.criterios[3] or fila[8] == self.criterios[3]): #actor1 o actor2
          self.writer_previo_2.writerow(fila)
    elif self.criterios[2] == 2: #tipo de artista es director
      for fila in self.reader_previo_1:
        if (fila[6] == self.criterios[3]): #director
          self.writer_previo_2.writerow(fila)
    self.previo_1.close()
    self.previo_2.close()

    self.previo_2 = open("previo_2.csv", mode="r+")
    self.reader_previo_2  = csv.reader(self.previo_2,delimiter=",")
    self.previo_3 = open("previo_3.csv", mode="w+", newline="")
    self.writer_previo_3 = csv.writer(self.previo_3,delimiter=",")
    self.previo_4 = open("previo_4.csv", mode="w+", newline="")
    self.writer_previo_4 = csv.writer(self.previo_4,delimiter=",")
    self.valor_mayor = 0
    self.fila_temporal = []
    for fila in self.reader_previo_2:
      if int(fila[4]) >= self.valor_mayor:
        self.valor_mayor = int(fila[4])
      else:
        for fila in self.reader_previo_3:

      self.writer_previo_3.writerow(fila)

    self.previo_2.close()
    

"""print('\nDetalles de la película:')
    myList = list(self.reader_peliculas)
    self.pelicula = Pelicula(*(myList[1]))
    self.pelicula.mostrar_detalles()"""