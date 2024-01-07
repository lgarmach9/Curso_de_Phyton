##Programa agenda por Laura Garcia Marchan

agenda = [["nombre","telefono","email"]]

print(agenda)

def miAgenda():
    print("Introduce el nuevo nombre en la agenda")
    nombre = input()
    print("Introduce el numero de telefono")
    telefono = input()
    print("Introduce el correo")
    correo = input()
    #antes de hacer nada mas, lo metemos en la lista y lo sacamos de la lista
    agenda.append([nombre,telefono,correo])
    print(agenda)
    #guardo en archivo
    archivo= open("agenda.txt",'a')
    longaniza = nombre+", "+telefono+", "+correo+"\n"
    archivo.write(str(longaniza))
    archivo.close()
    #ejecucion recursiva
    miAgenda()

miAgenda()

