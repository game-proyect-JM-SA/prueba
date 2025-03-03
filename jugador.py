import pygame
from utils import cargar_imagen

class Jugador:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.velocidad_x = 5
        self.velocidad_y = 0
        self.gravedad = 1
        self.en_suelo = False
        self.imagen = cargar_imagen("metal_slug.png", (50, 50))

    def mover(self, teclas):
        """Mueve al jugador según las teclas presionadas."""
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad_x
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad_x
        if teclas[pygame.K_SPACE] and self.en_suelo:
            self.velocidad_y = -15
            self.en_suelo = False

    def aplicar_gravedad(self, plataformas):
        """Aplica la gravedad y maneja colisiones con plataformas."""
        self.velocidad_y += self.gravedad
        self.rect.y += self.velocidad_y
        self.en_suelo = False

        for plataforma in plataformas:
            if self.rect.colliderect(plataforma) and self.velocidad_y > 0:
                self.rect.y = plataforma.y - self.rect.height
                self.velocidad_y = 0
                self.en_suelo = True

    def dibujar(self, pantalla):
        """Dibuja al jugador en la pantalla."""
        pantalla.blit(self.imagen, self.rect.topleft)
