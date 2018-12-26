# -*- coding: utf-8 -*-

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
dimensions = (700, 500)
screen = pygame.display.set_mode(dimensions)

# Window title
pygame.display.set_caption("Titulo de la pantalla")

# Iterate until the user clicks on the close button.
close_window = False

# It is used to manage how quickly the screen is updated
clock = pygame.time.Clock()

# Select the font and size
title = pygame.font.Font(None, 30)

subtitle = pygame.font.Font(None, 25)

text = pygame.font.Font(None, 20)

letter = ['', '', '']
letter_corrects = ['a', 'b', 'b']
number_corrects = 0

def pregunta1():
    # Pregunta 1
    screen.blit(text.render("1- Segun la matriz del juego #1, diga en que posiciones se encuentran las dos imagenes de perro.", True, BLACK), [20, 60])
    load_image = pygame.image.load('test/dog.png')
    screen.blit(load_image, (40, 90))

    screen.blit(text.render("a). [0, 0] / [2, 0]", True, BLACK), [40, 330])
    screen.blit(text.render("b). [10, 7] / [0, 0]", True, BLACK), [40, 350])
    screen.blit(text.render("c). [0, 100] / [1, 2]", True, BLACK), [40, 370])

    screen.blit(title.render("Escribe la letra de la respuesta: ", True, BLACK), [40, 420])
    screen.blit(title.render(str(letter[0]), True, GREEN), [400, 420])


def pregunta2():
    screen.blit(text.render("2- ¿Cual seria la respuesta del videojuego al tener el siguiente condicional?", True, BLACK),[20, 60])
    load_image = pygame.image.load('test/conditional.png')
    screen.blit(load_image, (40, 90))

    screen.blit(text.render("a). No tienes pareja", True, BLACK), [40, 330])
    screen.blit(text.render("b). Tienes una pareja", True, BLACK), [40, 350])
    screen.blit(text.render("c). Error", True, BLACK), [40, 370])

    screen.blit(title.render("Escribe la letra de la respuesta: ", True, BLACK), [40, 420])
    screen.blit(title.render(str(letter[1]), True, GREEN), [400, 420])


def pregunta3():
    screen.blit(text.render("3- Si tengo el vector:", True, BLACK),[20, 60])
    load_image = pygame.image.load('test/vec.png')
    screen.blit(load_image, (40, 90))
    screen.blit(text.render("y quiero obtener la letra [i] ¿ Cual deberia de ser la posicion?", True, BLACK), [20, 130])


    screen.blit(text.render("a). vector_prueba[10]", True, BLACK), [40, 160])
    screen.blit(text.render("b). vector_prueba[3]", True, BLACK), [40, 180])
    screen.blit(text.render("c). vector_prueba[4]", True, BLACK), [40, 200])

    screen.blit(title.render("Escribe la letra de la respuesta: ", True, BLACK), [40, 420])
    screen.blit(title.render(str(letter[2]), True, GREEN), [400, 420])


def respuesta():
    screen.blit(text.render("Resultados", True, BLACK), [20, 60])
    screen.blit(text.render("Respuestas seleccionadas:", True, BLACK), [40, 200])
    screen.blit(text.render("1) " + str(letter[0]), True, BLACK), [40, 220])
    screen.blit(text.render("2) " + str(letter[1]), True, BLACK), [40, 240])
    screen.blit(text.render("3) " + str(letter[2]), True, BLACK), [40, 260])

    screen.blit(text.render("Respuestas correctas:", True, BLACK), [40, 280])
    screen.blit(text.render("1) " + str(letter_corrects[0]), True, BLACK), [40, 300])
    screen.blit(text.render("2) " + str(letter_corrects[1]), True, BLACK), [40, 320])
    screen.blit(text.render("3) " + str(letter_corrects[2]), True, BLACK), [40, 340])

    screen.blit(text.render("Numero de respuestas correctas:", True, GREEN), [40, 360])
    screen.blit(text.render(str(number_corrects) + " de 3", True, BLACK), [300, 360])

    screen.blit(title.render("Resultado: ", True, BLACK), [300, 380])

    if number_corrects >= 2:
        screen.blit(title.render("Pasaste el test!!", True, GREEN), [410, 380])
    else:
        screen.blit(title.render("Perdiste el test!!", True, RED), [410, 380])

steps = {
    1: pregunta1,
    2: pregunta2,
    3: pregunta3,
    4: respuesta,
}

step = 1

varx = False

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

            if event.key != pygame.K_DOWN and event.key != pygame.K_UP and event.key != pygame.K_LEFT and event.key != pygame.K_RIGHT:
                if step == 1:
                    letter[0] = event.unicode
                    if letter[0] == letter_corrects[0]:
                        number_corrects = number_corrects + 1

                if step == 2:
                    letter[1] = event.unicode
                    if letter[1] == letter_corrects[1]:
                        number_corrects = number_corrects + 1

                if step == 3:
                    letter[2] = event.unicode
                    if letter[2] == letter_corrects[2]:
                        number_corrects = number_corrects + 1

                print letter

    # Cleare the screen
    screen.fill(WHITE)

    # Here goes the code
    screen.blit(title.render("Prueba de conceptos", True, BLUE), [240, 10])
    screen.blit(subtitle.render("Matrices, vectores, ciclos", True, GREEN), [240, 30])

    actual_step()

    pygame.display.flip()

    # Limited to 20 frames per second
    clock.tick(20)

# Close the program
pygame.quit()
