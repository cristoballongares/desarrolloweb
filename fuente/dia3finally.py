n1 = int(input("Digita tu edad: "))

veintes = n1 >= 20 and n1 < 30
#print(veintes)

treintas = (n1 >= 30) and (n1 < 40)
#print(treintas)

if veintes or treintas:
	print("Estas en el rango de los 20-30")

	if veintes:
		print("Estas en los 20`s")
	elif treintas:
		print("Estas en los 30`s")

else:
	print("No estas en el rango ni en 30 ni en 20")
