print ("Introduce el numero de respuestas correctas")
RC=int (input("RC: "))

print ("Introduce el numero de respuestas incorrectas")
RI=int (input("RI: "))

print ("Introduce el numero de respuestas en blanco")
RB=int (input("RB: "))

PRC = int (RC*3)
print ("\nPuntaje de respuestas correctas: ")
print (PRC)

PRI = int (RI*(-1))
print ("\nPuntaje de respuestas Incorrectas: ")
print (PRI)

PRB = int (RB*0)
print ("\nPuntaje de respuestas en blanco: ")
print (PRB)

PF = int (PRC+PRI+PRB)
print ("\nEl Puntaje Final es: ")
print (PF)



