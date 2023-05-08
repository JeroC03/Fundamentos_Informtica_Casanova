import re
# Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?

#r'\d{4,}'

# Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?

#r'[a-z]{3,6}'

# Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string?

#r'ab*'

#texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
#patron = 'ipsum(.*)elit'
#print(re.search(patron, texto))
#print(texto[22:26])
#print(re.match(patron, texto)) #match es para ver si el patron esta al principio
#print(re.findall(patron, texto)) # findall te muestra todas las veces que encuentra tu patron
#print(re.search(patron, texto).group()) # el .group() te muestra los caracteres que encontraste
#print(re.sub(patron, "###", texto))

#TP expreciones regulares

#1) Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.

def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z0-9]', string))
print(caracteres_permitidos('expreci/.on#'))

#2) Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.

# def caracteres_permitidos(string):
#     return not bool(re.search('[^a-zA-Z0-9]', string))
# print(caracteres_permitidos('exprecion'))

#3) Creá un programa que verifique las siguientes condiciones:
#si un string dado tiene una h seguida de ninguna o más e.

def encontrar_patron(string):
    patron = 'he*'
    if re.search(patron, string) is not None:
        return 'Se encontro el patron'
    else:
        return 'No se encontro el patron'
    
#si un string dado tiene una h seguida de una o más e.

def encontrar_patron(string):
    patron = 'he+'
    if re.search(patron, string) is not None:
        return 'Se encontro el patron'
    else:
        return 'No se encontro el patron'

#si un string dado tiene una h seguida de cero o una e.

def encontrar_patron(string):
    patron = 'he?'
    if re.search(patron, string) is not None:
        return 'Se encontro el patron'
    else:
        return 'No se encontro el patron'

#si un string dado tiene una h seguida de dos o tres e.

def encontrar_patron(string):
    patron = 'he{2;3}'
    if re.search(patron, string) is not None:
        return 'Se encontro el patron'
    else:
        return 'No se encontro el patron'
    

#4) Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).

def palabra_unida(string):
    patron = '^[aA-zZ]+_[aA-zZ]+$'
    if re.search(patron, string) is not None:
        return 'patron encontrado'
    else:
        return 'patron no encontrado'
#cadena = input('ingrese ena cadena: ')
#print(palabra_unida(cadena))

#5) Escribí un programa que diga si un string empieza con un número específico.

def numero_especifico(string):
    patron = '^5+[aA-zZ]'
    if re.search(patron, string) is not None:
        return 'patron encontrado'
    else:
        return 'patron no encontrado'
#print(numero_especifico('7gjked'))


#8) Escribí un programa que separe y devuelva los caracteres númericos de un string.

def extraer_numeros(string):
    resultado = re.split('\D+', string)
    for elemento in resultado:
        print(elemento)
#print(extraer_numeros('movi 10 cajas de 5 logar'))

#9) Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")

def entre_guiones(string):
    return re.findall(r'-(.*?)-', string) #el ? mira los matches internos
strin = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
#print(entre_guiones(strin))

#10) Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.

def get_substr(string):
    return re.findall('[@|&](.*?)[@|&]', string)
#print(get_substr('curn@ jirf@runr &rfvh ujeejn '))



