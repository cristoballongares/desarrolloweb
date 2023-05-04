n1 = int(input("Digita tu edad: ")) # supongo que esto no tiene explicacion.

veintes = n1 >= 20 and n1 < 30 # verificamos si esta en el rango 20
#print(veintes)

treintas = (n1 >= 30) and (n1 < 40) # verificamos si esta en el rango 30
#print(treintas)


# Comienza lo bueno diria yo lmao

if veintes or treintas: 
	print("Estas en el rango de los 20-30") # Devolvera esto por si esta en los 2 rangos, de lo contrario...

	if veintes:
		print("Estas en los 20`s") # Esto devolvera si esta en los 20`s
	elif treintas:
		print("Estas en los 30`s") # Esto devolvera si esta en los 30`s

else:
	print("No estas en el rango ni en 30 ni en 20") # Si no esta en ningun rango, devolvera esto
