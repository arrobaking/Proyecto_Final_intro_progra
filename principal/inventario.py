

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

  def buscar(self, criterios):
    self.criterios = criterios
    self.info_peliculas = open(self.archivo_peliculas, mode="r+")
    self.reader_peliculas  = csv.reader(self.info_peliculas,delimiter=",")
    print('\nDetalles de la película:')
    myList = list(self.reader_peliculas)
    self.pelicula = Pelicula(*(myList[1]))
    self.pelicula.mostrar_detalles()
    self.info_peliculas.close()
    return resultados