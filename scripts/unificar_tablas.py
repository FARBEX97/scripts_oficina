# Importar los módulos necesarios
import pandas as pd
import os
import glob


def main():

    # Generar lista con los archivos del directorio
    extOrig = ''
    formatOrig = False
    while formatOrig == False:
        if extOrig == '1':
            extension = 'xlsx'
            formatOrig = True
        elif extOrig == '2':
            extension = 'csv'
            formatOrig = True
        else:
            extOrig = input('Selecciona el formato de origen:\n1) xlsx\n2) csv\n')

    filesToFormat = []
    for file in glob.glob('*.' + extension):
        filesToFormat.append(file)

    # Crear instancia de DataFrame
    combinado = pd.DataFrame()

    # Unificar los archivos de la lista manteniendo el formato del primero
    for file in filesToFormat:
        df = pd.read_excel(file, skiprows = 0)
        combinado = combinado.append(df, ignore_index = True)
        print('Archivo ' + file + ' añadido.')

    # Exportar el resultado a excel
    extFinal = ""
    formatFin = False

    while formatFin == False:
        if extFinal == '1':
            combinado.to_excel('combinado.xlsx')
            formatFin = True
        elif extFinal == '2':
            combinado.to_csv('combinado.csv')
            formatFin = True
        else:
            extFinal = input('Selecciona el formato de salida:\n1) xlsx\n2) csv\n')

    input('Proceso finalizado. Pulsa "Enter" para cerrar el programa.')


if __name__ == '__main__':
    main()
