print("Dime tu nombre")
nombre=input()
#a continuacion quiero ver si el sistema esta guardando esa informacion
print("Hola,",nombre)

print("Dime tu edad")
edad=input()
print("Tu nombre es",nombre,"Tu edad es de",edad,"años")

edad= 15

if edad < 30:
    print("Eres una persona joven")
else:
    print("Ya no eres tan joven como antes")
    print("Esto esta dentro del else")
#las sangrias son importantes para saber las lineas que estan dentro de if
print("Esto esta FUERA del else")
