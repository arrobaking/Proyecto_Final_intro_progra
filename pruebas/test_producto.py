#Proyecto Final: Recomendar qué ver en plataformas de streaming.
#Primer cuatrimestre 2024, Introducción a la Programación.
#Alumno: Antonio Reyes.

#Archivo con las pruebas unitarias para las clases correspondientes a los productos.

import unittest

from principal.productos import Producto, Pelicula, Animacion, Serie

ID_producto_pelicula = "1003"
titulo_pelicula = "Oppenheimer"
anyo_pelicula = "2023"
genero_pelicula = "10"
calificacion_pelicula = "9"
plataformas_pelicula = "3.4"
director_pelicula = "Christopher Nolan"
actor1_pelicula = "Cillian Murphy"
actor2_pelicula = "Robert Downey"
duracion_pelicula = "180"

ID_producto_animacion = "2004"
titulo_animacion = "Ponyo"
anyo_animacion = "2008"
genero_animacion = "5"
calificacion_animacion = "8"
plataformas_animacion = "7"
studio_animacion = "Ghibli"
duracion_animacion = "110"

ID_producto_serie = "3001"
titulo_serie = "Game of Thrones"
anyo_serie = "2011"
genero_serie = "2"
calificacion_serie = "10"
plataformas_serie = "1.2"
actor1_serie = "Jason Momoa"
actor2_serie = "Sean Bean"
num_temporadas_serie = "8"

pelicula    = Pelicula(ID_producto_pelicula,
                       titulo_pelicula,anyo_pelicula,
                       genero_pelicula,
                       calificacion_pelicula,
                       plataformas_pelicula,
                       director_pelicula,
                       actor1_pelicula,
                       actor2_pelicula,
                       duracion_pelicula)                       
animacion   = Animacion(ID_producto_animacion,
                        titulo_animacion,
                        anyo_animacion,
                        genero_animacion,
                        calificacion_animacion,
                        plataformas_animacion,
                        studio_animacion,
                        duracion_animacion)
serie       = Serie(ID_producto_serie,
                    titulo_serie,
                    anyo_serie,
                    genero_serie,
                    calificacion_serie,
                    plataformas_serie,
                    actor1_serie,
                    actor2_serie,
                    num_temporadas_serie)

class TestProducto(unittest.TestCase):

    def test_instance_of_producto_pelicula(self):
        self.assertIsInstance(pelicula, Producto)

    def test_genero_pelicula(self):
        genero = pelicula.definir_genero()
        self.assertEqual(genero, "Alternativo")

    def test_plataforma_pelicula(self):
        plataformas = pelicula.definir_plataformas()
        self.assertEqual(plataformas, "\n\t\t\tMax (HBO)\n\t\t\tPrime Video (Amazon)")    
    
    def test_member_pelicula(self):
        actor2 = pelicula.actor2
        self.assertEqual(actor2, "Robert Downey")

    def test_orden_pelicula(self):
        ID = pelicula.ID_producto
        self.assertNotEqual(ID, "2023")

    def test_instance_of_producto_animacion(self):
        self.assertIsInstance(animacion, Producto)

    def test_genero_animacion(self):
        genero = animacion.definir_genero()
        self.assertEqual(genero, "Fantasía")

    def test_plataforma_animacion(self):
        plataformas = animacion.definir_plataformas()
        self.assertEqual(plataformas, "\n\t\t\tApple TV")    
    
    def test_member_animacion(self):
        studio = animacion.studio
        self.assertEqual(studio, "Ghibli")

    def test_orden_animacion(self):
        ID = animacion.ID_producto
        self.assertNotEqual(ID, "2008")

    def test_instance_of_producto_serie(self):
        self.assertIsInstance(serie, Producto)

    def test_genero_serie(self):
        genero = serie.definir_genero()
        self.assertEqual(genero, "Drama")

    def test_plataforma_serie(self):
        plataformas = serie.definir_plataformas()
        self.assertEqual(plataformas, "\n\t\t\tDisney+\n\t\t\tNetflix")    
    
    def test_member_serie(self):
        titulo = serie.titulo
        self.assertEqual(titulo, "Game of Thrones")

    def test_orden_serie(self):
        anyo = serie.anyo
        self.assertNotEqual(anyo, "3001")