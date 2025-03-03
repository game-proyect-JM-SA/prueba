import pygame

pygame.init()  # 🔹 Asegura que pygame se inicialice antes de usar fuentes

# Configuración de pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Plataforma")

# Colores
GRIS = (128, 128, 128)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Fuente para el menú
fuente = pygame.font.Font(None, 50)  # 🔹 Ahora no fallará

# Botones del menú
boton_jugar = pygame.Rect(300, 250, 200, 50)
boton_salir = pygame.Rect(300, 350, 200, 50)

# Estados del juego
MENU = 0
JUEGO = 1

clock = pygame.time.Clock()  # 🔹 Se agregó la variable clock aquí
