    #!/usr/bin/env python

#1)Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

# with open ('lectura.txt', 'r') as archivo:
#     count = 0
#     for lineas in archivo:
#         if not lineas.startswith('p'):
#             count += 1
# print(count)


#2)Escribí un programa que lea un archivo e imprima las primeras n líneas.

# def imprimir_primeras_n_lineas(filename, n):
#     with open(filename, 'r') as archivo:
#         for i in range(n):
#             linea = archivo.readline()
#             print(linea)

# filename = input("Ingrese el nombre del archivo: ")
# n = int(input("Ingrese la cantidad de líneas a imprimir: "))

# imprimir_primeras_n_lineas(filename, n)


#3) Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

# with open ('lectura.txt', 'r') as archivo:
#     lista = []
#     for lineas in archivo:
#         lineas = archivo.readlines()
#         lista.append(lineas)
#         print(lista)


#4) Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

# with open ('lectura.txt', 'r') as archivo:
#     texto = archivo.read()
#     palabras = texto.split()
#     numero_palabras = len(palabras)
# print(f'el numero de palabras es {numero_palabras}')

#5) Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

# with open ('lectura.txt', 'r') as original:
#     texto = original.read()
# letra_remplazar = str(input('ingrese una letra: '))
# nuevo_contenido = texto.replace(letra_remplazar, letra_remplazar + '\n')
# with open ('Ejercicio5.txt', 'w') as destino:
#     destino.write(nuevo_contenido)


#6) Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

# with open ('lectura.txt', 'r') as origen:
#     texto = origen.read()
# nuevo_texto = texto.replace('\n', ' ')
# with open ('ejercicio6.txt', 'w') as destino:
#     destino.write(nuevo_texto)

#7) Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

# with open ('lectura.txt', 'r') as original:
#     texto = original.read()
#     palabras = texto.split()
#     palabra_mas_larga = max(palabras, key=len)
#     largo_palabra = len(palabra_mas_larga)
#     print(f'la palabra mas larga es {palabra_mas_larga} y tiene {largo_palabra} caracteres')


#8) Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

# with open ('lectura.txt', 'r') as arch1, open ('nombre.txt', 'r') as arch2, open ('ejercicio8.txt', 'r+') as destino:
#     contenido1 = arch1.read()
#     contenido2 = arch2.read()
#     destino.write(contenido1 and contenido2)


#9)