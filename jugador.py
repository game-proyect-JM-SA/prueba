import pygame
import os

class Jugador:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.vel_x = 5
        self.vel_y = 0
        self.gravedad = 1
        self.en_suelo = False
        ruta_imagen = os.path.join("assets", "images", "metal_slug.png")
        self.imagen = pygame.image.load(ruta_imagen).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (50, 50))

    def mover(self, teclas, offset_x):
        if teclas[pygame.K_LEFT]:
            offset_x -= self.vel_x
        if teclas[pygame.K_RIGHT]:
            offset_x += self.vel_x
        return offset_x

    def saltar(self, teclas):
        if teclas[pygame.K_SPACE] and self.en_suelo:
            self.vel_y = -15
            self.en_suelo = False

    def aplicar_gravedad(self):
        self.vel_y += self.gravedad
        self.rect.y += self.vel_y

    def colision_con_plataformas(self, plataformas, offset_x):
        self.en_suelo = False
        for plataforma in plataformas:
            plataforma_desplazada = plataforma.move(-offset_x, 0)
            if self.rect.colliderect(plataforma_desplazada) and self.vel_y > 0:
                self.rect.y = plataforma_desplazada.y - self.rect.height
                self.vel_y = 0
                self.en_suelo = True

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect.topleft)
        
    def return_menu(self, teclas):
        if teclas[pygame.K_ESCAPE]:
            return True
        return False
    
  
