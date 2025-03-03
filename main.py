import pygame  # 🔹 Importar pygame primero
pygame.init()  # 🔹 Inicializar pygame antes de importar otros módulos

from config import pantalla, clock, MENU, JUEGO, GRIS
from menu import manejar_eventos_menu, dibujar_menu
from jugador import Jugador
from plataformas import crear_plataformas, dibujar_plataformas

# Crear jugador y plataformas
jugador = Jugador(100, 400)
plataformas = crear_plataformas()

estado = MENU  # Estado inicial

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if estado == MENU:
            estado = manejar_eventos_menu(evento, estado)

    pantalla.fill(GRIS)

    if estado == MENU:
        dibujar_menu(pantalla)
    elif estado == JUEGO:
        teclas = pygame.key.get_pressed()
        jugador.mover(teclas)
        jugador.aplicar_gravedad(plataformas)

        # Dibujar elementos del juego
        pantalla.fill(GRIS)
        jugador.dibujar(pantalla)
        dibujar_plataformas(pantalla, plataformas)

    pygame.display.flip()
    clock.tick(60)
