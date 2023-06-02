#Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.
import os, glob, sys


def mover_archivos(path_resultados):
    
    textos = glob.glob('*.txt')
    contenido = ''
    for texto in textos:
        with open(texto, 'r') as txt:
            contenido += txt.read()
    os.mkdir(path_resultados)
    os.chdir(path_resultados)
    with open('archivo', 'a') as arch_final:
        arch_final.write(contenido)
mover_archivos('C:/Users/jeroc/Fundamentos_Informtica_Casanova/carpeta1/Resultados')


