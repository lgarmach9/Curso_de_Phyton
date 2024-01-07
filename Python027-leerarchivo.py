archivo = open("miarchivo.txt",'r')

#lee la primera linea y deja el cursor al final
print(archivo.readline())

#lee todo el documento
print(archivo.read())

#tambien se puede leer asi
for i in range(0,10):
    print(archivo.readline())

archivo.close()
