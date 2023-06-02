
#modificar este script para que puede incorporar el nombre de los archivos desde la terminal

import sys
import os

if len(sys.argv) != 3:
    print("Debe proporcionar el nombre de los archivos origen y destino.")
    print("Ejemplo: python script.py archivo1.txt archivo2.txt")
    sys.exit()

archivo1 = sys.argv[1]
archivo2 = sys.argv[2]

if not os.path.exists(archivo1):
    print(f"El archivo {archivo1} no existe.")
    sys.exit()

os.rename(archivo1, archivo1 + '.temp')
os.rename(archivo2, archivo1)
os.rename(archivo1 + '.temp', archivo2)

print(f"Los archivos {archivo1} y {archivo2} han sido intercambiados correctamente.")