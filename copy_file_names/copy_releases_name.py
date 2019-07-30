import os
import pyperclip

folderPath = input('Informe ou arraste o caminho da pasta: ').replace("\\", "/")
folder_files_name = os.listdir(folderPath)

names = ''
for file in folder_files_name:
    names += (file[:file.rfind('.')] + '\n')

pyperclip.copy(names)