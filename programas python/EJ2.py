print ("Introduce el numero de partidos ganados")
PG=int (input("PG: "))

print ("Introduce el numero de partidos perdidos")
PP=int (input("PP: "))

print ("Introduce el numero de partidos empatados")
PE=int (input("PE: "))

PPG = int (PG*3)
print ("Puntaje de partidos ganados: ")
print (PPG)

PPP = int (PP*0)
print ("Puntaje de partidos perdidos: ")
print (PPP)

PPE = int (PE*1)
print ("Puntaje de partidos empatados: ")
print (PPE)

PT = int (PPG+PPP+PPE)
print ("\nEl Puntaje Total es: ")
print (PT)

