#Proyecto Final: Recomendar qué ver en plataformas de streaming.
#Primer cuatrimestre 2024, Introducción a la Programación.
#Alumno: Antonio Reyes.

#Archivo con las pruebas unitarias para las clases correspondientes a los productos.

import unittest

from principal.productos import Producto, Pelicula, Animacion, Serie

class TestPelicula(unittest.TestCase):
    def test_pelicula_instance_of_producto(self):
        
        self.assertIsInstance(pelicula, Producto)

    def test_generaro(self):
        pelicula = Pelicula("3333", "Oppenheimer", "2023", "2", "9", "3", "Nolan", "Cillian Murphy", "Robert Downey", "120")
        genero = pelicula.definir_genero()
        self.assertEqual(genero,"Drama")

    def test_plataforma(self):
        pelicula = Pelicula("4444","Dune 2","2024","7","10","5.6","Villenueve","Austin","Florence","120")
        plataformas = pelicula.definir_plataformas()
        self.assertEqual(plataformas,"\n\t\t\tMovistar Plus+\n\t\t\tFilmin")    
    
    def test_actor2(self):
        pelicula = Pelicula("2222", "Dune", "2021", "8", "10", "1", "Villenueve", "Chalamet", "Zendaya", "120")
        actor2 = pelicula.actor2
        self.assertEqual(actor2, "Zendaya")