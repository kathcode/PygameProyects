# -*- coding: utf-8 -*-

# Import the pygame library
import pygame
import os
import random

# Initialize the game engine
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (102, 255, 204)
RED = (255, 80, 80)
BLUE = (0, 153, 255)

# Dimensions
dimensions = (700, 500)
screen = pygame.display.set_mode(dimensions)

# Window title
pygame.display.set_caption("Comprendiendo las estructuras algorístmicas")

# Iterate until the user clicks on the close button.
close_window = False

# It is used to manage how quickly the screen is updated
clock = pygame.time.Clock()

# Select the font and size
font = pygame.font.Font(None, 25)

point_x_1 = [20, 20]
point_x_2 = [20, 120]
point_x_3 = [120, 120]
point_x_4 = [120, 20]

point_y_1 = [20, 120]
point_y_2 = [20, 220]
point_y_3 = [120, 220]
point_y_4 = [120, 120]

itemList2x2 = {
    2: [
        {'id': 1, 'type': 'dog', 'position': [20, 20], 'range': [[20, 120], [20, 120]], 'show': False, 'image': 'parejas/dog.jpg'},
        {'id': 2, 'type': 'cat', 'position': [120, 20], 'range': [[120, 220], [20, 120]], 'show': False, 'image': 'parejas/cat.jpg'},
        {'id': 3, 'type': 'dog', 'position': [20, 120], 'range': [[20, 120], [120, 220]], 'show': False, 'image': 'parejas/dog.jpg'},
        {'id': 4, 'type': 'cat', 'position': [120, 120], 'range': [[120, 220], [120, 220]], 'show': False, 'image': 'parejas/cat.jpg'},
    ],
    3: [
        {'id': 1, 'type': 'dog', 'position': [20, 20], 'range': [[20, 120], [20, 120]], 'show': False, 'image': 'parejas/dog.jpg'},
        {'id': 2, 'type': 'cat', 'position': [120, 20], 'range': [[120, 220], [20, 120]], 'show': False, 'image': 'parejas/cat.jpg'},
        {'id': 3, 'type': 'dog', 'position': [220, 20], 'range': [[220, 320], [20, 120]], 'show': False, 'image': 'parejas/dog.jpg'},
        {'id': 4, 'type': 'birt', 'position': [20, 120], 'range': [[20, 120], [120, 220]], 'show': False, 'image': 'parejas/birt.jpg'},
        {'id': 5, 'type': 'cat', 'position': [120, 120], 'range': [[120, 220], [120, 220]], 'show': False, 'image': 'parejas/cat.jpg'},
        {'id': 7, 'type': 'birt', 'position': [220, 120], 'range': [[220, 320], [120, 220]], 'show': False, 'image': 'parejas/birt.jpg'},
    ],
    4: [
        {'id': 1, 'type': 'dog', 'position': [20, 20], 'range': [[20, 120], [20, 120]], 'show': False, 'image': 'parejas/dog.jpg'},
        {'id': 2, 'type': 'cat', 'position': [120, 20], 'range': [[120, 220], [20, 120]], 'show': False, 'image': 'parejas/cat.jpg'},
        {'id': 3, 'type': 'dog', 'position': [220, 20], 'range': [[220, 320], [20, 120]], 'show': False, 'image': 'parejas/dog.jpg'},
        {'id': 4, 'type': 'cat', 'position': [320, 20], 'range': [[320, 420], [20, 120]], 'show': False, 'image': 'parejas/cat.jpg'},
        {'id': 5, 'type': 'birt', 'position': [20, 120], 'range': [[20, 120], [120, 220]], 'show': False, 'image': 'parejas/birt.jpg'},
        {'id': 6, 'type': 'horse', 'position': [120, 120], 'range': [[120, 220], [120, 220]], 'show': False, 'image': 'parejas/horse.jpg'},
        {'id': 7, 'type': 'birt', 'position': [220, 120], 'range': [[220, 320], [120, 220]], 'show': False, 'image': 'parejas/birt.jpg'},
        {'id': 8, 'type': 'horse', 'position': [320, 120], 'range': [[320, 420], [120, 220]], 'show': False, 'image': 'parejas/horse.jpg'}
    ]
}

array_size_selected = 4

step = 0

matches_list = []
compare_list = []
newvariable = False

varx = False

