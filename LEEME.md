# Aviso
Las funcionalidades del módulo "asistentes" se migrarán al paquete Coffeece, que pasará a ser parte de las dependencias de este paquete.
Puedes descargarlo aquí: https://github.com/FARBEX97/coffeece

# Scripts de Oficina

Este repositorio está creado con el único propósito de mejorar la calidad de vida de los empleados de oficina de habla hispana.

El repositorio tiene la siguiente estructura:

- Scripts.
- Asistentes (descontinuado -> funcionalidades migradas a Coffeece).

## Scripts

Los scripts de este repositorio son pequeños programas con funcionalidades muy específicas para descargar y utilizar sin necesidad de mucha configuración. Únicamente descarga la versión del intérprete de Python y las dependencias que se especifican al final de esta misma página.

### unificar_tablas

¡Reune tus archivos .xlsx y .csv en uno solo de forma automática con este script!

### encontrar_duplicados

Busca los archivos duplicados de manera recursiva dentro del directorio definido por el usuario.

### comprimir_img

Comprime imágenes en formato PNG y configura la calidad de imágenes en formato JPG/JPEG.

## Requisitos

- Python3 (Versión recomendada: 3.8.2 en adelante)
- Dependencias: se encuentran en el archivo "requirements.txt". Para instalar las dependencias, utiliza este comando en el directorio donde se encuentra el archivo con las dependencias:

```cmd
pip install -r requirements.txt
```

- coffeece==0.2.1
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

El contenido de este repositorio se distribuye mediante la licencia del MIT, en pocas palabras: puedes hacer lo que quieras con el código, pero si lo cambias, mejoras o distribuyes, debes incluir el archivo LICENSE tal cual está.
