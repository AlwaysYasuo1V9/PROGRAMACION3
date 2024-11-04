import unittest
from laberinto import hay_camino, crear_laberinto

class TestLaberinto(unittest.TestCase):
    def setUp(self):
        self.laberinto = crear_laberinto()

    def test_hay_camino(self):
        entrada = (1, 1)
        salida = (5, 5)  # Cambia esto a una posición que se puede usar
        self.laberinto[entrada[0]][entrada[1]] = ' '
        self.laberinto[salida[0]][salida[1]] = ' '
        self.assertTrue(hay_camino(self.laberinto, entrada, salida))

if __name__ == '__main__':
    unittest.main()
