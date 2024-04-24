#Código Ejercicio de Streaming con POO.
#Primer Cuatrimestre 2024, Introducción a la Programación.
#Alumno: Antonio Reyes

#Archivo con la clase pricipal que controla el menú que interactúa con el usuario.

import csv

from clases_productos import Pelicula, Video, Cancion

class Main:
  def __init__(self, archivo_peliculas, archivo_videos, archivo_canciones):
    self.archivo_peliculas  = archivo_peliculas
    self.archivo_videos     = archivo_videos
    self.archivo_canciones  = archivo_canciones
    self.listaIDs_peliculas = []
    self.listaIDs_videos    = []
    self.listaIDs_canciones = []
    self.operacion          = 4
    self.tipo               = 4
    self.PINdiario          = 1234
    self.pelicula           = Pelicula("", "", "", "", "", "", "")
    self.video              = Video("", "", "", "", "")
    self.cancion            = Cancion("", "", "", "", "", "")

  def iniciar(self):
    print("\nBienvenido al catálogo de producciones audiovisuales de Melange Contents.")
    self.PINdiario = int(input("Establezca un PIN para salir del programa, al finalizar: "))

    self.info_peliculas   = open(self.archivo_peliculas, mode="r+")
    self.info_videos      = open(self.archivo_videos, mode="r+")
    self.info_canciones   = open(self.archivo_canciones, mode="r+")

    self.reader_peliculas  = csv.reader(self.info_peliculas,delimiter=",")
    self.reader_videos     = csv.reader(self.info_videos,delimiter=",")
    self.reader_canciones  = csv.reader(self.info_canciones,delimiter=",")

    for fila in self.reader_peliculas:
      self.listaIDs_peliculas.append(fila[0])
    for fila in self.reader_videos:
      self.listaIDs_videos.append(fila[0])
    for fila in self.reader_canciones:
      self.listaIDs_canciones.append(fila[0])

    self.info_peliculas.close()
    self.info_videos.close()
    self.info_canciones.close()
      
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
        print("\nEscriba el tipo de contenido a agregar:\n 1) Película\n 2) Video\n 3) Canción")
        self.tipo = int(input("Tipo: "))
        print("Escriba el número de ID del producto")
        ID = input("ID: ")

        if self.tipo == 1:
          if ID in self.listaIDs_peliculas:
            print("Ese ID de producto ya ha sido registrado. Revise y vuelva a intentar.")
            continue
          self.listaIDs_peliculas.append(ID)
          self.pelicula.ID_producto = ID
          self.pelicula.pedir_info()
          self.info_peliculas = open(self.archivo_peliculas, mode="a+", newline="")
          self.writer_peliculas = csv.writer(self.info_peliculas,delimiter=",")
          self.writer_peliculas.writerow(self.pelicula.generar_lista())
          self.info_peliculas.close()

        elif self.tipo == 2:
          if ID in self.listaIDs_videos:
            print("Ese ID de producto ya ha sido registrado. Revise y vuelva a intentar.")
            continue
          self.listaIDs_videos.append(ID)
          self.video.ID_producto = ID
          self.video.pedir_info()
          self.info_videos = open(self.archivo_videos, mode="a+", newline="")
          self.writer_videos = csv.writer(self.info_videos,delimiter=",")
          self.writer_videos.writerow(self.video.generar_lista())
          self.info_videos.close()

        elif self.tipo == 3:
          if ID in self.listaIDs_canciones:
            print("Ese ID de producto ya ha sido registrado. Revise y vuelva a intentar.")
            continue
          self.listaIDs_canciones.append(ID)
          self.cancion.ID_producto = ID
          self.cancion.pedir_info()
          self.info_canciones = open(self.archivo_canciones, mode="a+", newline="")
          self.writer_canciones = csv.writer(self.info_canciones,delimiter=",")
          self.writer_canciones.writerow(self.cancion.generar_lista())
          self.info_canciones.close()
      
      elif (self.operacion == 2):
        print("\nEscriba el tipo de contenido para ver la lista:\n 1) Película\n 2) Video\n 3) Canción")
        self.tipo = int(input("Tipo: "))

        if self.tipo == 1:
          self.info_peliculas = open(self.archivo_peliculas, mode="r+")
          self.reader_peliculas  = csv.reader(self.info_peliculas,delimiter=",")
          print('Lista de películas: ')
          for fila in self.reader_peliculas:
            print(f"(ID: {fila[0]}) {fila[1]}")
          ID_detalles = input("Para ver información más detallada sobre una película, escriba su ID (o cero (0) para salir): ")
          if ID_detalles == '0':
            self.info_peliculas.close()
            continue
          else:
            if ID_detalles not in self.listaIDs_peliculas:
              print("Ese ID no corresponde a ninguna de las películas en la lista. Vuelva a intentar.")
              self.info_peliculas.close()
              continue
            self.info_peliculas.seek(0)
            print('Detalles de la película:')
            for fila in self.reader_peliculas:
              if fila[0] == ID_detalles:
                self.pelicula = Pelicula(*fila)
                self.pelicula.mostrar_detalles()
            self.info_peliculas.close()

        elif self.tipo == 2:
          self.info_videos = open(self.archivo_videos, mode="r+")
          self.reader_videos  = csv.reader(self.info_videos,delimiter=",")
          print('Lista de videos: ') 
          for fila in self.reader_videos:
            print(f"(ID: {fila[0]}) {fila[1]}")
          ID_detalles = input("Para ver información más detallada sobre un video, escriba su ID (o cero (0) para salir): ")
          if ID_detalles == '0':
            self.info_videos.close()
            continue
          else:
            self.info_videos.seek(0)
            print('Detalles del video:')
            for fila in self.reader_videos:
              if fila[0] == ID_detalles:
                self.video = Video(*fila)
                self.video.mostrar_detalles()
            self.info_videos.close()

        elif self.tipo == 3:
          self.info_canciones = open(self.archivo_canciones, mode="r+")
          self.reader_canciones  = csv.reader(self.info_canciones,delimiter=",")
          print('Lista de canciones: ')
          for fila in self.reader_canciones:
            print(f"(ID: {fila[0]}) {fila[1]}")
          ID_detalles = input("Para ver información más detallada sobre una canción, escriba su ID (o cero (0) para salir): ")
          if ID_detalles == '0':
            self.info_canciones.close()
            continue
          else:
            self.info_canciones.seek(0)
            print('Detalles de la canción:')
            for fila in self.reader_canciones:
              if fila[0] == ID_detalles:
                self.cancion = Cancion(*fila)
                self.cancion.mostrar_detalles()
            self.info_canciones.close()
                
      elif (self.operacion == 3):
        print(f"\nMelange Contents es una plataforma creada por Antonio Reyes en abril de 2024 usando lenguaje Python")
      
      else:
        print("Opción incorrecta. Regresando al inicio.\n")
        
  def terminar(self):
    print("\nPrograma cerrado. Hasta luego.\n")