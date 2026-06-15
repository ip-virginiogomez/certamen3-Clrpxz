#Autopista
velocidades0 = int(input("Ingresa 5 velocidades distintas: "))
velocidades1 = int(input("Ingresa 5 velocidades distintas: "))
velocidades2 = int(input("Ingresa 5 velocidades distintas: "))
velocidades3 = int(input("Ingresa 5 velocidades distintas: "))
velocidades4 = int(input("Ingresa 5 velocidades distintas: "))
ListadoDeVelocidades = [0]
ListaDeVelocidades = [velocidades0, velocidades1, velocidades2, velocidades3, velocidades4]
promedio_de_velocidades = sum(ListaDeVelocidades) / len(ListaDeVelocidades)

if velocidades0 <= 20 or velocidades0 >= 140:
    print("Peligro")
elif velocidades0 <= 60 or velocidades0 >= 120:
    print(f"La primera velocidad esta por fuera del limite permitido")

if velocidades1 <= 20 or velocidades1 >= 140:
    print("Peligro")
elif velocidades1 <= 60 or velocidades1 >= 120:
    print(f"La segunda velocidad esta por fuera del limite permitido")

if velocidades2 <= 20 or velocidades2 >= 140:
    print("Peligro")
elif velocidades2 <= 60 or velocidades2 >= 120:
    print(f"La tercera velocidad esta por fuera del limite permitido")

if velocidades3 <= 20 or velocidades3 >= 140:
    print("Peligro")
elif velocidades3 <= 60 or velocidades3 >= 120:
    print(f"La cuarta velocidad esta por fuera del limite permitido")

if velocidades4 <= 20 or velocidades4 >= 140:
    print("Peligro")
elif velocidades4 <= 60 or velocidades4 >= 120:
    print(f"La quinta velocidad esta por fuera del limite permitido")

print(ListaDeVelocidades)
print(promedio_de_velocidades)