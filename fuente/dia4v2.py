print("Tienda de libros \n")

namebook = input("Cual es el nombre del libro?: ")
id = int(input("Cual es la ID del libro?: "))
price = float(input(f"Cual es el precio de {namebook}?: "))

envio_gratis = (True) or (False)

envio_gratis = input("Tiene envio gratis?  \n(True/False): ")

print(f"Nombre del Libro: {namebook}\n ID del libro: {id}\n Precio de {namebook}: {price}\n Tiene envio gratis?: {envio_gratis}")