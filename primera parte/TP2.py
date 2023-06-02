#!/usr/bin/env python

#1) Definir un procedimiento que tome como parámetro una lista, verifique si tiene el elemento "control" y le agregue el string "revisado" y le quite el elemento "control".

# def control_lista(lista):
#     if 'control' in lista:
#         donde_control = lista.index('control')
#         lista[donde_control] = 'revisado'
#         del lista[donde_control + 1]


#2) Definir un procedimiento que tome una lista como parámetro y elimine el primer elemento de la lista. Hacer las verificaciones que sean necesarias.

# def eliminar_1(lista):
#     del lista[0]
#     return lista
# print(eliminar_1(["perro", "gato"]))


#3) Definir una función que dada una lista y un elemento devuelva la posición de este elemento en la lista.

# def posicion_elemento(lista, elemento):
#     if elemento in lista:
#         return lista.index(elemento)
#     else:
#         return -1

# print(posicion_elemento(['hola', 'sandia', 'chau', 'fruta'], 'chau'))


#4) Definir un procedimiento que tome como parámetros dos listas y un elemento, en la que se debe eliminar el elemento de una lista y agregarlo a la otra. Realizar dos versiones del ejercicio, usando un método distinto para eliminar el elemento en cada versión. ¿Qué problema/s tiene este procedimiento?

# def cmabiar_de_lista(lista1, lista2, elemento):
#     if elemento in lista1:
#         lista2.append(elemento)
#         lista1.remove(elemento)
#         return lista1, lista2
    
# print(cmabiar_de_lista(['hola', 'sandia', 'chau', 'fruta'], ['jero', 'santi', 'manu'], 'sandia'))


#5) Escribir una función que tome como parámetro una lista de enteros y devuelva una lista con valores booleanos que indique si cada elemento es par o impar. Por ejemplo, para la lista [2, 45, 108, 12, 7], la función debería retornar [True, False, True, True, False]. Utilizar la función realizada en la práctica anterior.

# def par_impar(lista):
#     return [x % 2 == 0 for x in lista]
# print(par_impar([2,5,4,3,7,8,665,3,4]))


#6) Escribir una función que lea un string y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).

# def contar_caracteres(cadena):
#     diccionario = {}
#     for caracter in cadena:
#         if caracter in diccionario:
#             diccionario[caracter] += 1
#         else:
#             diccionario[caracter] = 1
#     return diccionario
# print(contar_caracteres('hola como estas'))


#7) Modificá la función anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.

#8) Definir una función que dada una palabra, nos diga si el palíndromo o no.

# def palindromo(palabra):
#     if palabra == palabra[::-1]:
#         return "la palabra es palindromo"
#     else:
#         return 'la palabra no es palindromo'
# print(palindromo('neuquen'))


#9) Definir una función llamada productoria que toma como parámetro una lista de números y los multiplica a todos.


# def productoria(lista):
#     resultado = 1
#     for numero in lista:
#         resultado *= numero
#     return resultado
# print(productoria([3,2,5]))


#10) 