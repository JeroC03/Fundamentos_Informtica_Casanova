#!/usr/bin/env python

import os, glob

def ejercicio_rutas():
    os.chdir("informes")
    txt = glob.glob("*.txt")
    cantidad_estado = []
    cantidad_lineas = []
    for archivo in txt:
        with open(archivo, "r") as file:
            file_completa = file.read()
            cantidad_estado.append(file_completa.count("estado"))
            cantidad_lineas.append(file_completa.count("\n"))
    os.mkdir("Apellido")
    with open("Apellido/Lista.txt", "w") as salida:
        for archivo in txt:
            with open(archivo, "r") as file:
                salida.write(file.readline())
    return cantidad_estado, cantidad_lineas
c1, c2 = ejercicio_rutas