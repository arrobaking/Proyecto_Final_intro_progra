#Proyecto Final: Recomendar qué ver en plataformas de streaming
#Primer cuatrimestre 2024, Introducción a la Programación.
#Alumno: Antonio Reyes

#Archivo con las clases para los formatos de productos: Película, Animación o Serie.

class Producto:
  
  def __init__(self, ID_producto, titulo, anyo, genero, calificacion, plataformas):
    self.ID_producto    = ID_producto
    self.titulo         = titulo
    self.anyo           = anyo
    self.genero         = genero
    self.calificacion   = calificacion
    self.plataformas    = plataformas
    self.diccionario_generos      = {'1': "Comedia",
                                     '2': "Drama",
                                     '3': "Acción",
                                     '4': "Terror",
                                     '5': "Fantasía",
                                     '6': "Documental",
                                     '7': "Familiar",
                                     '8': "Sci-Fi",
                                     '9': "Romance"}
    self.diccionario_plataformas  = {'1': "Disney+",
                                     '2': "Netflix",
                                     '3': "Max (HBO)",
                                     '4': "Prime Video (Amazon)",
                                     '5': "Movistar Plus+",
                                     '6': "Filmin",
                                     '7': "Apple TV"}    
    self.genero_str       = ""
    self.plataformas_str  = ""
  
  def definir_genero():
    pass

  def definir_plataformas():
    pass

  def mostrar_detalles():
    pass

class Pelicula(Producto):
  
  def __init__(self, ID_producto, titulo, anyo, genero, calificacion, plataformas, director, actor1, actor2, duracion):
    super().__init__(ID_producto, titulo, anyo, genero, calificacion, plataformas)
    self.director = director
    self.actor1   = actor1
    self.actor2   = actor2
    self.duracion = duracion
  
  def definir_genero(self):
    self.genero_str = self.diccionario_generos[self.genero]
    return self.genero_str

  def definir_plataformas(self):
    for num_plataforma in self.plataformas:
      if num_plataforma == ".":
        pass
      else:
        self.plataformas_str += ("\n" + self.diccionario_plataformas[num_plataforma])
    return self.plataformas_str
    
  def mostrar_detalles(self):
    self.definir_genero()
    self.definir_plataformas()
    print(f"\tTítulo:         {self.titulo}
          \n\taño:            {self.anyo}
          \n\tgéneros:        {self.definir_genero()}
          \n\tdirector:       {self.director}
          \n\tactores:        {self.actor1} y {self.actor2}
          \n\tduración:       {self.duracion} minutos
          \n\tdisponible en:  {self.definir_plataformas()}")

#class Animacion(Producto):
  
  
    
#class Serie(Producto):
  
  