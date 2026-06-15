edad = int(input("Ingresa tu edad: "))
TarjetaDeSocio = input("Tienes tarjeta de socio (si/no): ").lower()
TotalCompra = int(input("Ingresa el total de tu compra: "))

if TotalCompra >= 10000 and edad >= 60 or TarjetaDeSocio == "si":
    print("Usted cumple con los requisitos")
    print(f"Su compra es de: {TotalCompra}\nEl descuento es de 15%\nSu total con descuento es de {TotalCompra / 0.15}")
else:
    print("Usted no cumple con los requisitos para el descuento")