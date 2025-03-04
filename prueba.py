import pygame
import os  # Para manejar rutas de archivos

# Inicialización
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Plataforma")

# Colores
GRIS = (128, 128, 128)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Fuente para el menú
fuente = pygame.font.Font(None, 50)

# Botones del menú
boton_jugar = pygame.Rect(300, 250, 200, 50)
boton_salir = pygame.Rect(300, 350, 200, 50)

# Jugador (rectángulo)
jugador = pygame.Rect(100, 400, 50, 50)
velocidad_x = 5
gravedad = 1
velocidad_y = 0
en_suelo = False

# Cargar imagen del jugador
ruta_imagen = os.path.join("assets", "images", "metal_slug.png")  # Asegura una ruta correcta
imagen_jugador = pygame.image.load(ruta_imagen).convert_alpha()
imagen_jugador = pygame.transform.scale(imagen_jugador, (jugador.width, jugador.height))

# Plataformas
plataformas = [
    pygame.Rect(50, 500, 700, 20),
    pygame.Rect(300, 400, 200, 20),
    pygame.Rect(150, 300, 200, 20),
]

# Estados del juego
MENU = 0
JUEGO = 1
estado = MENU

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Función para centrar texto
def centrar_texto(texto, fuente, superficie, y):
    texto_renderizado = fuente.render(texto, True, BLANCO)
    rect_texto = texto_renderizado.get_rect(center=(ANCHO // 2, y))
    superficie.blit(texto_renderizado, rect_texto)

# Bucle del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if estado == MENU:
                if boton_jugar.collidepoint(evento.pos):
                    estado = JUEGO
                elif boton_salir.collidepoint(evento.pos):
                    pygame.quit()
                    exit()

    pantalla.fill(GRIS)

    if estado == MENU:
        pantalla.fill(NEGRO)
        centrar_texto("Juego de Plataforma", fuente, pantalla, 150)
        pygame.draw.rect(pantalla, BLANCO, boton_jugar)
        centrar_texto("Jugar", fuente, pantalla, boton_jugar.centery)
        pygame.draw.rect(pantalla, BLANCO, boton_salir)
        centrar_texto("Salir", fuente, pantalla, boton_salir.centery)
    elif estado == JUEGO:
        # Lógica del juego  
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            jugador.x -= velocidad_x
        if teclas[pygame.K_RIGHT]:
            jugador.x += velocidad_x
        if teclas[pygame.K_SPACE] and en_suelo:
            velocidad_y = -15
            en_suelo = False

        # Aplicar gravedad
        velocidad_y += gravedad
        jugador.y += velocidad_y

        # Colisión con plataformas
        en_suelo = False
        for plataforma in plataformas:
            if jugador.colliderect(plataforma) and velocidad_y > 0:
                jugador.y = plataforma.y - jugador.height
                velocidad_y = 0
                en_suelo = True

        # Dibujar elementos del juego
        pantalla.fill(GRIS)
        pantalla.blit(imagen_jugador, jugador.topleft)  # 🔹 Se dibuja la imagen del jugador
        for plataforma in plataformas:
            pygame.draw.rect(pantalla, NEGRO, plataforma)

    pygame.display.flip()
    clock.tick(60)
