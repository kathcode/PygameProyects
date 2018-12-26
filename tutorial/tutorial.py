# Import the pygame library
import pygame

# Initialize the game engine
pygame.init()

# Colors
BLACK = (23, 32, 42)
WHITE = (247, 249, 249)
GREEN = (88, 214, 141)
RED = (192, 57, 43)
BLUE = (41, 128, 185)

# Dimensions
dimensions = (600, 600)
screen = pygame.display.set_mode(dimensions)

# Window title
pygame.display.set_caption("Kath learning pygame")

# Iterate until the user clicks on the close button.
close_window = False

# It is used to manage how quickly the screen is updated
clock = pygame.time.Clock()

# Select the font and size
title = pygame.font.Font(None, 30)

subtitle = pygame.font.Font(None, 25)

text = pygame.font.Font(None, 20)

def Instalation():
    # Python
    screen.blit(title.render("Instalacion", True, BLUE), [250, 10])
    screen.blit(subtitle.render("Python:", True, BLUE), [20, 60])
    screen.blit(text.render("Ingresa a la pagina www.python.org/downloads y descarga python.", True, BLACK), [40, 90])

    # Pygame
    screen.blit(subtitle.render("Pygame:", True, BLUE), [20, 130])
    screen.blit(text.render("Ingresa a la pagina www.pygame.org/wiki/GettingStarted e instala segun tu", True, BLACK), [40, 150])
    screen.blit(text.render("sistema operativo.", True, BLACK), [40, 170])

    # Arrows
    load_image = pygame.image.load('tutorial/rigth.png')
    screen.blit(load_image, (540, 540))


def InitialConfiguration():
    screen.blit(title.render("Configuracion inicial", True, BLUE), [200, 10])
    screen.blit(subtitle.render("Pantalla:", True, BLUE), [20, 60])

    screen.blit(text.render("Colores:", True, BLUE), [30, 80])
    screen.blit(text.render("se representan con colores RGBA, en rango de 0-255", True, BLACK), [90, 80])
    screen.blit(text.render("Ejemplo: BLACK = (23, 32, 42)", True, BLACK), [30, 100])

    screen.blit(text.render("Dimension de pantalla: ", True, BLUE), [30, 120])
    screen.blit(text.render("Para darle el ancho y el alto a la pantalla usa la siguiente", True, BLACK),[180, 120])
    screen.blit(text.render("funcion: pygame.display.set_mode(100, 400) que recibe como argumento el ancho y el alto.", True, BLACK), [30, 140])
    screen.blit(text.render("De este modo la pantalla quedaria con un ancho de 100 y un alto de 400.", True, BLACK), [30, 160])

    screen.blit(subtitle.render("Ciclo infinito: ", True, BLUE), [20, 180])
    screen.blit(text.render("debes de crear un ciclo infinito para que corra tu juego hasta que el", True, BLACK), [30, 200])
    screen.blit(text.render("el jugador quiera salir.", True, BLACK), [30, 220])

    screen.blit(text.render("Ejemplo: ", True, BLACK), [30, 240])
    screen.blit(text.render("mientras que la ventana no este cerrada: ", True, RED), [50, 260])
    screen.blit(text.render("se ejecutara este codigo", True, RED), [70, 280])
    screen.blit(text.render("fin mientras", True, RED), [50, 300])

    # Arrows
    load_image = pygame.image.load('tutorial/rigth.png')
    screen.blit(load_image, (540, 540))

    # Arrows
    load_image = pygame.image.load('tutorial/left.png')
    screen.blit(load_image, (5, 540))

    # Primero se debe configurar la pantalla
    # Configuracion de colores
    # Ciclo infinito


def PlantillaPantalla():
    screen.blit(title.render("Plantilla - Configuracion de la pantalla", True, BLUE), [50, 10])
    load_image = pygame.image.load('tutorial/code1.png')
    screen.blit(load_image, (40, 30))

    # Arrows
    load_image = pygame.image.load('tutorial/rigth.png')
    screen.blit(load_image, (540, 540))

    # Arrows
    load_image = pygame.image.load('tutorial/left.png')
    screen.blit(load_image, (5, 540))


def PlantillaLoop():
    screen.blit(title.render("Plantilla - Configuracion del ciclo para el codigo", True, BLUE), [50, 10])
    load_image = pygame.image.load('tutorial/code2.png')
    screen.blit(load_image, (40, 30))

    # Arrows
    load_image = pygame.image.load('tutorial/rigth.png')
    screen.blit(load_image, (540, 540))

    # Arrows
    load_image = pygame.image.load('tutorial/left.png')
    screen.blit(load_image, (5, 540))

def CreateSmallAnimation():
    screen.blit(title.render("Creando la primera animacion", True, BLUE), [170, 10])
    screen.blit(text.render("Con este codigo creamos una animacion, donde el balon rebota en la pantalla", True, BLACK), [20, 30])
    screen.blit(text.render("Solo necesitas agregar la imagen ball.gif y copiar el siguiente codigo:", True, BLACK), [20, 50])
    load_image = pygame.image.load('tutorial/code3.png')
    screen.blit(load_image, (20, 80))

    # Arrows
    load_image = pygame.image.load('tutorial/rigth.png')
    screen.blit(load_image, (540, 540))

    # Arrows
    load_image = pygame.image.load('tutorial/left.png')
    screen.blit(load_image, (5, 540))


