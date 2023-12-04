import pygame
import sys
import time
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 720, 480
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Snake con Pygame')
difficulty = 9

# Colores (R, G, B)
NEGRO = pygame.Color(0, 0, 0)
BLANCO = pygame.Color(255, 255, 255)
ROJO = pygame.Color(255, 0, 0)
VERDE = pygame.Color(0, 255, 0)
AZUL = pygame.Color(0, 0, 255)

COLORES_SERPIENTE = {
    'VERDE': pygame.Color(0, 255, 0),
    'AZUL': pygame.Color(0, 0, 255),
    'ROJO': pygame.Color(255, 0, 0),
    # Agrega más colores según tus preferencias
}

color_serpiente = COLORES_SERPIENTE['VERDE']

# FPS (frames per second) controller
reloj = pygame.time.Clock()

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50]]
direccion = 'DERECHA'
cambiar_a = direccion

comida_pos = [random.randrange(1, (ANCHO // 10)) * 10, random.randrange(1, (ALTO // 10)) * 10]
comida_generada = True

puntuacion = 0
# Nueva variable para controlar el estado del juego
game_over = False

# Función de Game Over
def fin_del_juego():
    fuente_game_over = pygame.font.SysFont('times new roman', 90)
    superficie_game_over = fuente_game_over.render('Game Over', True, AZUL)
    rect_game_over = superficie_game_over.get_rect()
    rect_game_over.midtop = (ANCHO / 2, ALTO / 4)

    fuente_instrucciones = pygame.font.SysFont('times new roman', 30)
    superficie_instrucciones = fuente_instrucciones.render('Presiona la barra espaciadora para volver a jugar', True, BLANCO)
    rect_instrucciones = superficie_instrucciones.get_rect()
    rect_instrucciones.midtop = (ANCHO / 2, rect_game_over.bottom + 20)

    pantalla.fill(NEGRO)
    pantalla.blit(superficie_game_over, rect_game_over)
    pantalla.blit(superficie_instrucciones, rect_instrucciones)
    mostrar_puntuacion(1, ROJO, 'times', 20)
    pygame.display.flip()

    
    # Esperar hasta que se presione la barra espaciadora
    esperar_tecla()
    
    # Reiniciar el juego
    reiniciar_juego()

def esperar_tecla():
    esperando_tecla = True
    while esperando_tecla:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    esperando_tecla = False
                    break

# Función para reiniciar el juego
def reiniciar_juego():
    global snake_pos, snake_body, direccion, cambiar_a, comida_pos, comida_generada, puntuacion, game_over
    snake_pos = [100, 50]
    snake_body = [[100, 50]]
    direccion = 'DERECHA'
    cambiar_a = direccion
    comida_pos = [random.randrange(1, (ANCHO // 10)) * 10, random.randrange(1, (ALTO // 10)) * 10]
    comida_generada = True
    puntuacion = 0
    game_over = False


# Función para mostrar la puntuación
def mostrar_puntuacion(eleccion, color, fuente, tamaño):
    fuente_puntuacion = pygame.font.SysFont(fuente, tamaño)
    superficie_puntuacion = fuente_puntuacion.render('Puntuación: ' + str(puntuacion), True, color)
    rect_puntuacion = superficie_puntuacion.get_rect()
    if eleccion == 1:
        rect_puntuacion.midtop = (ANCHO / 10, 15)
    else:
        rect_puntuacion.midtop = (ANCHO / 2, ALTO / 1.25)
    pantalla.blit(superficie_puntuacion, rect_puntuacion)

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP or evento.key == ord('w'):
                cambiar_a = 'ARRIBA'
            if evento.key == pygame.K_DOWN or evento.key == ord('s'):
                cambiar_a = 'ABAJO'
            if evento.key == pygame.K_LEFT or evento.key == ord('a'):
                cambiar_a = 'IZQUIERDA'
            if evento.key == pygame.K_RIGHT or evento.key == ord('d'):
                cambiar_a = 'DERECHA'
            if evento.key == pygame.K_1:
                color_serpiente = COLORES_SERPIENTE['VERDE']
            elif evento.key == pygame.K_2:
                color_serpiente = COLORES_SERPIENTE['AZUL']
            elif evento.key == pygame.K_3:
                color_serpiente = COLORES_SERPIENTE['ROJO']
            if evento.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Cambiar dirección según la entrada del usuario
    if cambiar_a == 'ARRIBA' and direccion != 'ABAJO':
        direccion = 'ARRIBA'
    if cambiar_a == 'ABAJO' and direccion != 'ARRIBA':
        direccion = 'ABAJO'
    if cambiar_a == 'IZQUIERDA' and direccion != 'DERECHA':
        direccion = 'IZQUIERDA'
    if cambiar_a == 'DERECHA' and direccion != 'IZQUIERDA':
        direccion = 'DERECHA'

    # Mover la serpiente en la dirección actual
    if direccion == 'ARRIBA':
        snake_pos[1] -= 10
    if direccion == 'ABAJO':
        snake_pos[1] += 10
    if direccion == 'IZQUIERDA':
        snake_pos[0] -= 10
    if direccion == 'DERECHA':
        snake_pos[0] += 10

    particulas = pygame.sprite.Group()

    # Lógica de colisiones con la comida
    if snake_pos[0] == comida_pos[0] and snake_pos[1] == comida_pos[1]:
        puntuacion += 1
        comida_generada = False

    else:
        snake_body.insert(0, list(snake_pos))
        if len(snake_body) > puntuacion:
            snake_body.pop()

    # Generar nueva comida si se ha comido la actual
    if not comida_generada:
        comida_pos = [random.randrange(1, (ANCHO // 10)) * 10, random.randrange(1, (ALTO // 10)) * 10]
        comida_generada = True

    # Verificar colisiones con la pared o con uno mismo
    if (
        snake_pos[0] < 0
        or snake_pos[0] >= ANCHO
        or snake_pos[1] < 0
        or snake_pos[1] >= ALTO
        or snake_pos in snake_body[1:]
    ):
        fin_del_juego()

    # Dibujar en la pantalla
    pantalla.fill(NEGRO)
    for segmento in snake_body:
        pygame.draw.rect(pantalla, color_serpiente, (segmento[0], segmento[1], 10, 10))
    pygame.draw.rect(pantalla, ROJO, (comida_pos[0], comida_pos[1], 10, 10))

    # Mostrar puntuación
    mostrar_puntuacion(0, BLANCO, 'times', 20)

    pygame.display.flip()

    # Control de la velocidad del juego
    reloj.tick(difficulty)
