import random

def opcion_piedra(player, bot):
    if player == "piedra" and bot == "tijeras":
        return "¡Has ganado!"
    elif player == "piedra" and bot == "papel":
        return "Has perdido..."
    elif player == "piedra" and bot == "piedra":
        return "Empate"

def opcion_papel(player, bot):
    if player == "papel" and bot == "piedra":
        return "¡Has ganado!"
    elif player == "papel" and bot == "tijeras":
        return "Has perdido..."
    elif player == "papel" and bot == "papel":
        return "Empate"

def opcion_tijeras(player, bot):
    if player == "tijeras" and bot == "papel":
        return "¡Has ganado!"
    elif player == "tijeras" and bot == "piedra":
        return "Has perdido..."
    elif player == "tijeras" and bot == "tijeras":
        return "Empate"


print("Escribe 'piedra', 'papel' o 'tijeras' para empezar a jugar. Si quieres salir escribe 'salir': ")
jugador = input("Elijo: ")
puntos_jugador = 0
puntos_maquina = 0


while jugador != "salir":
    maquina = random.choice(["piedra", "papel", "tijeras"])
    if jugador == "piedra":
        print(f"Tu rival elige: {maquina}")
        print(opcion_piedra(jugador, maquina))
    elif jugador == "papel":
        print(f"Tu rival elige: {maquina}")
        print(opcion_papel(jugador, maquina))
    elif jugador == "tijeras":
        print(f"Tu rival elige: {maquina}")
        print(opcion_tijeras(jugador, maquina))
    jugador = input(f"Si quieres seguir jugando vuelve a probar: ")
