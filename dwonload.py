from urllib import request
import sys

def descargar_pdf(pdfUrl, name):
    print(pdfUrl)
    response = request.urlopen(pdfUrl)
    file= open(name+ ".pdf", "wb")
    file.write(response.read())
    

if __name__ == "__main__":
    archivo = sys.argv[1]
    print(archivo)
    nombre = sys.argv[2]
    print(nombre)
    descargar_pdf(archivo, nombre)
    