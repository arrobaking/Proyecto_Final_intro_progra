from inventario import Inventario

class Main():
  
  def __init__(self):
    self.PINdiario  = 1234
    self.inventario = inventario
    self.operacion  = 3
    self.formato    = 4
    
  def iniciar(self):
    print("\nBienvenido al catálogo de producciones audiovisuales de Melange Contents.")
    self.PINdiario = int(input("Establezca un PIN para salir del programa, al finalizar: "))

  def operar(self):
    while (self.operacion != 0):
      print("\nSeleccione la operación que desea realizar:\n\t0) Salir (ingresando el PIN).\n\t1) Solicitar una recomendación de qué mirar y dónde. ;-)\n\t2) Acerca de la plataforma.")
      self.operacion = int(input("Operación: "))

      if (self.operacion == 0):
        print("Ha decidido cerrar el programa.")
        PIN = int(input("Escriba el PIN: "))
        if PIN==self.PINdiario:
          break
        else:
          print("PIN incorrecto. Regresando al inicio.")
          self.operacion = 3

      elif (self.operacion == 1):
        print("\n¿Qué tipo de formato le apetece ver hoy?\n\t1) Película (\"live action\").\n\t2) Animación.\n\t3) Serie.")
        self.formato = int(input("Formato: "))
        self.recolectar_criterios(self.formato)
                
      elif (self.operacion == 2):
        print(f"\nMelange Suggestions (R) es una plataforma creada por Antonio Reyes en abril de 2024 usando lenguaje Python.")
      
      else:
        print("Opción incorrecta. Regresando al inicio.\n")

  def recolectar_criterios(self, formato):
    print("""¿Cuál es el género que le suena mejor en este momento?
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
    self.genero = input("Género: ")

  def mostrar_resultados():

  def terminar(self):
    print("\nPrograma cerrado. Hasta luego.\n")
    

sesionActual = Main("info_peliculas.csv", "info_animaciones.csv", "info_series.csv")

sesionActual.iniciar()
sesionActual.operar()
sesionActual.terminar()