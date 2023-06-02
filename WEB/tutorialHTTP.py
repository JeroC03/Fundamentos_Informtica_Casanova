import requests

# respuesta = requests.get('https://api.github.com/users/AJVelezRueda/orgs') #get = vervo http asociado a las consultas al servidor
#                                                                             # los vervos http disparan acciones particulares
# #agregar = requests.post() # vervo asociado a escribir datos (de 0, nuevo dato)
# #borrar = requests.delete() # vervo para borrar datos 
# #reescribir = requests.patch() # reescribe datos de una entrada

# datos = respuesta.json() # da la respuesta en formato json que tiene el formato parecido a un diccionario {'claves':'respuesta'}
# # en cuantas orgas esta involucrado el usuario?
# print(len(datos))

# # lista de nombres de las orgas en la que esta involucrada

# # for valor in datos.values():
# #     print(valor)


respuesta = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
contenido = respuesta.json()
print(contenido.keys())
print(respuesta.headers['Content-Type'])
print(respuesta.status_code)
print(len(contenido['abilities']))

#1)el protocolo es https, el dominio es pokeapi.co, y el recurso(cosas que puedo consultar en la base) es api/v2/pokemon/ditto
#2)obtiene informacion de la url
#3)el contenido type es un json 
#4) 200
#5) tiene 2 habilidades



# Estructura del proyecto
# FLASK
    #app.py --> tenemos los andpoints (rutas) de un API
    #templates --> vamos a tener todas las pantallas de mi aplicaccion (archivos html)
    #static --> vamos a tener todos los estilos de mi pantallas (archivos css)