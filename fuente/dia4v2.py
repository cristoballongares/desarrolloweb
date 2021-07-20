print("Tienda de libros \n")

namebook = input("Cual es el nombre del libro?: ")
id = int(input("Cual es la ID del libro?: "))
price = float(input(f"Cual es el precio de {namebook}?: "))
envio_gratis = input("Tiene envio gratis?  \n(True/False): ")

if envio_gratis == 'True':
	envio_gratis = True
elif envio_gratis == 'False':
	envio_gratis == False
else:
	print("Valor incorrecto, digita True (Verdadero) o False (Falso)\n")

print(f"\nNombre del Libro: {namebook}\n ID del libro: {id}\n Precio de {namebook}: {price}\n Tiene envio gratis?: {envio_gratis}")