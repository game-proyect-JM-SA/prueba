import pygame
from config import boton_jugar, boton_salir, fuente, BLANCO, NEGRO
from utils import centrar_texto

def manejar_eventos_menu(evento, estado):
    """Maneja los eventos en el menú."""
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if boton_jugar.collidepoint(evento.pos):
            return 1  # JUEGO
        elif boton_salir.collidepoint(evento.pos):
            pygame.quit()
            exit()
    return estado

def dibujar_menu(pantalla):
    """Dibuja el menú en la pantalla."""
    pantalla.fill(NEGRO)
    centrar_texto("Juego de Plataforma", fuente, pantalla, 150)
    pygame.draw.rect(pantalla, NEGRO, boton_jugar)
    centrar_texto("Jugar", fuente, pantalla, boton_jugar.centery)
    pygame.draw.rect(pantalla, NEGRO, boton_salir)
    centrar_texto("Salir", fuente, pantalla, boton_salir.centery)