# ---------- Main Loop of the Program ----------
while not close_window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window = True
        
    letter_pressed = ''
    if event.type == pygame.KEYDOWN and varx:
            varx = False

    if event.type == pygame.KEYDOWN and not varx:
        varx = True

        if event.key != pygame.K_DOWN and event.key != pygame.K_UP and event.key != pygame.K_LEFT and event.key != pygame.K_RIGHT:
            letter_pressed = event.unicode

    # Cleare the screen
    screen.fill(WHITE)

    if step == 0:
        reset = font.render("Por favor seleccione un tamano para la matriz presionando la tecla", True, BLACK)
        screen.blit(reset, [100, 100])

        reset = font.render("a) 2x2", True, BLACK)
        screen.blit(reset, [100, 120])

        reset = font.render("b) 2x3", True, BLACK)
        screen.blit(reset, [100, 140])

        reset = font.render("c) 2x4", True, BLACK)
        screen.blit(reset, [100, 160])

        if letter_pressed == 'a':
            array_size_selected = 2

        if letter_pressed == 'b':
            array_size_selected = 3

        if letter_pressed == 'c':
            array_size_selected = 4

        if letter_pressed in ('a', 'b', 'c'):
            step = 1

    itemsList = itemList2x2[array_size_selected]

    if step == 1:
        reset = font.render("Reinicia con la tecla C", True, RED)
        screen.blit(reset, [500, 480])

        score = font.render('Numero de parejas:', True, BLACK)
        text = font.render(str(len(matches_list)), True, BLUE)
        screen.blit(text, [650, 100])
        screen.blit(score, [430, 100])
        
        score = font.render("0", True, BLACK)
        screen.blit(score, [3, 60])

        score = font.render("1", True, BLACK)
        screen.blit(score, [3, 160])

        score = font.render("0", True, BLACK)
        screen.blit(score, [60, 3])

        score = font.render("1", True, BLACK)
        screen.blit(score, [160, 3])

        if array_size_selected == 3 or array_size_selected == 4:
            score = font.render("2", True, BLACK)
            screen.blit(score, [260, 3])

        if array_size_selected == 4:
            score = font.render("3", True, BLACK)
            screen.blit(score, [360, 3])

        score = font.render("Si (", True, BLACK)
        screen.blit(score, [60, 300])

        score = font.render("Si (", True, BLACK)
        screen.blit(score, [60, 300])

        # Show the image to compare 1
        if len(compare_list) >= 1:
            score = font.render(compare_list[0].get('type'), True, BLUE)
            screen.blit(score, [100, 300])

        score = font.render(" = ", True, BLACK)
        screen.blit(score, [160, 300])

        # Show the image to compare 2
        if len(compare_list) >= 2:
            score = font.render(compare_list[1].get('type'), True, BLUE)
            screen.blit(score, [200, 300])

        score = font.render(") entonces", True, BLACK)
        screen.blit(score, [250, 300])

        # Show the images selected
        for item in itemsList:
            if item.get('show'):
                load_image = pygame.image.load(item.get('image'))
                image = pygame.transform.scale(load_image, (100, 100))
                rect_y = image.get_rect()
                rect_y = rect_y.move(item.get('position')[0], item.get('position')[1])
                screen.blit(image, rect_y)

        # Show the conditional in the screen
        score = font.render("Tienes una pareja", True, BLACK)
        screen.blit(score, [100, 340])

        score = font.render("Si no", True, BLACK)
        screen.blit(score, [60, 380])

        score = font.render("No son pareja", True, BLACK)
        screen.blit(score, [100, 430])

        score = font.render("Finsi", True, BLACK)
        screen.blit(score, [60, 470])

        # Draw the grid
        for point in range(array_size_selected):
            score = font.render(str(point), True, BLACK)
            # X - box
            points_x = [
                [point_x_1[0] + (point * 100), point_x_1[1]],
                [point_x_2[0] + (point * 100), point_x_2[1]],
                [point_x_3[0] + (point * 100), point_x_3[1]],
                [point_x_4[0] + (point * 100), point_x_4[1]]
            ]
            pygame.draw.polygon(screen, BLACK, points_x, 1)

            # Y - box
            points_y = [
                [point_y_1[0] + (point * 100), point_y_1[1]],
                [point_y_2[0] + (point * 100), point_y_2[1]],
                [point_y_3[0] + (point * 100), point_y_3[1]],
                [point_y_4[0] + (point * 100), point_y_4[1]]
            ]

            pygame.draw.polygon(screen, BLACK, points_y, 1)

        x = []
        y = []

    # Botton not pressed
    if event.type == pygame.MOUSEBUTTONUP and newvariable:
        newvariable = False

    # Botton pressed
    if event.type == pygame.MOUSEBUTTONDOWN and not newvariable:
        newvariable = True

        position_clicked = pygame.mouse.get_pos()
        x = position_clicked[0]
        y = position_clicked[1]

        for it in itemsList:
            # Get the box position
            if (it.get('range')[0][0] <= x <= it.get('range')[0][1]) and (it.get('range')[1][0] <= y <= it.get('range')[1][1]):
                compare_list.append({'type': it.get('type'), 'id': it.get('id')})
                it['show'] = True

                if len(compare_list) == 3:

                    if compare_list[0].get('type') == compare_list[1].get('type'):
                        if compare_list[0].get('id') != compare_list[1].get('id'):
                            # Add the text with the match
                            text = font.render("This is a match", True, RED)
                            screen.blit(text, [400, 400])
                            # Adding the match for the list of matches
                            matches_list.append({'type': it.get('type'), 'id': it.get('id')})
                            # Hide the last
                            it['show'] = False
                            # Reset the list
                            compare_list = []
                    else:
                        # Hide the last
                        it['show'] = False
                        # Hide the second item
                        itemsList[compare_list[1].get('id') - 1]['show'] = False
                        # Remove the last two items
                        del compare_list[2]
                        del compare_list[1]

    # Update the screen
    pygame.display.flip()

    # Limited to 15 frames per second
    clock.tick(15)
# Close the program
pygame.quit()
''