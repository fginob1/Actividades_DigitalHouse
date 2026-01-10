nombre1 = input("Nombre jugador 1")
nombre2 = input("Nombre jugador 2")

jugador1 = input("Jugador 1, piedra papel o tijera? ")
jugador2 = input("Jugador 2, piedra papel o tijera? ")

if jugador1 == jugador2:
    print("Empate")
elif jugador1 == "piedra" and jugador2 == "tijeras" or jugador1 == "tijeras" and jugador2 == "papel" or jugador1 == "papel" and jugador2 == "piedra":
    print("Gano ", nombre1)
else:
    print("Gano ", nombre2)