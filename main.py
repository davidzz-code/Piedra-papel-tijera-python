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
jugador = input()
maquina = random.choice(["piedra", "papel", "tijeras"])
puntos_jugador = 0
puntos_maquina = 0


# while jugador != "salir":
#     if jugador == "piedra":
#         print(opcion_piedra)
#     elif jugador == "papel":
#         print(opcion_papel)
#     elif jugador == "tijeras":
#         print(opcion_tijeras)
