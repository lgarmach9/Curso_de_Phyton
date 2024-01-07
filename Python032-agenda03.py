##Programa agenda por Laura Garcia Marchan

agenda = [["nombre","telefono","email"]]

#antes de nada, vamos a cargar los registros que teniamos en el archivo de texto
archivo = open("agenda.txt",'r')
for i in range(1,10):
    nuevalinea = archivo.readline().split(",")
    agenda.append(nuevalinea)
    
#antes de seguir, dime en que estado esta la agenda
print(agenda)

def miAgenda():
    #menu inicial
    print("Escoge tu opcion")
    print("1.-Introduce nuevo registro")
    print("2.-Listar registros")
    print("3.-Buscar registros")
    opcion = input()
    
    if opcion == "1":
        print("Introduce el nuevo nombre en la agenda")
        nombre = input()
        print("Introduce el numero de telefono")
        telefono = input()
        print("Introduce el correo")
        correo = input()
        #antes de hacer nada mas, lo metemos en la lista y lo sacamos de la lista
        agenda.append([nombre,telefono,correo])
        #print(agenda)
        #guardo en archivo
        archivo= open("agenda.txt",'a')
        longaniza = nombre+", "+telefono+", "+correo+"\n"
        archivo.write(str(longaniza))
        archivo.close()
    #ejecucion recursiva
    miAgenda()

miAgenda()

