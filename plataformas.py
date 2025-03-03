import pygame

def crear_plataformas():
    """Devuelve una lista con las plataformas del juego."""
    return [
        pygame.Rect(50, 500, 700, 20),
        pygame.Rect(300, 400, 200, 20),
        pygame.Rect(150, 300, 200, 20),
    ]

def dibujar_plataformas(pantalla, plataformas):
    """Dibuja las plataformas en la pantalla."""
    for plataforma in plataformas:
        pygame.draw.rect(pantalla, (0, 0, 0), plataforma)
