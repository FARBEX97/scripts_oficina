# AsistenteWin version 1.1

import glob
import os
import shutil
from pathlib import Path




def generar_lista_xlsx():
    """Generar lista con los archivos .xlsx de la carpeta."""
    xlsx_files = []
    for file in glob.glob("*.xlsx"):
        xlsx_files.append(file)
    return xlsx_files



def generar_subdirectorios_xlsx(lista):        
    """Crea un subdirectorio por cada archivo excel de la lista dada."""
    print('Creando subdirectorios...')
    for file in lista:
        dir_name = file.replace('.xlsx','')
        os.mkdir(dir_name)
        shutil.move(file,dir_name)
        print(f'Creado directorio {file}.')



def generar_lista_subdirectorios():
    """Genera una lista con los subdirectorios del directorio."""
    subdirectorios = [os.path.abspath(x[0]) for x in os.walk('.')]
    return subdirectorios



def cambiar_dir_activo(abspath):
    """Cambiar el directorio activo al path absoluto definido."""
    os.chdir(abspath)



def cambiar_nombres_archivos(texto_entrada, texto_salida):
    """Reemplaza una cadena de texto por otra en cada nombre de usuario."""
    ruta = os.listdir()

    for archivo in ruta:
        nuevo_nombre = archivo.replace(texto_entrada,texto_salida)
        os.rename(archivo,nuevo_nombre)

