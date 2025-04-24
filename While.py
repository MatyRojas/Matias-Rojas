#Explicacion y uso del While

num = 0

while num <5:
    print("hola")
    num += 1 

#otro ejemplo

num = 10

import time 

while num > 0:
    print(num)
    time.sleep(1)
    num -= 1

#Clave

clave = 213
password = int(input("Ingrese la contraeña\n")) 

while clave != password:
    print("Error, intente otra vez")
    password = int(input("Ingrese la contraeña\n"))

print("Contraseña Correcta!!!")

# Solo con 3 intentos

clave = 213
password = int(input("Ingrese la contraeña\n"))
intento = 3

while clave != password:
    intento -= 1
    print("Error, le quedan {} intentos\n".format(intento))
    password = int(input("Ingrese la contraeña\n"))
    if intento <= 1:
        break

if intento != 0 and clave == password:
    print("Contraseña Correcta!!!")
else:
    print("Sistema Bloqueado")      