import random

def crear_laberinto(ancho, alto):
    laberinto = [['#' for _ in range(ancho)] for _ in range(alto)]
    for x in range(1, alto - 1, 2):
        for y in range(1, ancho - 1, 2):
            laberinto[x][y] = ' '
            for _ in range(4):
                mov_x = random.choice([-1, 1]) * (random.choice([0, 1]))
                mov_y = random.choice([-1, 1]) * (random.choice([0, 1]))
                if 0 <= x + mov_x < alto and 0 <= y + mov_y < ancho:
                    laberinto[x + mov_x][y + mov_y] = ' '

    return laberinto

def agregar_entrada_salida(laberinto):
    alto = len(laberinto)
    ancho = len(laberinto[0])

    #entrada en (1, 1)
    laberinto[1][1] = 'E'

    #salida al final
    laberinto[alto - 2][ancho - 2] = 'S'

    return laberinto

def generar_laberinto(ancho, alto):
    laberinto = crear_laberinto(ancho, alto)
    laberinto = agregar_entrada_salida(laberinto)

    return laberinto

def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print(''.join(fila))
