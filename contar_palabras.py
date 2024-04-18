import sys

def leerContar(txt):
    archivo = open(txt).read()
    palabras = archivo.split()
    count = 0
    count2 = len(palabras)

if __name__ == "__main__":
    archivo = sys.argv[1]
    leerContar(archivo)