ventas = [
    [],
    [], 
    []
    ]
    
ventas[0].append(34)
ventas[0].append(21)
ventas[0].append(21)
ventas[1].append(31)
ventas[1].append(1)
ventas[1].append(7)
ventas[2].append(10)
ventas[2].append(64)
ventas[2].append(27)
suma1 = sum(ventas[0])
suma2 = sum(ventas[1])
suma3 = sum(ventas[2])
print(f"{ventas}")
print(f"El primero vendio: {suma1}")
print(f"El segundo vendio: {suma2}")
print(f"El tercero vendio: {suma3}")

if suma1 >= suma2 and suma1 >= suma3:
    print("Primer Vendedor es el mejor")
if suma2 >= suma1 and suma2 >= suma3:
    print("Segundo Vendedor es el mejor")
if suma3 >= suma2 and suma3 >= suma1:
    print("Tercer Vendedor es el mejor")

if suma1 <= 30000:
    print("Las ventas del primero son menores a 30.000")
if suma2 <= 30000:
    print("Las ventas del segundo son menores a 30.000")
if suma3 <= 30000:
    print("Las ventas del tecero son menores a 30.000")