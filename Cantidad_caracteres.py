frase = input("Escriba una frase\n")

print("La cantidad de letras caracteres es: {}".format(len(frase)))

# Manera lenta

frase = input("Escriba una frase\n")
cont=0
for i in frase:
    cont += 1

print("La cantidad de caracteres es: {}".format(cont))