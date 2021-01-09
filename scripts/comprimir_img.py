import os
import cv2
from coffeece.Popup import Popup as pu


def main():

    def input_integer(message):
        valid_input = False
        while valid_input == False:
            user_value = input(message)
            try:
                user_value = int(user_value)
                valid_input = True
            except:
                print('Please, input a number.')
        return user_value
                

    # Pedir al usuario que seleccione el archivo
    admitted_file_extensions = ['PNG', 'JPG', 'JPEG']
    img_path = pu.ask_file(admitted_file_extensions)

    # Definir las variables derivadas de la ruta del archivo
    img_name = os.path.split(img_path)[-1]
    img_extension = img_name.split('.')[-1]
    img_dir_path = os.path.split(img_path)[-2]
    new_img_name = img_dir_path + os.sep + "compressed_" + img_name

    # Leer la imagen original
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    # Definir parámetros de compresión/calidad
    if img_extension.upper() == 'PNG':
        compression_factor = input_integer('Choose a compression factor. Input a number from 0 to 9 (higher value = smaller size):')
        compression_params = [int(cv2.IMWRITE_PNG_COMPRESSION), compression_factor]
    elif img_extension.upper() == 'JPG' or 'JPEG':
        quality_value = input_integer('Choose a quality value. Input a number from 0 to 100 (higher value = higher quality = higher size):')
        compression_params = [int(cv2.IMWRITE_JPEG_QUALITY), quality_value]

    # Guardar nueva imagen
    cv2.imwrite(new_img_name, img,  compression_params)

if __name__ == "__main__":
    main()