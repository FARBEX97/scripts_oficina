# Aviso
Las funcionalidades del módulo "asistentes" se migrarán al paquete Coffeece, que pasará a ser parte de las dependencias de este paquete.
Puedes descargarlo aquí: https://github.com/FARBEX97/coffeece

# Scripts de Oficina v1

Este repositorio está creado con el único propósito de mejorar la calidad de vida de los empleados de oficina de habla hispana.

Este repositorio tiene la siguiente estructura:

- Scripts.
- Asistentes.

## Scripts

Los scripts de este repositorio son pequeños programas con funcionalidades muy específicas para descargar y utilizar sin necesidad de mucha configuración. Únicamente descarga la versión del intérprete de Python y las dependencias que se especifican al final de esta misma página.

### ejecutar_script

Introduce la ruta a python.exe dentro de tu entorno virtual y a continuación el nombre del script que deseas ejecutar para ver la magia.

### unificar_tablas

¡Reune tus archivos .xlsx y .csv en uno solo de forma automática con este script!

#### Instrucciones

- Prepara tus ficheros en una misma carpeta y pega el script en ella ¡No importa cuántos sean!
- Ejecuta el programa unificarTablas.py y sigue las instrucciones que aparecerán en la ventana emergente (consola).
- Recoge tu fichero "combinado.xlsx/.csv".

#### Nota importante

- Para unificar los archivos, deben encontrarse en la misma carpeta.
- Para que el programa interprete bien bajo qué columnas colocar los datos, las tablas deben tener coherencia y tener siempre los mismos encabezados.
- Las celdas formuladas se quedarán como valores en lugar de fórmulas.

## Asistentes

El paquete de "asistentes" contiene funciones para algunas de las actividades más habituales en la oficina. Actualmente cuenta con:

- AsistenteExcel.py
- AsistenteGUI.py
- AsistenteWin.py

### AsistenteGUI

Contiene pequeñas funciones para las interacciones con el usuario más básicas, como seleccionar directorios o archivos, entre otros.

Cada función de este módulo abrirá una ventana emergente que se cerrará al finalizar las acciones de la misma.

### AsistenteWin

El módulo AsistenteWin pretende complementar el paquete con funciones básicas de cambiar el directorio activo, generar listas de archivos o cambiar el nombre de todos los archivos de una ubicación.

Este módulo pretende simplificar el uso de automatizaciones que requieran hacer desplazamientos por el sistema.

### AsistenteExcel

El módulo AsistenteExcel contiene las funciones típicas de Excel aplicadas a instancias de pd.DataFrame como BuscarV o concatenar.


## Requisitos

- Python3 (Versión recomendada: 3.8.2 en adelante)
- Dependencias: se encuentran en el archivo "requirements.txt". Para instalar las dependencias, utiliza este comando en el directorio donde se encuentra el archivo con las dependencias:

```cmd
pip install -r requirements.txt
```

- et-xmlfile==1.0.1
- jdcal==1.4.1
- numpy==1.19.1
- openpyxl==3.0.5
- pandas==1.1.1
- python-dateutil==2.8.1
- pytz==2020.1
- six==1.15.0
- xlrd==1.2.0

## Esto es software libre

El contenido de este repositorio se distribuye mediante la licencia del MIT, en pocas palabras: puedes hacer lo que quieras con el código, pero debes mencionarme si lo utilizas.
