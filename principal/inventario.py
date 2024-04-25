

import csv

from productos import Pelicula #, Animacion, Serie

class Inventario():
  
  def __init__(self, archivo_peliculas, archivo_videos, archivo_canciones):
    self.archivo_peliculas  = archivo_peliculas
    self.archivo_videos     = archivo_videos
    self.archivo_canciones  = archivo_canciones
        
    self.pelicula           = Pelicula("a", "b", "c", "1", "d", "1", "e", "f", "g", "h")
    #self.animacion          = Animacion("", "", "", "", "")
    #self.serie              = Serie("", "", "", "", "", "")

  def buscar(self, solicitud):
