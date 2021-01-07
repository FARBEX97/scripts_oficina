# Aviso: las funcionalidades de este módulo se migrarán al paquete Coffeece, que pasará a ser parte de las dependencias de este paquete.
# Puedes descargarlo aquí: https://github.com/FARBEX97/coffeece

import pandas as pd


def buscarv_col(df_resultado, valor_comun, valor_buscado_izq, valor_buscado_dcha, df_busqueda):
    """
    Ejecuta una función igual a BuscarV en Excel. Devuelve pd.DataFrame()
    df_resultado = DF sobre el que deseamos efectuar el BuscarV.
    valor_comun = nombre de la columna a usar como índice en la búsqueda.
    valor_buscado_izq = nombre de la columna sobre la que desamos efectuar el BuscarV.
    valor_buscado_dcha = nombre de la columna del segundo DF que contiene los valores a encontrar. 
    
    """
    df_aux = df_resultado.merge(df_busqueda, on=valor_comun, how='left')
    df_resultado[valor_buscado_izq] = df_aux[valor_buscado_dcha]
    return df_resultado


def buscarx_celda(valor_buscado, columna_buscar, columna_devolver):
    """
    Fuente: pythoninoffice.com
    valor_buscado: valor en el que estamos interesados, será una string.
    columna_buscar: columna en la que vamos a buscar el valor buscado.
    columna_devolver: columna en la que esperamos encontrar un valor.    
    """
    return columna_devolver.loc[columna_buscar == valor_buscado].tolist()[0]

