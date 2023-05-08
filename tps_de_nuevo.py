import re

#1) Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

# def lineas_con_P(archivo):
#     with open(archivo, 'r') as texto:
#         contador = 0
#         for lineas in texto:
#             if lineas.startswith('P'):
#                 contador += 1
#         return contador
# print(lineas_con_P('pruebas.txt'))

#2)Escribí un programa que lea un archivo e imprima las primeras n líneas

# def leer_n_lineas(archivo, n):
#     with open(archivo, 'r') as texto:
#         for i in range(n):
#             linea = texto.readline()
#             print(linea)
# print(leer_n_lineas('pruebas.txt', 6))

#6) Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo

# def eliminar_saltos(arch1, arch2):
#     with open(arch1, 'r') as texto:
#         contenido = texto.read()
#         eliminar = contenido.replace('\n', ' ')
#         with open(arch2, 'a') as destino:
#             destino.write(eliminar)
# eliminar_saltos('pruebas.txt', 'ejercicio8.txt')

#7) Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

# def palabra_mas_larga(arch1):
#     with open(arch1, 'r') as texto:
#         contenido = texto.read()
#         palabras = contenido.split()
#         palabra_larga = max(palabras, key=len)
#         largo = len(palabra_larga)
#         return (f'La palabra mas larga es {palabra_larga} y tiene {largo} caracteres')
# print(palabra_mas_larga('pruebas.txt'))

#10) Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.



# EXPRECIONES REGULARES

#1)Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.

# def caracter_permitido(string):
#     return bool(re.search('[Aa-zZ0-9]', string))
# print(caracter_permitido('fgd'))

#2) Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.

# def caracter_permitido(string):
#     return bool(re.search('[^Aa-zZ0-9]', string))
# print(caracter_permitido('fgd'))

#3) Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")

# def extraccion(string):
#     patron = '-(.*?)-'
#     return re.findall(patron, string)
# print(extraccion("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"))



#4) Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado

# def contar_palabras(archivo):
#     with open(archivo, 'r') as texto:
#         contenido = texto.read()
#         palabras = contenido. split()
#         return len(palabras)
# print(contar_palabras('pruebas.txt'))

#5) Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

# def remplazar(archivo):
#     with open(archivo, 'r') as origen:
#         contenido = origen.read()
#         remplaza = contenido.replace('e', 'e' + '\n')
#         with open('ejercicio5.txt', 'w') as destino:
#             destino.write(remplaza)
# remplazar('pruebas.txt')



# class Pasta:
#     def __init__(self):
#         self.ajies = 0

#     def picantear(self):
#         if self.ajies <= 10:
#             self.ajies += 5
#         else:
#             raise Exception("El plato ya está demasiado picante")

#     def suavizar(self):
#         self.ajies -= 1

# class Pizza:
#     def __init__(self):
#         self.condimento = "adobo"
        
#     def picantear(self):
#         if self.condimento == "cayena":
#             raise Exception("El plato ya esta demasiado picante")
#         self.condimento = "cayena"
        
#     def suavizar(self):
#         self.condimento = "orégano"


# class Chef:
#     def __init__(self, plato_del_dia):
#         self.plato_del_dia = plato_del_dia

#     def picantear(self):
#         self.plato_del_dia.picantear()

#     def suavizar(self, plato):
#         plato.suavizar()

# class AyudanteDeCocina:
#     def suavizar(self, plato):
#         plato.suavizar()