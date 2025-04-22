candidato_1 = "Coyote"
Candidato_2 = "Correcaminos"

cantidad_votos1 = 0
cantidad_votos2 = 0

cantidad_votantes = int(input("Ingrese la cantidad de votantes\n" ))

for i in range(cantidad_votantes):
    print("Por quien va a votar:\n"
           f"1.-{candidato_1}\n"
            f"2.-{Candidato_2}")
    voto =int(input())
    if voto == 1:
        cantidad_votos1 += 1
    elif voto == 2:
        cantidad_votos2 += 1
    
    if voto == 1:
        print("Usted voto por {}\n".format(candidato_1))
    else:
        print("Usted voto por {}\n".format(Candidato_2))

print("La cantidad de votos para {} es {}".format(candidato_1,cantidad_votos1))
print("La cantidad de votos para {} es {}".format(Candidato_2,cantidad_votos2))

if cantidad_votos1 > cantidad_votos2:
    print("\nEl gandor es: {}".format(candidato_1))
elif cantidad_votos2 > cantidad_votos1:
    print("\nEl gandor es: {}".format(Candidato_2))
    

                              