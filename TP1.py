#i = int(input('ingrese un numero: '))

#1)

# i = int(input('ingrese un numero: '))
# def posterior(numero):
#     return numero + 1
# print('el numero posterior es: ' + str(posterior(i)))

# def anterior(numero):
#     return numero - 1
# print('el numero anterior es: ' + str(anterior(i)))


# #2)

# def doble(numero):
#     return numero * 2
# print('el doble de ese numero es: ' + str(doble(i)))


# #3)


# def posteriordoble(numero):
#     return doble(posterior(i))
# print('el doble del posterior es: ' + str(posteriordoble(i)))

# def anteriordoble(numero):
#     return doble(anterior(i))
# print('el doble del anterior es: ' + str(anteriordoble(i)))


#4)

# def retirar_dinero(saldo, monto_retirado):
#     return max(saldo - monto_retirado, 0)
# print(int(input('queda en la cuenta: ' + str(retirar_dinero(60, 15)) + ' pesos')))


#5)

# def dia_de_la_semana_favorito(dia):
#     return dia == 'sabado'
# print(dia_de_la_semana_favorito('lunes'))
# print(dia_de_la_semana_favorito('sabado'))


#11) Escribir una función que tome como parámetro un string y que, si empieza con la letra "H", nos devuelva la longitud del string.

# i = str(input('ingrese una palabra: '))
# def string(palabra):
#     if palabra[0] == 'h':
#         return('La palabra tiene ' + str(len(palabra)) + ' letras')
#     else:
#         return('La palabra no empieza con H')
# print(string(i))


#12) Escribir una función que reciba como parámetro un string y nos diga si el string empieza con "Buenos" o "Buenas".

# def empieza_con_buenos(string):
#     return string.startswith('Buenos') or string.startswith('Buenas')
# print(empieza_con_buenos('Buenas'))


#13) Escribir una función llamada es_multiplo que reciba dos números y diga si el segundo es múltiplo del primero

# a = (int(input('ingrese un numero: ')))
# b = (int(input('ingrese un numero: ')))
# def es_multiplo(num1, num2):
#     if num2 % num1 == 0:
#         return('Son multiplos')
#     else:
#         return('No son multiplos')
# print(es_multiplo(a,b))


#14) Escribir una función que nos diga si un número es par, impar o cero.

# def par(numero):
#     if numero == 0:
#         return('El numero es 0')
#     elif numero % 2 == 0:
#         return('Es par')
#     else:
#         return('Es impar')
# print(par(int(input('ingrese un numero: '))))


#15) Escribir una función que tome como parámetro una frase y nos diga cuántas "a" (o "A") hay en la frase, utilizando for.

# def contar_a(frase):
#     contador = 0
#     for letra in frase:
#         if letra == "a" or letra == "A":
#             contador += 1
#     return contador
# print(contar_a(str(input('ingrese una frase: '))))


#16) Escribir una función que tome como valor una cantidad de dinero y nos diga por cuántos meses podemos subsistir con ese dinero, tomando en cuenta que se gastan 60000 pesos por mes.

def cantidad_de_meses(cantida_de_dinero):
    meses = int(cantida_de_dinero / 60000)
    return meses
print(cantidad_de_meses(int(input('ingrese la cantidad de dinero que tenga: '))))