from coffeece.SysWalker import SysWalker as sw
from coffeece.Popup import Popup as pu


def main():
    # Crea un diccionario con las rutas, carpetas y archivos
    # dentro de la carpeta especificada por el usuario
    src_directory = pu.ask_directory()
    files_tree = sw.list_all_files_recursively(src_directory)

    # Extrae los nombres de archivo duplicados y crea un diccionario
    # relacionando nombres de archivo duplicados y las rutas que tienen

    unique_filenames = []
    duplicate_files = {}

    for root in files_tree:
        for file in files_tree[root]["files"]:
            if file in unique_filenames:
                if file in duplicate_files:
                    duplicate_files[file]["paths"].append(root)
                else:
                    duplicate_files[file] = {}
                    duplicate_files[file]["paths"] = []
                    duplicate_files[file]["paths"].append(root)
            else:
                unique_filenames.append(file)

    for file in duplicate_files:
        print(f"File {file} exists on various locations:")
        for path in duplicate_files[file]["paths"]:
            print(path)


if __name__ == '__main__':
    main()
