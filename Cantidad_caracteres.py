# frase = input("Escriba una frase\n")

# print("La cantidad de letras caracteres es: {}".format(len(frase)))

# # Manera lenta

# frase = input("Escriba una frase\n")
# cont=0
# for i in frase:
#     cont += 1

# print("La cantidad de caracteres es: {}".format(cont))

#Solo vocales

frase = input("Escriba una frase\n")
cont = 0
vocal = 0
cons = 0
for i in frase:
    print(i)
    cont += 1
    # if i == "a" or i == "e" or i == "i" or i == "o" or == "u":  #Forma larga
    #     vocal += 1
    if i.lower() in "aeiou":
        vocal += 1
    elif i.lower() != " ":
        cons += 1

print("El total de caracteres es {}".format(cont))    
print("Esta frase tiene {} vocales".format(vocal))
print("Esta frase tiene {} consonantes".format(cons))
