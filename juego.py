import pygame
import sys
pygame.mixer.init()  # Inicializar el módulo de música
from config import pantalla, clock, ANCHO, ALTO, GRIS
from jugador import Jugador
from plataformas import crear_plataformas, dibujar_plataformas
from menu import manejar_eventos_menu, dibujar_menu  # 🔹 Importamos correctamente
from config import pantalla, clock, MENU, JUEGO, GRIS

def ejecutar_juego():
    estado = MENU  # 🔹 Empezamos en el menú

    try:
        pygame.mixer.music.load("assets/Music/lost-in-dreams-abstract-chill-downtempo-cinematic-future-beats-270241.mp3")
        pygame.mixer.music.play(-1)  # Reproduce música de fondo en bucle
        pygame.mixer.music.set_volume(1.0)  # Asegurarse de que el volumen esté al máximo
    except pygame.error as e:
        print("No se pudo cargar la música:", e)

    jugador = Jugador(ANCHO // 2, 400)
    plataformas = crear_plataformas()
    offset_x = 0  # Controla el desplazamiento del mundo
    ejecutando = True

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            if estado == MENU:
                estado = manejar_eventos_menu(evento, estado)

        pantalla.fill(GRIS)

        if estado == MENU:
            dibujar_menu(pantalla)
        elif estado == JUEGO:
            teclas = pygame.key.get_pressed()
            offset_x = jugador.mover(teclas, offset_x)
            jugador.saltar(teclas)
            jugador.aplicar_gravedad()
            jugador.colision_con_plataformas(plataformas, offset_x)

            jugador.dibujar(pantalla)
            dibujar_plataformas(pantalla, plataformas, offset_x)
    
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

