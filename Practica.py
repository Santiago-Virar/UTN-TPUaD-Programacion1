#ACTIVIDAD 10
"""1. Simula un juego de "Piedra, Papel o Tijera" entre dos jugadores."""


jugador1 = input("Jugador 1, ingresa tu jugada (Piedra, Papel o Tijera): ").lower()
jugador2 = input("Jugador 2, ingresa tu jugada (Piedra, Papel o Tijera): ").lower()

if jugador1 == jugador2:
    print("EMPATE")
elif (jugador1 == "piedra" and jugador2 == "tijera") or \
    (jugador1 == "papel" and jugador2 == "piedra") or \
    (jugador1 == "tijera" and jugador2 == "papel"):
    print("GANA JUGADOR 1")
else:
    print("GANA JUGADOR 2")

