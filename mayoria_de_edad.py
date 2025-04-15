#Verificacion de mayoria de edad

edad = int(input(print("Escriba su edad")))

if edad >= 18: 
    print("Con {} eres mayor de edad".format(edad))
elif edad < 12:
    print("Con {} eres un niño".format(edad))
elif edad >= 12 and edad <= 17:
    print("Con {} eres un adolecente".format(edad))    
