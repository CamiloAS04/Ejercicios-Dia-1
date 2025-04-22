peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Bajo Peso")
elif 18.5 <= imc <= 24.9:
    print("Peso Saludable")
elif 25.0 <= imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")