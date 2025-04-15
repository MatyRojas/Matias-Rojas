print("Bienvenido al saca promedios")

nota_1 = float(input("Ingrese la primera nota "))
nota_2 = float(input("Ingrese la segunda nota "))
nota_3 = float(input("Ingrese la tercera nota "))

promedio = (nota_1 + nota_2 + nota_3)/3

print("su promedio es",promedio)

if promedio >= 40:
    print("Pasaste el curso")
else:
    print("No pasaste el curso")    
    
