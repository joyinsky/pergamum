import os
import glob
import tablib

TYPES = {'txt', 'png', 'wmv', 'rtf', 'pps', 'jpg', 'wma', 'mdi', 'doc', 'pptx', 'pdf', 'xls', 'htm', 'docx', 'gif'}


data = tablib.Dataset(headers=[])

archivos = [file for file in glob.glob("articledb/**/*", recursive=True) if os.path.isfile(file)]
nombre_archivo = ["".join(archivo.split('/')[-1].split('.')[0:-1]) for archivo in archivos]
extensiones = [archivo.split('.')[-1].lower() for archivo in archivos]
carpetas = ["/".join(archivo.split('/')[1:-1]) for archivo in archivos]

data.append_col(nombre_archivo, header='filename')
data.append_col(extensiones, header='ext')
data.append_col(carpetas, header='folder')
data.append_col(archivos, header='path')

data.headers = ['filename', 'ext', 'folder', 'path']

if __name__ == "__main__":
    with open("archivos.csv", "w") as db:
        db.write(data.csv)
    print(set(data['ext']))