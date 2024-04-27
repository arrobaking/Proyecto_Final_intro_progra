import unittest

from principal.inventario import Producto, Pelicula #, Video, Cancion

class TestPelicula(unittest.TestCase):
    def test_pelicula_instance_of_producto(self):
        pelicula = Pelicula("1111", "Fight Club", "1999", "10", "10", "1.3.5", "David Fincher", "Brad Pitt", "Edward Norton", "Accion")
        self.assertIsInstance(pelicula, Producto)

    def test_genero(self):
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