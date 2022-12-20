import random

def opcion_piedra(player, bot):
    global puntos_jugador
    global puntos_maquina
    if player == "piedra" and bot == "tijeras":
        puntos_jugador += 1
        return "¡Has ganado!"
    elif player == "piedra" and bot == "papel":
        puntos_maquina += 1
        return "Has perdido..."
    elif player == "piedra" and bot == "piedra":
        return "Empate"

def opcion_papel(player, bot):
    global puntos_jugador
    global puntos_maquina
    if player == "papel" and bot == "piedra":
        puntos_jugador += 1
        return "¡Has ganado!"
    elif player == "papel" and bot == "tijeras":
        puntos_maquina += 1
        return "Has perdido..."
    elif player == "papel" and bot == "papel":
        return "Empate"

def opcion_tijeras(player, bot):
    global puntos_jugador
    global puntos_maquina
    if player == "tijeras" and bot == "papel":
        puntos_jugador += 1
        return "¡Has ganado!"
    elif player == "tijeras" and bot == "piedra":
        puntos_maquina += 1
        return "Has perdido..."
    elif player == "tijeras" and bot == "tijeras":
        return "Empate"


print("Escribe 'piedra', 'papel' o 'tijeras' para empezar a jugar. Si quieres salir escribe 'salir': ")
jugador = input("Elijo: ")
puntos_maquina = 0
puntos_jugador = 0


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

if puntos_jugador == puntos_maquina:
    print("Habéis empatado")
elif puntos_jugador < puntos_maquina:
    print(f"Tienes {puntos_jugador} puntos y tu rival tiene {puntos_maquina} puntos \n Lo siento, has perdido")
else:
    print(f"Tienes {puntos_jugador} puntos y tu rival tiene {puntos_maquina} puntos \n ¡Enhorabuena, has ganado!")