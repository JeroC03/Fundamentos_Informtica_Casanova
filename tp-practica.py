#!/usr/bin/env python

import os, glob, sys

# def ejercicio_rutas():
#     os.chdir("informes")
#     txt = glob.glob("*.txt")
#     cantidad_estado = []
#     cantidad_lineas = []
#     for archivo in txt:
#         with open(archivo, "r") as file:
#             file_completa = file.read()
#             cantidad_estado.append(file_completa.count("estado"))
#             cantidad_lineas.append(file_completa.count("\n"))
#     os.mkdir("Apellido")
#     with open("Apellido/Lista.txt", "w") as salida:
#         for archivo in txt:
#             with open(archivo, "r") as file:
#                 salida.write(file.readline())
#     return cantidad_estado, cantidad_lineas
# c1, c2 = ejercicio_rutas


# class Biblioteca:
#   def __init__(self):
#     self.libros = set()

#   def agregar_libro(self, libro):
#     self.libros.add(libro)
    
#   def libros_largos(self):
#     return [libro for libro in self.libros if libro.es_largo()]

#   def titulos_disponibles(self):
#     return [libro.titulo for libro in self.libros]

# class Libro(Biblioteca):
#   def __init__(self, titulo, paginas, genero, autoria):
#     self.titulo = titulo
#     self.paginas = paginas
#     self.genero = genero
#     self.autoria = autoria

#   def nacionalidad(self):
#         return self.autoria["nacionalidad"]

#   def es_largo(self):
#     return self.paginas > 300

# autor_carl_sagan = {"nombre": "Carl", "apellido": "Sagan", "nacionalidad": "Estados Unidos"}
# autor_elsa_bornemann = {"nombre": "Elsa", "apellido": "Bornemann", "nacionalidad": "Argentina"}

# libro_contacto = Libro("Contacto", 400, "Ciencia Ficción", autor_carl_sagan)
# libro_socorro = Libro("Socorro", 250, "Terror", autor_elsa_bornemann)
                 
# biblioteca_de_emma = Biblioteca()
# biblioteca_de_emma.agregar_libro(libro_contacto)
# biblioteca_de_emma.agregar_libro(libro_socorro)


def primeras_lineas(path_a_txt, path_resultado, salida):
    os.chdir(path_a_txt) # te moves al archivo que queres leer
    textos = glob.glob('*.txt')
    primer_linea = []
    for txt in textos:
        with open(txt, 'r') as texto:
            primer_linea.append(texto.readline())
    os.chdir('../../')
    os.mkdir(path_resultado) # crea una carpeta en el path que le pases
    os.chdir(path_resultado)
    with open(salida, 'a') as final_txt:
        for linea in primer_linea:   # se hace porque primer_linea es una lista y el metodo .write no lee listas por lo que tenees que trasformar la lista en str
            final_txt.write(linea)




