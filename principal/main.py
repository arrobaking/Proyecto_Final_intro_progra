#Proyecto Final: Recomendar qué ver en plataformas de streaming.
#Primer cuatrimestre 2024, Introducción a la Programación.
#Alumno: Antonio Reyes.

#Archivo con las clase Main, que maneja el menú principal y la ejecución general del programa.

from inventario import Inventario

class Main():
  
  def __init__(self, archivo_peliculas, archivo_animaciones, archivo_series):
    self.archivo_peliculas    = archivo_peliculas
    self.archivo_animaciones  = archivo_animaciones
    self.archivo_series       = archivo_series

    self.inventario = Inventario(self.archivo_peliculas, self.archivo_animaciones, self.archivo_series)

    self.PINdiario    = 1234
    self.operacion    = 3
    self.formato      = 4
    self.genero       = 10
    self.tipo_artista = 3
    self.eleccion     = 2
    self.artista      = ""
    self.criterios    = [self.formato, self.genero, self.tipo_artista, self.artista]
    
  def iniciar(self):
    print("\nBienvenido al catálogo de producciones audiovisuales de Melange Contents.")
    self.PINdiario = int(input("Establezca un PIN para salir del programa, al finalizar: "))

  def operar(self):
    while (self.operacion != 0):
      print("\nSeleccione la operación que desea realizar:\n\t0) Salir (ingresando el PIN).\n\t1) Solicitar una recomendación de qué mirar y dónde. ;-)\n\t2) Acerca de la plataforma.")
      self.operacion = int(input("Operación: "))

      if (self.operacion == 0):
        print("\nHa decidido cerrar el programa.")
        PIN = int(input("Escriba el PIN: "))
        if PIN==self.PINdiario:
          break
        else:
          print("\nPIN incorrecto. Regresando al inicio.")
          self.operacion = 3

      elif (self.operacion == 1):
        print("\n¿Qué tipo de formato le apetece ver hoy?\n\t1) Película (\"live action\").\n\t2) Animación (largometraje).\n\t3) Serie.")
        self.formato = int(input("Formato: "))
        self.recolectar_criterios(self.formato)
        self.resultado = self.inventario.buscar(self.criterios)
        self.resultado.mostrar_resultado()
        
      elif (self.operacion == 2):
        print(f"\nMelange Suggestions (R) es una plataforma creada por Antonio Reyes en abril de 2024 usando lenguaje Python.")
      
      else:
        print("\nOpción incorrecta. Regresando al inicio.\n")

  def recolectar_criterios(self, formato):
    print("""\n¿Cuál es el género que le suena mejor en este momento?
\t1)  Comedia.
\t2)  Drama.
\t3)  Acción.
\t4)  Terror.
\t5)  Fantasía.
\t6)  Documental.
\t7)  Familiar.
\t8)  Sci-Fi.
\t9)  Romance.
\t10) Alternativo.""")
    self.genero = int(input("Género: "))
    if formato == 1:
      print("\n¿Para cuál tipo de artista desea que se realice la búsqueda?\n\t1) Actor/actriz.\n\t2) Director.\n\t3) Ninguno.")
      self.tipo_artista = int(input("Tipo de artista: "))
    elif formato == 2:
      print("\n¿Desea incluir algún studio de animación en la búsqueda?\n\t1) Sí.\n\t2) No.")
      self.eleccion = int(input("Elección: "))
      if self.eleccion == 1:
        self.tipo_artista = 1
      else:
        self.tipo_artista = 3
        self.artista = ""
    elif formato == 3:
      print("\n¿Desea incluir algún actor/actriz en la búsqueda?\n\t1) Sí.\n\t2) No.")
      self.eleccion = int(input("Elección: "))
      if self.eleccion == 1:
        self.tipo_artista = 1
      else:
        self.tipo_artista = 3
        self.artista = ""
    if self.tipo_artista == 1:
      if (formato == 1 or formato == 3):
        self.artista = input("Ingrese el nombre del actor/actriz que desea incluir en su búsqueda: ")
      elif formato == 2:
        self.artista = input("Ingrese el nombre del studio de animación que desea incluir en su búsqueda: ")
    elif self.tipo_artista == 2:
      self.artista = input("Ingrese el nombre del(la) director(a) que desea incluir en su búsqueda: ")
    self.criterios = [formato, self.genero, self.tipo_artista, self.artista]

  def terminar(self):
    print("\nPrograma cerrado. Hasta luego.\n")
    
sesionActual = Main("info_peliculas.csv", "info_animaciones.csv", "info_series.csv")

sesionActual.iniciar()
sesionActual.operar()
sesionActual.terminar()