total = float(input("ingrese el total de la cuenta: "))
porcentaje = int(input("que porcentaje de propina quieres dejar? (10, 15,20):"))
propina = total * (porcentaje / 100)
print(f"la propina es: ${propina: .2f}")