def PresentacionVideoJuego():
    screen.blit(title.render("Creando un videojuego", True, BLUE), [170, 10])
    screen.blit(subtitle.render("Vamos a mostrar como hacer el videojuego SNAKE.", True, BLACK), [20, 60])
    load_image = pygame.image.load('tutorial/snake.png')
    screen.blit(load_image, (20, 90))

    # Arrows
    load_image = pygame.image.load('tutorial/rigth.png')
    screen.blit(load_image, (540, 540))

    # Arrows
    load_image = pygame.image.load('tutorial/left.png')
    screen.blit(load_image, (5, 540))


def VideojuegoPaso1():
    screen.blit(title.render("Configuracion inicial del juego", True, BLUE), [170, 10])
    screen.blit(text.render("Pantalla, dimesiones de la culebra y del espacio", True, BLACK), [20, 30])
    load_image = pygame.image.load('tutorial/1.png')
    screen.blit(load_image, (20, 45))

    # Arrows
    load_image = pygame.image.load('tutorial/rigth.png')
    screen.blit(load_image, (540, 540))

    # Arrows
    load_image = pygame.image.load('tutorial/left.png')
    screen.blit(load_image, (5, 540))


def VideojuegoPaso2():
    screen.blit(title.render("Creando la caja", True, BLUE), [170, 10])
    screen.blit(text.render("Con esta funcion vamos a dibujar la caja (culebra).", True, BLACK), [20, 50])
    load_image = pygame.image.load('tutorial/2.png')
    screen.blit(load_image, (20, 90))

    # Arrows
    load_image = pygame.image.load('tutorial/rigth.png')
    screen.blit(load_image, (540, 540))

    # Arrows
    load_image = pygame.image.load('tutorial/left.png')
    screen.blit(load_image, (5, 540))


def VideojuegoPaso3():
    screen.blit(title.render("Clase snake", True, BLUE), [170, 10])
    screen.blit(text.render("En esta clase se crearan varios metodos como la posicion, los puntos,", True, BLACK), [20, 40])
    screen.blit(text.render("el movimiento y que pasa cuando pierde.", True, BLACK), [20, 60])
    load_image = pygame.image.load('tutorial/3.png')
    screen.blit(load_image, (10, 90))

    # Arrows
    load_image = pygame.image.load('tutorial/rigth.png')
    screen.blit(load_image, (540, 540))

    # Arrows
    load_image = pygame.image.load('tutorial/left.png')
    screen.blit(load_image, (5, 540))


def VideoJuegoPaso4():
    screen.blit(title.render("Creemos la manzana para la culebra", True, BLUE), [130, 10])
    screen.blit(text.render("Se agrega una posicion aleatoria a la comida y luego se pinta", True, BLACK), [40, 40])
    load_image = pygame.image.load('tutorial/4.png')
    screen.blit(load_image, (40, 90))

    # Arrows
    load_image = pygame.image.load('tutorial/rigth.png')
    screen.blit(load_image, (540, 540))

    # Arrows
    load_image = pygame.image.load('tutorial/left.png')
    screen.blit(load_image, (5, 540))


def VideoJuegoPaso5():
    screen.blit(title.render("Verificar si la culebra ha comido", True, BLUE), [130, 10])
    screen.blit(text.render("Se verifica si la posicion de la cabeza de la culebra es la misma que la de la manzana", True, BLACK), [40, 40])
    load_image = pygame.image.load('tutorial/5.png')
    screen.blit(load_image, (40, 90))

    # Arrows
    load_image = pygame.image.load('tutorial/rigth.png')
    screen.blit(load_image, (540, 540))

    # Arrows
    load_image = pygame.image.load('tutorial/left.png')
    screen.blit(load_image, (5, 540))


def VideoJuegoPaso6():
    screen.blit(title.render("Ciclo infinito para ejecutar el codigo", True, GREEN), [130, 10])
    screen.blit(text.render("En este ciclo se corre el juego", True, BLACK), [40, 40])
    load_image = pygame.image.load('tutorial/6.png')
    screen.blit(load_image, (40, 90))

    # Arrows
    load_image = pygame.image.load('tutorial/rigth.png')
    screen.blit(load_image, (540, 540))

    # Arrows
    load_image = pygame.image.load('tutorial/left.png')
    screen.blit(load_image, (5, 540))


varx = False

steps = {
    1: Instalation,
    2: InitialConfiguration,
    3: PlantillaPantalla,
    4: PlantillaLoop,
    5: CreateSmallAnimation,
    6: PresentacionVideoJuego,
    7: VideojuegoPaso1,
    8: VideojuegoPaso2,
    9: VideojuegoPaso3,
    10: VideoJuegoPaso4,
    11: VideoJuegoPaso5,
    12: VideoJuegoPaso6,
}

step = 1

# ---------- Main Loop of the Program ----------
while not close_window:
    actual_step = steps[step]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window = True

        if event.type == pygame.KEYDOWN and varx:
            varx = False

        if event.type == pygame.KEYDOWN and not varx:
            varx = True

            if event.key == pygame.K_RIGHT:
                step = step + 1

            if event.key == pygame.K_LEFT:
                step = step - 1

    # Cleare the screen
    screen.fill(WHITE)

    actual_step()


    # Initial configuration
        # Screen
        # Infinit loop
        # Display
        # Quit

    # Create a small animation

    # Create snake game


    # Update the screen
    pygame.display.flip()

    # Limited to 20 frames per second
    clock.tick(20)

# Close the program
pygame.quit()


