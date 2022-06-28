sueldo = float(input("Ingresa tu sueldo: "))
aumento = float( sueldo * 0.15)
Sueldo_aumento = ( sueldo + aumento)

if sueldo <= 1000:
    print("Tu sueldo es: ", Sueldo_aumento)
else:
    print("No se aplica aumento")
