import pygame
import sys

# Definir colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)

# Definir dimensiones
ANCHO = 800
ALTO = 400

TORRE_ANCHO = 20
TORRE_ALTO = 200

TORRE_1_X = 100
TORRE_2_X = 400
TORRE_3_X = 700
TORRE_Y = 250

# Inicializar Pygame
pygame.init()

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Torres de Hanoi")

# Fuente de texto
fuente = pygame.font.Font(None, 36)

# Función para dibujar las torres y los discos
def dibujar_torres(torres, seleccionada):
    ventana.fill(NEGRO)
    for i, torre in enumerate(torres):
        pygame.draw.rect(ventana, AZUL, [i * 300 + 90, TORRE_Y, TORRE_ANCHO, TORRE_ALTO])
        for j, disco in enumerate(torre):
            disco_ancho = 20 + disco * 20
            disco_alto = 20
            pygame.draw.rect(ventana, VERDE, [i * 300 + 90 - (disco_ancho / 2) + 10, TORRE_Y - (j * disco_alto), disco_ancho, disco_alto])
    if seleccionada is not None:
        pygame.draw.rect(ventana, AZUL, [seleccionada * 300 + 70, TORRE_Y - 10, TORRE_ANCHO + 20, TORRE_ALTO + 20])

# Función para mostrar mensajes en la ventana
def mostrar_mensaje(mensaje):
    ventana.fill(NEGRO)
    fuente_mensaje = pygame.font.Font(None, 36)  # Tamaño de fuente un poco más grande
    texto = fuente_mensaje.render(mensaje, True, BLANCO)  # Cambiar el color a blanco
    ventana.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

# Crear botones
def crear_botones():
    fuente_botones = pygame.font.Font(None, 24)
    botones = {
        "salir": {
            "rect": pygame.Rect(700, 10, 80, 30),
            "texto": fuente_botones.render("Salir", True, BLANCO),  # Cambiar el color a blanco
        },
        "instrucciones": {
            "texto": fuente_botones.render("Toca las pilas para mover un disco", True, BLANCO),  # Texto en blanco
        }
    }
    return botones

# Comprobar clic en botones
def clic_en_botones(botones, x, y):
    for nombre, boton in botones.items():
        if "rect" in boton and boton["rect"].collidepoint(x, y):
            return nombre
    return None

# Función para resolver las Torres de Hanoi
def torres_de_hanoi(n, origen, auxiliar, destino):
    if n > 0:
        torres_de_hanoi(n - 1, origen, destino, auxiliar)
        disco = torres[origen].pop()
        torres[destino].append(disco)
        dibujar_torres(torres, origen)
        pygame.display.flip()
        pygame.time.wait(500)
        torres_de_hanoi(n - 1, auxiliar, origen, destino)

# Mostrar la pregunta en la pantalla
mostrar_mensaje("¿Cuántos discos deseas jugar? (1-10): ")
n_discos = None

# Esperar a que el usuario ingrese un número válido de discos
while n_discos is None:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                if 1 <= n_discos <= 10:
                    break
                else:
                    mostrar_mensaje("Número de discos no válido. Ingresa un número entre 1 y 10: ")
            elif evento.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0]:
                n_discos = int(pygame.key.name(evento.key))
            else:
                mostrar_mensaje("Entrada no válida. Ingresa un número entre 1 y 10: ")

# Inicializar las torres con la cantidad de discos especificada
torres = [[] for _ in range(3)]
for i in range(n_discos, 0, -1):
    torres[0].append(i)

# Variables para el seguimiento de los movimientos del jugador
movimiento_origen = None
movimiento_destino = None

# Bucle principal
botones = crear_botones()

# Mostrar las instrucciones al inicio del juego
mostrar_mensaje("Toca las pilas para mover un disco")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            torre_seleccionada = (x - 90) // 300
            if clic_en_botones(botones, x, y) == "salir":
                pygame.quit()
                sys.exit()
            if movimiento_origen is None:
                if len(torres[torre_seleccionada]) > 0:
                    movimiento_origen = torre_seleccionada
            else:
                movimiento_destino = torre_seleccionada

                if (movimiento_destino is not None and
                        movimiento_origen is not None and
                        movimiento_origen != movimiento_destino):
                    origen = movimiento_origen
                    destino = movimiento_destino

                    if len(torres[origen]) > 0:
                        disco = torres[origen][-1]
                        if len(torres[destino]) == 0 or disco < torres[destino][-1]:
                            torres[origen].pop()
                            torres[destino].append(disco)
                        else:
                            mostrar_mensaje("Movimiento inválido. El disco no puede ser colocado sobre otro más pequeño.")
                    movimiento_origen = None
                    movimiento_destino = None

    dibujar_torres(torres, movimiento_origen if movimiento_origen is not None else movimiento_destino)
    pygame.display.flip()

    if len(torres[2]) == n_discos:
        mostrar_mensaje("¡Juego completado!")
