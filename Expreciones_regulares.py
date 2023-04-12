import re
# Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?

#r'\d{4,}'

# Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?

#r'[a-z]{3,6}'

# Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string?

#r'ab*'

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = 'ipsum(.*)elit'
print(re.search(patron, texto))
#print(texto[22:26])
#print(re.match(patron, texto)) #match es para ver si el patron esta al principio
#print(re.findall(patron, texto)) # findall te muestra todas las veces que encuentra tu patron
print(re.search(patron, texto).group()) # el .group() te muestra los caracteres que encontraste
print(re.sub(patron, "###", texto))