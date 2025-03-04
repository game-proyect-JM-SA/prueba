import pygame
import os

class Enemy:
    def __init__(self, x, y,offset_x):
        self.vel_x = 0
        self.vel_y = 1
        self.x=x
        self.y=y
        self.y=self.y+self.vel_y
        self.rect = pygame.Rect(self.x-offset_x, self.y, 70, 70)
        self.gravedad = 1
        self.en_suelo = False
        ruta_imagen = os.path.join("Assets", "Images", "enemy.jpg")
        self.imagen = pygame.image.load(ruta_imagen).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (self.rect.width,self.rect.height))
        
    def aplicar_gravedad(self):
        if self.en_suelo:
            self.vel_y=0
        else:
            self.vel_y += self.gravedad
    
    def colision_con_plataformas(self, plataformas):
        self.en_suelo = False
        for plataforma in plataformas:
            if self.rect.colliderect(plataforma):
                self.en_suelo = True
    
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect.topleft)