

peso = input("¿Cual es tu peso en kilos?")
altura = input("¿Cual es tu altura en metros")

Imc = round(float(peso)/float(altura)**2,2)
print("Tu indice de masa corporal es: " + str(Imc))
