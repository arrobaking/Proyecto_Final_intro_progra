#Código Ejercicio de Streaming con POO.
#Primer Cuatrimestre 2024, Introducción a la Programación.
#Alumno: Antonio Reyes

#Archivo con las clases de productos usados: Película, Video y Canción.

class Producto:
  
  def __init__(self, ID_producto, titulo, anyo):
    self.ID_producto  = ID_producto
    self.titulo       = titulo
    self.anyo         = anyo
  
  def pedir_info(self):
    pass

class Pelicula(Producto):
  
  def __init__(self, ID_producto, titulo, anyo, director, actor1, actor2, genero):
    super().__init__(ID_producto, titulo, anyo)
    self.director = director
    self.actor1 = actor1
    self.actor2 = actor2
    self.genero = genero
  
  def pedir_info(self):
    self.titulo     = input("Escriba el título:        ")
    self.anyo       = input("Escriba el año:           ")
    self.director   = input("Escriba el director:      ")
    self.actor1     = input("Escriba el primer actor:  ")
    self.actor2     = input("Escriba el segundo actor: ")
    self.genero     = input("Escriba el género:        ")
  
  def generar_lista(self):
    self.lista_info = [self.ID_producto, self.titulo, self.anyo, self.director, self.actor1, self.actor2, self.genero]
    return self.lista_info
  
  def mostrar_detalles(self):
    self.generar_lista()
    print(f"\tTítulo:   {self.lista_info[1]}\n\taño:      {self.lista_info[2]}\n\tdirector:   {self.lista_info[3]}\n\tactores:    {self.lista_info[4]} y {self.lista_info[5]}\n\tgénero:  {self.lista_info[6]}")

class Video(Producto):
  
  def __init__(self, ID_producto, titulo, anyo, autor, tema):
    super().__init__(ID_producto, titulo, anyo)
    self.autor = autor
    self.tema = tema
  
  def pedir_info(self):
    self.titulo   = input("Escriba el título: ")
    self.anyo     = input("Escriba el año:    ")
    self.autor    = input("Escriba el autor:  ")
    self.tema     = input("Escriba el tema:   ")
  
  def generar_lista(self):
    self.lista_info = [self.ID_producto, self.titulo, self.anyo, self.autor, self.tema]
    return self.lista_info
  
  def mostrar_detalles(self):
    self.generar_lista()
    print(f"\tTítulo:   {self.lista_info[1]}\n\taño:      {self.lista_info[2]}\n\tautor:   {self.lista_info[3]}\n\ttema:    {self.lista_info[4]}")
    
class Cancion(Producto):
  
  def __init__(self, ID_producto, titulo, anyo, genero, album, artista):
    super().__init__(ID_producto, titulo, anyo)
    self.genero = genero
    self.album = album
    self.artista = artista
  
  def pedir_info(self):
    self.titulo   = input("Escriba el título:  ")
    self.anyo     = input("Escriba el año:     ")
    self.genero   = input("Escriba el género:  ")
    self.album    = input("Escriba el álbum:   ")
    self.artista  = input("Escriba el artista: ")
  
  def generar_lista(self):
    self.lista_info = [self.ID_producto, self.titulo, self.anyo, self.genero, self.album, self.artista]
    return self.lista_info
  
  def mostrar_detalles(self):
    self.generar_lista()
    print(f"\tTítulo:   {self.lista_info[1]}\n\taño:      {self.lista_info[2]}\n\tgénero:   {self.lista_info[3]}\n\tálbum:    {self.lista_info[4]}\n\tartista:  {self.lista_info[5]}")