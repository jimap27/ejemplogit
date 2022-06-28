import math

print("Ingrese la coordenada en X para el punto A")
AX = float(input())
print("Ingrese la coordenada en Y para el punto A")
AY = float(input())

print("Ingrese la coordenada en X para el punto B")
BX = float(input())
print("Ingrese la coordenada en X para el punto B")
BY = float(input())

D  = math.sqrt(pow(AX-BX,2)+pow(AY-BY,2))

print("La distancia entre el punto A y el Punto B es: ", round(D, 2))




