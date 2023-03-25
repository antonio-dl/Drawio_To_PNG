# Semplice script che converte i diagrammi multipagina di drawio in png, ognuno con il nome del file + nome della pagina


import subprocess
import xml.etree.ElementTree as ET
import os
import sys


def create_result_folder(name):
    path = os.path.realpath(f".\\{name}")
    os.makedirs(path, exist_ok=True)
    return path


def check_args(argv):
    if len(argv) >= 2:
        path = argv[1]
    else:
        print("Inserire il nome del file")
        path = input()
    isFileExist = os.path.exists(path)
    if (isFileExist == False):
        print("File non esistente")
        quit()
    return path


# "C:\Program Files\draw.io\draw.io.exe" -x -f png -t --crop -p {n page} -o {script-folder\page-name} {path-to-file}
def convert_file_to_pngs(path_to_exe, path_to_file, file_name, img_dir_path, names):
    page = 0
    for name in names:
        args = [f'{path_to_exe}', '-x', '-f', 'png', '-s', '3', '-t', '--crop', '-p',
                f'{page}', '-o', f'{img_dir_path}\\{file_name}-{name}.png', f'{path_to_file}']

        print(' '.join(args))
        print()
        result = subprocess.run(args, shell=True)
        page += 1


def find_all_pages_name(root):
    names = [node.get('name') for node in root.findall('.//*[@name]')]
    return names


def print_names(names):
    for name in names:
        print(name)


path_to_exe = r"C:\Program Files\draw.io\draw.io.exe"

path_to_file = check_args(sys.argv)
file_name = os.path.basename(path_to_file)
img_dir_path = create_result_folder("images")

tree = ET.parse(path_to_file)
root = tree.getroot()

names = find_all_pages_name(root)
print_names(names)


convert_file_to_pngs(path_to_exe, path_to_file, file_name, img_dir_path, names)

input("Press Enter to exit...")
