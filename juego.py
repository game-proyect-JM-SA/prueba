import pygame
from config import pantalla, clock, ANCHO, ALTO, GRIS
from jugador import Jugador
from plataformas import crear_plataformas, dibujar_plataformas, create_insolated_platform, draw_one_platform
from menu import manejar_eventos_menu, dibujar_menu  # 🔹 Importamos correctamente
from config import pantalla, clock, MENU, JUEGO, GRIS
from enemy import Enemy


x=2
y=400

x_enemy=10
y_enemy=200
def reset_position(offset):
    jugador = Jugador(ANCHO // x-offset, y)
    return jugador


def ejecutar_juego():
    
    estado = MENU  # 🔹 Empezamos en el menú
    jugador = Jugador(ANCHO // x, y)
    plataformas = crear_plataformas()
    
    
    death_sone = create_insolated_platform()
    death = False
    
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
            jugador=reset_position(offset_x)
            offset_x=0
        elif estado == JUEGO:
            
            enemy = Enemy(ANCHO // x_enemy, y_enemy,offset_x)
            teclas = pygame.key.get_pressed()
            offset_x = jugador.mover(teclas, offset_x)
            jugador.saltar(teclas)
            jugador.aplicar_gravedad()
            jugador.colision_con_plataformas(plataformas, offset_x)
            
            jugador.dibujar(pantalla)
            dibujar_plataformas(pantalla, plataformas, offset_x)
            
            
            enemy.colision_con_plataformas(plataformas)
            enemy.aplicar_gravedad()
            enemy.dibujar(pantalla)

            
                
            
            draw_one_platform(pantalla, death_sone)
            death=jugador.rect.colliderect(death_sone) or jugador.rect.colliderect(enemy.rect)
            if death:
                estado=MENU 
            if jugador.return_menu(teclas):
                estado=MENU
    
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

