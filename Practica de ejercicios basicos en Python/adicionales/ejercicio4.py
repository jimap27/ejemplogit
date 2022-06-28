print("Ingresa las velocidades de los vehiculos")
vehiculo1 = float(input("velocidad del primer vehiculo: "))
vehiculo2 = float(input("velocidad del segundo vehiculo: "))

print("\nIngresa la distancia que separa a los vehiculos")
distancia = float(input("distancia: "))

print("\nEl tiempo de encuentro es de: ")

if vehiculo1 > 0 and vehiculo2 > 0:
    tiempo=distancia/(vehiculo1+vehiculo2)
    print(tiempo,"segundos")
else:
    print("error")
