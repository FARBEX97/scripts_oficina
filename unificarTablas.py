# Importar los módulos necesarios
import pandas as pd
import os
import glob


def main():
    # Limpiar consola
    clear = lambda: os.system('cls')

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
            clear()

    filesToFormat = []
    for file in glob.glob('*.' + extension):
        filesToFormat.append(file)

    # Crear instancia de DataFrame
    combined = pd.DataFrame()

    # Unificar los archivos de la lista manteniendo el formato del primero
    for file in filesToFormat:
        df = pd.read_excel(file, skiprows = 0)
        combined = combined.append(df, ignore_index = True)
        print('Archivo ' + file + ' añadido.')

    # Exportar el resultado a excel
    extFinal = ""
    formatFin = False

    while formatFin == False:
        if extFinal == '1':
            combined.to_excel('combinado.xlsx')
            formatFin = True
        elif extFinal == '2':
            ecombined.to_csv('combinado.csv')
            formatFin = True
        else:
            extFinal = input('Selecciona el formato de salida:\n1) xlsx\n2) csv\n')
            clear()

    input('Proceso finalizado. Pulsa "Enter" para cerrar el programa.')


if __name__ == '__main__':
    # execute only if run as a script
    main()