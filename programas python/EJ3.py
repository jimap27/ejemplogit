import math

print("Introduce la cantidad de gigas del disco duro ")
GB = float (input("GB: "))

MG = float (GB*1024)
print ("\nConversion a megabytes es: ")
print (MG)

MD = float (MG/1.44)


print("Numero de Discos necesarios: ", math.ceil(MD))

