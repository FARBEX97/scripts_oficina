# Aviso: las funcionalidades de este módulo se migrarán al paquete Coffeece, que pasará a ser parte de las dependencias de este paquete.
# Puedes descargarlo aquí: https://github.com/FARBEX97/coffeece

def definir_cabeceras(ruta_formato):
    """Compara el modelo definido con el formato deseado y devuelve un diccionario."""
  
    modelo = pd.read_excel(ruta_formato, sheet_name='modelo')
    formato = pd.read_excel(ruta_formato, sheet_name='formato')
  
    cols_modelo = modelo.columns.values.tolist()
    cols_formato = formato.columns.values.tolist()
    return dict(zip(cols_modelo, cols_formato))
  
 
