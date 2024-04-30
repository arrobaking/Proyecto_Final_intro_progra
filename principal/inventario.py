#Proyecto Final: Recomendar qué ver en plataformas de streaming.
#Primer cuatrimestre 2024, Introducción a la Programación.
#Alumno: Antonio Reyes.

#Archivo con la clase Inventario, que maneja la búsqueda de recomendaciones a través de los archivos csv con la información de los productos.

import csv

from resultado import Resultado

class Inventario():
  
  def __init__(self, archivo_peliculas, archivo_animaciones, archivo_series):
    self.archivo_peliculas    = archivo_peliculas
    self.archivo_animaciones  = archivo_animaciones
    self.archivo_series       = archivo_series

  def buscar(self, criterios):
    self.criterios = criterios
    if self.criterios[0]    == 1: #formato es película
      self.resultado = Resultado(self.buscar_peliculas(), 1)
    elif self.criterios[0]  == 2: #formato es animación
      self.resultado = Resultado(self.buscar_animaciones(), 2)
    elif self.criterios[0]  == 3: #formato es serie
      self.resultado = Resultado(self.buscar_series(), 3)
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
        if (fila[7] == self.criterios[3] or fila[8] == self.criterios[3]): #actor1 o actor2
          self.writer_previo_2.writerow(fila)
    elif int(self.criterios[2]) == 2: #tipo de artista es director
      for fila in self.reader_previo_1:
        if (fila[6] == self.criterios[3]): #director
          self.writer_previo_2.writerow(fila)
    elif int(self.criterios[2]) == 3: #no se va a realizar búsqueda por artista
      for fila in self.reader_previo_1:
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
      if int(fila[4]) >= self.max_calificacion:
        self.max_calificacion = int(fila[4])
        self.ID_max_calificacion_1 = fila[0] #primera recomendación
    self.previo_2.seek(0)
    self.max_calificacion = 0
    for fila in self.reader_previo_2:
      if fila[0] != self.ID_max_calificacion_1:
        if int(fila[4]) >= self.max_calificacion:
          self.max_calificacion = int(fila[4])
          self.ID_max_calificacion_2 = fila[0] #segunda recomendación
    self.previo_2.seek(0)
    self.max_calificacion = 0
    for fila in self.reader_previo_2:
      if (fila[0] != self.ID_max_calificacion_1) and (fila[0] != self.ID_max_calificacion_2):
        if int(fila[4]) >= self.max_calificacion:
          self.max_calificacion = int(fila[4])
          self.ID_max_calificacion_3 = fila[0] #tercera recomendación
    self.previo_2.seek(0)
    for fila in self.reader_previo_2:
      if (fila[0] == self.ID_max_calificacion_1) or (fila[0] == self.ID_max_calificacion_2) or (fila[0] == self.ID_max_calificacion_3):
        self.recomendaciones.append(fila)        
    self.previo_2.close()
    
    return self.recomendaciones
  
  def buscar_animaciones(self):
    self.recomendaciones = []
    self.info_animaciones = open(self.archivo_animaciones, mode="r+")
    self.reader_animaciones  = csv.reader(self.info_animaciones,delimiter=",")
    self.previo_1 = open("previo_1.csv", mode="w+", newline="")
    self.writer_previo_1 = csv.writer(self.previo_1,delimiter=",")
    for fila in self.reader_animaciones:
      if int(fila[3]) == self.criterios[1]: #género
        self.writer_previo_1.writerow(fila)
    self.info_animaciones.close()
    self.previo_1.close()

    self.previo_1 = open("previo_1.csv", mode="r+")
    self.reader_previo_1  = csv.reader(self.previo_1,delimiter=",")
    self.previo_2 = open("previo_2.csv", mode="w+", newline="")
    self.writer_previo_2 = csv.writer(self.previo_2,delimiter=",")
    if int(self.criterios[2]) == 1: #tipo de artista es studio de animación
      for fila in self.reader_previo_1:
        if fila[6] == self.criterios[3]:
          self.writer_previo_2.writerow(fila)
    elif int(self.criterios[2]) == 3: #no se va a realizar búsqueda por artista
      for fila in self.reader_previo_1:
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
      if int(fila[4]) >= self.max_calificacion:
        self.max_calificacion = int(fila[4])
        self.ID_max_calificacion_1 = fila[0] #primera recomendación
    self.previo_2.seek(0)
    self.max_calificacion = 0
    for fila in self.reader_previo_2:
      if fila[0] != self.ID_max_calificacion_1:
        if int(fila[4]) >= self.max_calificacion:
          self.max_calificacion = int(fila[4])
          self.ID_max_calificacion_2 = fila[0] #segunda recomendación
    self.previo_2.seek(0)
    self.max_calificacion = 0
    for fila in self.reader_previo_2:
      if (fila[0] != self.ID_max_calificacion_1) and (fila[0] != self.ID_max_calificacion_2):
        if int(fila[4]) >= self.max_calificacion:
          self.max_calificacion = int(fila[4])
          self.ID_max_calificacion_3 = fila[0] #tercera recomendación
    self.previo_2.seek(0)
    for fila in self.reader_previo_2:
      if (fila[0] == self.ID_max_calificacion_1) or (fila[0] == self.ID_max_calificacion_2) or (fila[0] == self.ID_max_calificacion_3):
        self.recomendaciones.append(fila)
    self.previo_2.close()
    
    return self.recomendaciones
  
  def buscar_series(self):
    self.recomendaciones = []
    self.info_series = open(self.archivo_series, mode="r+")
    self.reader_series  = csv.reader(self.info_series,delimiter=",")
    self.previo_1 = open("previo_1.csv", mode="w+", newline="")
    self.writer_previo_1 = csv.writer(self.previo_1,delimiter=",")
    for fila in self.reader_series:
      if int(fila[3]) == self.criterios[1]: #género
        self.writer_previo_1.writerow(fila)
    self.info_series.close()
    self.previo_1.close()

    self.previo_1 = open("previo_1.csv", mode="r+")
    self.reader_previo_1  = csv.reader(self.previo_1,delimiter=",")
    self.previo_2 = open("previo_2.csv", mode="w+", newline="")
    self.writer_previo_2 = csv.writer(self.previo_2,delimiter=",")
    if int(self.criterios[2]) == 1: #tipo de artista es actor
      for fila in self.reader_previo_1:
        if (fila[6] == self.criterios[3] or fila[7] == self.criterios[3]): #actor1 o actor2
          self.writer_previo_2.writerow(fila)
    elif int(self.criterios[2]) == 3: #no se va a realizar búsqueda por artista
      for fila in self.reader_previo_1:
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
      if int(fila[4]) >= self.max_calificacion:
        self.max_calificacion = int(fila[4])
        self.ID_max_calificacion_1 = fila[0] #primera recomendación
    self.previo_2.seek(0)
    self.max_calificacion = 0
    for fila in self.reader_previo_2:
      if fila[0] != self.ID_max_calificacion_1:
        if int(fila[4]) >= self.max_calificacion:
          self.max_calificacion = int(fila[4])
          self.ID_max_calificacion_2 = fila[0] #segunda recomendación
    self.previo_2.seek(0)
    self.max_calificacion = 0
    for fila in self.reader_previo_2:
      if (fila[0] != self.ID_max_calificacion_1) and (fila[0] != self.ID_max_calificacion_2):
        if int(fila[4]) >= self.max_calificacion:
          self.max_calificacion = int(fila[4])
          self.ID_max_calificacion_3 = fila[0] #tercera recomendación
    self.previo_2.seek(0)
    for fila in self.reader_previo_2:
      if (fila[0] == self.ID_max_calificacion_1) or (fila[0] == self.ID_max_calificacion_2) or (fila[0] == self.ID_max_calificacion_3):
        self.recomendaciones.append(fila)
    self.previo_2.close()
    
    return self.recomendaciones