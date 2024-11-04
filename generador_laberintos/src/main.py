from laberinto import generar_laberinto, imprimir_laberinto

def main():
    ancho = 15  # Ancho 
    alto = 11   # Alto 

    laberinto = generar_laberinto(ancho, alto)

    # Imprimir el laberinto 
    imprimir_laberinto(laberinto)

if __name__ == "__main__":
    main()
