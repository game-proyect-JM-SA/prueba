import pygame
import os

# Inicialización
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Plataforma")

# Colores
GRIS = (128, 128, 128)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)

# Cargar imagen del jugador
ruta_imagen = os.path.join("assets", "images", "metal_slug.png")
imagen_jugador = pygame.image.load(ruta_imagen).convert_alpha()
imagen_jugador = pygame.transform.scale(imagen_jugador, (50, 50))

# Jugador
jugador = pygame.Rect(ANCHO // 2, 400, 50, 50)  # Siempre en el centro
velocidad_x = 5
gravedad = 1
velocidad_y = 0
en_suelo = False

# Offset para el desplazamiento del mundo
offset_x = 0  # 🔹 Desplazamiento del mapa

# Plataformas (extendiéndose más allá del ancho de la pantalla)
plataformas = [
    pygame.Rect(50, 500, 700, 20),
    pygame.Rect(300, 400, 200, 20),
    pygame.Rect(150, 300, 200, 20),
    pygame.Rect(900, 500, 300, 20),  # 🔹 Plataforma fuera de la pantalla
    pygame.Rect(1300, 400, 200, 20),  # 🔹 Plataforma aún más lejos
]

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Bucle del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Lógica del juego  
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT]:
        offset_x -= velocidad_x  # 🔹 Mover el mundo a la derecha (jugador va a la izquierda)
    
    if teclas[pygame.K_RIGHT]:
        offset_x += velocidad_x  # 🔹 Mover el mundo a la izquierda (jugador avanza a la derecha)

    if teclas[pygame.K_SPACE] and en_suelo:
        velocidad_y = -15
        en_suelo = False

    # Aplicar gravedad
    velocidad_y += gravedad
    jugador.y += velocidad_y

    # Colisión con plataformas
    en_suelo = False
    for plataforma in plataformas:
        plataforma_desplazada = plataforma.move(-offset_x, 0)  # 🔹 Ajustamos la posición con el offset
        if jugador.colliderect(plataforma_desplazada) and velocidad_y > 0:
            jugador.y = plataforma_desplazada.y - jugador.height
            velocidad_y = 0
            en_suelo = True

    # Dibujar elementos del juego
    pantalla.fill(GRIS)

    # Dibujar jugador (siempre en el centro)
    pantalla.blit(imagen_jugador, jugador.topleft)

    # Dibujar plataformas con desplazamiento
    for plataforma in plataformas:
        plataforma_desplazada = plataforma.move(-offset_x, 0)  # 🔹 Ajustamos la posición
        pygame.draw.rect(pantalla, NEGRO, plataforma_desplazada)

    pygame.display.flip()
    clock.tick(60)
