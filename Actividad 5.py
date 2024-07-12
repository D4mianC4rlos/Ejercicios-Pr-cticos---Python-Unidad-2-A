# 5 
# Crear un programa que al ingresar un número puede calcular si es mayor,
# niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años)
# adolescente (edad entre 13 y 17 años) de edad.

edad = int(input("ingresa tu edad: "))

if edad < 10:
    print("sos un niño")
elif 10 < edad <13:
    print("Usted es un pre-adolecente")
elif 13 < edad <17:
    print("Usted es un adolecente")
else:
    print("Usted es mayor de edad")