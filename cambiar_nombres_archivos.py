import os

ruta = os.listdir()

for archivo in ruta:
    nuevo_nombre = archivo.replace(" ","_")
    os.rename(archivo,nuevo_nombre)
