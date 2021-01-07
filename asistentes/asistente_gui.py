# Aviso: las funcionalidades de este módulo se migrarán al paquete Coffeece, que pasará a ser parte de las dependencias de este paquete.
# Puedes descargarlo aquí: https://github.com/FARBEX97/coffeece

import os
from tkinter import Frame
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showinfo
import pandas as pd



def elegir_archivo():
    """Pide un archivo a traves de una ventana emergente, devuelve string con el path"""
    Tk().withdraw()
    path = askopenfilename()
    filename = os.path.relpath(path, '.') 
    return filename



def importar_excel(): 
    """Permite seleccionar un archivo excel y devuelve una instancia de pd.DataFrame() de la librería pandas."""
    filename = elegir_archivo()
    df = pd.read_excel(filename)
    return df



def importar_excel_obj(): 
    """
    Permite seleccionar un archivo excel y devuelve una instancia de pd.DataFrame() de la librería pandas, con todas las columnas marcadas como tipo dato: str.
    Atención: esta función trabaja más lento que "importar_excel()", pero conserva mejor los datos numéricos con muchos dígitos (Excel redondea los núm largos).
    """
    filename = elegir_archivo()
    cols_names = pd.read_excel(filename).columns
    types_dict = {}
    for col in cols_names:
        types_dict[col] = str    
    df = pd.read_excel(filename, dtype=types_dict)
    return df



def mensaje_info(mensaje):
    """Muestra un popup con el mensaje que se pase como argumento."""
    showinfo("Información",mensaje)



def desplegable_lista(titulo, lista_opciones):
    """Muestra una lista de opciones a través de la consola."""
    ind_valido = False
    while ind_valido == False:
        print(titulo)
        for i in range(0,len(lista_opciones)):
            print(str(i) + ') ' + lista_opciones[i])

        ind_elegido = ""

        try:
            ind_elegido = int(input('Escribe el índice que deseas (ej: "1" -> ' + lista_opciones[1] + '):'))
            if ind_elegido not in range(0,len(lista_opciones)):
                os.system('cls')
                print('Valor fuera de rango.')
            else:
                valor_elegido = lista_opciones[ind_elegido]
                ind_valido = True
                return valor_elegido
        except:
            os.system('cls')
            print('Valor no válido.')



def elegir_directorio():
    """Pide un directorio a traves de una ventana emergente, devuelve string con el path"""
    Tk().withdraw()
    path = askdirectory()
    folder_selected = os.path.abspath(path) 
    return folder_selected



def exportar_excel(df, nombre_excel):
    """Exporta DataFrame a excel y entra en bucle si da error, para no perder el progreso."""
    print('Exportando a excel.')
    guardado = False
    while guardado == False:
        try:
            df.to_excel(f'{nombre_excel}.xlsx')
            print('Exportado.')
            guardado = True
        except:
            mensaje_info('Error al guardar archivo. Si tiene abierto un archivo con el mismo nombre, ciérrelo y pulse "Aceptar".')

