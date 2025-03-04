import pygame
from config import NEGRO
def create_insolated_platform():
    return  pygame.Rect(-100, 600, 2000, 1)
    
def crear_plataformas():
    return [
        pygame.Rect(50, 500, 700, 20),
        pygame.Rect(300, 400, 200, 20),
        pygame.Rect(150, 300, 200, 20),
        pygame.Rect(900, 500, 300, 20),
        pygame.Rect(1300, 400, 200, 20),
    ]

def dibujar_plataformas(pantalla, plataformas, offset_x):
    for plataforma in plataformas:
        plataforma_desplazada = plataforma.move(-offset_x, 0)
        pygame.draw.rect(pantalla, NEGRO, plataforma_desplazada)
        
def draw_one_platform(pantalla,plataforma):
    pygame.draw.rect(pantalla, NEGRO, plataforma)

