numero_secreto = 7
adivinanza = int(input("adivina el numero (entre 1 a 10):"))
if adivinanza == numero_secreto:
    print("¡Correcto adivinzaste el numero!")
elif adivinanza < numero_secreto:
    print("Demasiado bajo")
else:
    print("Demasiado alto")