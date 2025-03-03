import pygame
import os

def cargar_imagen(ruta, tamaño):
    """Carga y redimensiona una imagen."""
    imagen = pygame.image.load(os.path.join("assets", "images", ruta)).convert_alpha()
    return pygame.transform.scale(imagen, tamaño)

def centrar_texto(texto, fuente, superficie, y, color=(255, 255, 255)):
    """Renderiza un texto centrado en la pantalla."""
    texto_renderizado = fuente.render(texto, True, color)
    rect_texto = texto_renderizado.get_rect(center=(superficie.get_width() // 2, y))
    superficie.blit(texto_renderizado, rect_texto)
