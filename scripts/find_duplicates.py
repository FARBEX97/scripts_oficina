from coffeece.SysWalker import SysWalker as sw
from coffeece.Popup import Popup as pu


# Create a dictionary with all the files in a directory recursively
src_directory = pu.ask_directory()
files_tree = sw.list_all_files_recursively(src_directory)

# Extract duplicates and store them in a dictionary

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
