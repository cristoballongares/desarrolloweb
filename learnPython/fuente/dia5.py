n1 = int(input("Digita un numero entre 1 y 3: "))
numbertext = ''


if n1 == 1:
	numbertext = 'Numero 1'
elif n1 == 2:
	numbertext = 'Numero 2'
elif n1 == 3:
	numbertext = 'Numero 3'
else:
	print("Valor fuera de rango")
	

print(f"Numero dado: {n1}\n{numbertext}")