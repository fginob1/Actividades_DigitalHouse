import random

numero_secreto = random.randint(1,101)
adivinado = False
intentos = 0
max_intentos = 5
print("Bienvenido al juego")
while not adivinado:
    if intentos > max_intentos:
        print("Perdiste, eran 5 intentos")
        break
    numero = input("Introduce un numero del 1 al 100: ")
    numero = int(numero)
    intentos += 1
    if numero == numero_secreto:
        print("Ganaste!")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero es mayor")
    else:
        print("El numero es menor")

        