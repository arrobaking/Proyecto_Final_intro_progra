#Código Ejercicio de Streaming con POO.
#Primer Cuatrimestre 2024, Introducción a la Programación.
#Alumno: Antonio Reyes

#Archivo con el flujo principal de ejecución.
#Los archivos "info_peliculas.csv", "info_videos.csv" y "info_canciones.csv" almacenan los datos de los productos contenidos, para cada categoría.

from clase_main import Main

sesionActual = Main("info_peliculas.csv", "info_videos.csv", "info_canciones.csv")

sesionActual.iniciar()
sesionActual.operar()
sesionActual.terminar()