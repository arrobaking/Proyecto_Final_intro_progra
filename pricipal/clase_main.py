#Código Ejercicio de Streaming con POO.
#Primer Cuatrimestre 2024, Introducción a la Programación.
#Alumno: Antonio Reyes

#Archivo con la clase pricipal que controla el menú que interactúa con el usuario.

import csv

from clases_productos import Pelicula#, Animacion, Serie

class Main:
  def __init__(self, archivo_peliculas, archivo_videos, archivo_canciones):
    self.archivo_peliculas  = archivo_peliculas
    self.archivo_videos     = archivo_videos
    self.archivo_canciones  = archivo_canciones
    self.operacion          = 4
    self.tipo               = 4
    self.PINdiario          = 1234
    self.pelicula           = Pelicula("", "", "", "", "", "", "")
    #self.animacion          = Animacion("", "", "", "", "")
    #self.serie              = Serie("", "", "", "", "", "")

  def iniciar(self):
    print("\nBienvenido al catálogo de producciones audiovisuales de Melange Contents.")
    self.PINdiario = int(input("Establezca un PIN para salir del programa, al finalizar: "))
      
  def operar(self):
    while (self.operacion != 0):
      print("\nSeleccione la operación que desea realizar:\n 0) Salir (ingresando el PIN)\n 1) Agregar un nuevo producto\n 2) Mostrar lista contenido\n 3) Acerca de la plataforma")
      self.operacion = int(input("Operacion: "))

      if (self.operacion == 0):
        print("Ha decidido cerrar el programa.")
        PIN = int(input("Escriba el PIN: "))
        if PIN==self.PINdiario:
          break
        else:
          print("PIN incorrecto. Regresando al inicio.")
          self.operacion = 3

      elif (self.operacion == 1):
        pass

      elif (self.operacion == 2):
        print("\nEscriba el tipo de contenido para ver la info:\n 1) Película\n 2) Animación\n 3) Serie")
        self.tipo = int(input("Tipo: "))

        if self.tipo == 1:
          self.info_peliculas = open(self.archivo_peliculas, mode="r+")
          self.reader_peliculas  = csv.reader(self.info_peliculas,delimiter=",")
          print('Detalles de la película:')
          self.pelicula = Pelicula(*(self.reader_peliculas[1]))
          self.pelicula.mostrar_detalles()
          self.info_peliculas.close()

        elif self.tipo == 2:
          pass

        elif self.tipo == 3:
          pass
                
      elif (self.operacion == 3):
        print(f"\nMelange Contents es una plataforma creada por Antonio Reyes en abril de 2024 usando lenguaje Python")
      
      else:
        print("Opción incorrecta. Regresando al inicio.\n")
        
  def terminar(self):
    print("\nPrograma cerrado. Hasta luego.\n")