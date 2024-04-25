

import csv

from resultado import Resultado

class Inventario():
  
  def __init__(self, archivo_peliculas, archivo_animaciones, archivo_series):
    self.archivo_peliculas    = archivo_peliculas
    self.archivo_animaciones  = archivo_animaciones
    self.archivo_series       = archivo_series

    #self.animacion   = Animacion("", "", "", "", "")
    #self.serie   = Serie("", "", "", "", "", "")
    #self.criterios = [formato, self.genero, self.tipo_artista, self.artista]
    #ID,Titulo,Anyo,Genero,Calificacion,Plataformas,Director,Actor1,Actor2,Duracion

  def buscar(self, criterios):
    self.criterios = criterios
    if self.criterios[0] == 1: #formato es película
      self.resultado = Resultado(self.buscar_peliculas())
    elif self.criterios[0] == 2: #formato es animación
      self.buscar_animacion()
    elif self.criterios[0] == 3: #formato es serie
      self.buscar_serie()
    return self.resultado
    
  def buscar_peliculas(self):
    self.recomendaciones = []
    self.info_peliculas = open(self.archivo_peliculas, mode="r+")
    self.reader_peliculas  = csv.reader(self.info_peliculas,delimiter=",")
    self.previo_1 = open("previo_1.csv", mode="w+", newline="")
    self.writer_previo_1 = csv.writer(self.previo_1,delimiter=",")
    for fila in self.reader_peliculas:
      if int(fila[3]) == self.criterios[1]: #género
        self.writer_previo_1.writerow(fila)
    self.info_peliculas.close()
    self.previo_1.close()

    self.previo_1 = open("previo_1.csv", mode="r+")
    self.reader_previo_1  = csv.reader(self.previo_1,delimiter=",")
    self.previo_2 = open("previo_2.csv", mode="w+", newline="")
    self.writer_previo_2 = csv.writer(self.previo_2,delimiter=",")
    if int(self.criterios[2]) == 1: #tipo de artista es actor
      for fila in self.reader_previo_1:
        print("prueba 2")
        if (fila[7] == self.criterios[3] or fila[8] == self.criterios[3]): #actor1 o actor2
          self.writer_previo_2.writerow(fila)
    elif int(self.criterios[2]) == 2: #tipo de artista es director
      print("prueba 3")
      for fila in self.reader_previo_1:
        if (fila[6] == self.criterios[3]): #director
          self.writer_previo_2.writerow(fila)
    self.previo_1.close()
    self.previo_2.close()

    self.previo_2 = open("previo_2.csv", mode="r+")
    self.reader_previo_2  = csv.reader(self.previo_2,delimiter=",")
    self.ID_max_calificacion_1 = ""
    self.ID_max_calificacion_2 = ""
    self.ID_max_calificacion_3 = ""
    self.max_calificacion = 0
    for fila in self.reader_previo_2:
      print("prueba 4")
      if int(fila[4]) >= self.max_calificacion:
        self.max_calificacion = int(fila[4])
        self.ID_max_calificacion_1 = fila[0] #primera recomendación
        print(f"self.ID_max_calificacion_1: {self.ID_max_calificacion_1}")
    self.previo_2.seek(0)
    self.max_calificacion = 0
    for fila in self.reader_previo_2:
      print("prueba 5")
      if fila[0] != self.ID_max_calificacion_1:
        if int(fila[4]) >= self.max_calificacion:
          self.max_calificacion = int(fila[4])
          self.ID_max_calificacion_2 = fila[0] #segunda recomendación
          print(f"self.ID_max_calificacion_2 {self.ID_max_calificacion_}")
    self.previo_2.seek(0)
    self.max_calificacion = 0
    for fila in self.reader_previo_2:
      print("prueba 6")
      if (fila[0] != self.ID_max_calificacion_1) and (fila[0] != self.ID_max_calificacion_2):
        if int(fila[4]) >= self.max_calificacion:
          self.max_calificacion = int(fila[4])
          self.ID_max_calificacion_3 = fila[0] #tercera recomendación
          print(f"self.ID_max_calificacion_3 {self.ID_max_calificacion_3}")
    self.previo_2.seek(0)
    for fila in self.reader_previo_2:
      print("prueba 7")
      if (fila[0] == self.ID_max_calificacion_1) or (fila[0] == self.ID_max_calificacion_2) or (fila[0] == self.ID_max_calificacion_3):
        self.recomendaciones.append(fila)
        self.recomendaciones.append(fila)
        print(f"recomendaciones {self.recomendaciones}")
    self.previo_2.close()
    
    return self.recomendaciones


"""print('\nDetalles de la película:')
    myList = list(self.reader_peliculas)
    self.pelicula = Pelicula(*(myList[1]))
    self.pelicula.mostrar_detalles()"""