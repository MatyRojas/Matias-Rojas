print("Bienvenido al Supermercado")
print("Puede agregar los productos que desee, para salir ingrese un 0")

while True:
    opc("""Que productos llevara?
          1.- Diazepam $9000
          2.- Metametazona $18500
          3.- Oblea China $1000""")
    opc = int(input())
    if opc == 1:
        print("Usted lleva diazepam\n")
        total += 9000
    elif opc == 2:
        print("Ustes lleva Metametazona\n")
        total += 18500
    elif opc == 3:
        print("Usted lleva Oblea China\n")
        total += 1000 

print("El total neto es {}".format(total))
print("El total con IVA es {}".format(total * 1.19))    

