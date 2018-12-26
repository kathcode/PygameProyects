# Import the pygame library
import pygame

# Initialize the game engine
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (102, 255, 204)
RED = (255, 80, 80)
BLUE = (0, 153, 255)

# Dimensions
dimensions = (1100, 500)
screen = pygame.display.set_mode(dimensions)

# Window title
pygame.display.set_caption("kath")

# Iterate until the user clicks on the close button.
close_window = False

# It is used to manage how quickly the screen is updated
clock = pygame.time.Clock()

# Select the font and size
font = pygame.font.Font(None, 25)
font_small = pygame.font.Font(None, 20)
font_middle = pygame.font.Font(None, 40)
font_big = pygame.font.Font(None, 70)

# Global Variables
current_vector = [] # name, index inside the vector, vector
words_list = ['wifi', 'fabrica', 'celular', 'ciencia', 'digital', 'robot']
complete_list = ['', '', '', '', '', '']
vectorList = [{'vec': ['', '', '', ''], 'full': False},
            {'vec': ['', '', '', '', '', '', ''], 'full': False},
            {'vec': ['', '', '', '', '', '', ''], 'full': False},
            {'vec': ['', '', '', '', '', '', ''], 'full': False},
            {'vec': ['', '', '', '', '', '', ''], 'full': False},
            {'vec': ['', '', '', '', '', ''], 'full': False}]

actual_position = [[200, 30], [250, 30], [250, 80], [200, 80]]

letter_pressed = ''

vector1_coordinates = [
    [[200, 30], [250, 30], [250, 80], [200, 80]],
    [[200, 80], [250, 80], [250, 130], [200, 130]],
    [[200, 130], [250, 130], [250, 180], [200, 180]],
    [[200, 180], [250, 180], [250, 230], [200, 230]],
]

vector2_coordinates = [
    [[200, 130], [250, 130], [250, 180], [200, 180]],
    [[250, 130], [300, 130], [300, 180], [250, 180]],
    [[300, 130], [350, 130], [350, 180], [300, 180]],
    [[350, 130], [400, 130], [400, 180], [350, 180]],
    [[400, 130], [450, 130], [450, 180], [400, 180]],
    [[450, 130], [500, 130], [500, 180], [450, 180]],
    [[500, 130], [550, 130], [550, 180], [500, 180]],
]

vector3_coordinates = [
    [[450, 130], [500, 130], [500, 180], [450, 180]],
    [[450, 180], [500, 180], [500, 230], [450, 230]],
    [[450, 230], [500, 230], [500, 280], [450, 280]],
    [[450, 280], [500, 280], [500, 330], [450, 330]],
    [[450, 330], [500, 330], [500, 380], [450, 380]],
    [[450, 380], [500, 380], [500, 430], [450, 430]],
    [[450, 430], [500, 430], [500, 480], [450, 480]]
]


vector4_coordinates = [
    [[350, 180], [400, 180], [400, 230], [350, 230]],
    [[400, 180], [450, 180], [450, 230], [400, 230]],
    [[450, 180], [500, 180], [500, 230], [450, 230]],
    [[500, 180], [550, 180], [550, 230], [500, 230]],
    [[550, 180], [600, 180], [600, 230], [550, 230]],
    [[600, 180], [650, 180], [650, 230], [600, 230]],
    [[650, 180], [700, 180], [700, 230], [650, 230]],
]

vector5_coordinates = [
    [[200, 380], [250, 380], [250, 430], [200, 430]],
    [[250, 380], [300, 380], [300, 430], [250, 430]],
    [[300, 380], [350, 380], [350, 430], [300, 430]],
    [[350, 380], [400, 380], [400, 430], [350, 430]],
    [[400, 380], [450, 380], [450, 430], [400, 430]],
    [[450, 380], [500, 380], [500, 430], [450, 430]],
    [[500, 380], [550, 380], [550, 430], [500, 430]]
]

vector6_coordinates = [
    [[450, 430], [500, 430], [500, 480], [450, 480]],
    [[500, 430], [550, 430], [550, 480], [500, 480]],
    [[550, 430], [600, 430], [600, 480], [550, 480]],
    [[600, 430], [650, 430], [650, 480], [600, 480]],
    [[650, 430], [700, 430], [700, 480], [650, 480]],
]

vector_complete = [
    [[10, 20], [60, 20], [60, 70], [10, 70]],
    [[10, 70], [60, 70], [60, 120], [10, 120]],
    [[10, 120], [60, 120], [60, 170], [10, 170]],
    [[10, 170], [60, 170], [60, 220], [10, 220]],
    [[10, 220], [60, 220], [60, 270], [10, 270]],
    [[10, 270], [60, 270], [60, 320], [10, 320]],
]

varx = False

showCorrect = False

def draw():
    for point in vector1_coordinates:
        pygame.draw.polygon(screen, BLACK, point, 1)

    for point in vector2_coordinates:
        pygame.draw.polygon(screen, BLACK, point, 1)

    for point in vector3_coordinates:
        pygame.draw.polygon(screen, BLACK, point, 1)

    for point in vector4_coordinates:
        pygame.draw.polygon(screen, BLACK, point, 1)

    for point in vector5_coordinates:
        pygame.draw.polygon(screen, BLACK, point, 1)

    for point in vector6_coordinates:
        pygame.draw.polygon(screen, BLACK, point, 1)

    for point in vector_complete:
        pygame.draw.polygon(screen, BLACK, point, 1)


# ---------- Main Loop of the Program ----------
while not close_window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window = True

        if event.type == pygame.KEYDOWN and varx:
            varx = False

        if event.type == pygame.KEYDOWN and not varx:
            varx = True
            # Move RIGTH
            if event.key == pygame.K_RIGHT:
                point1x = actual_position[0][0] + 50
                point1y = actual_position[0][1]

                point2x = actual_position[1][0] + 50
                point2y = actual_position[1][1]

                point3x = actual_position[1][0] + 50
                point3y = actual_position[2][1]

                point4x = actual_position[1][0]
                point4y = actual_position[3][1]
                actual_position = [[point1x, point1y], [point2x, point2y], [point3x, point3y], [point4x, point4y]]
                letter_pressed = ''

            # Move LEFT
            if event.key == pygame.K_LEFT:
                point1x = actual_position[0][0] - 50
                point1y = actual_position[0][1]

                point2x = actual_position[1][0] - 50
                point2y = actual_position[1][1]

                point3x = actual_position[2][0] - 50
                point3y = actual_position[2][1]

                point4x = actual_position[3][0] - 50
                point4y = actual_position[3][1]
                actual_position = [[point1x, point1y], [point2x, point2y], [point3x, point3y], [point4x, point4y]]
                letter_pressed = ''

            # Move UP
            if event.key == pygame.K_UP:
                point1x = actual_position[0][0]
                point1y = actual_position[0][1] - 50

                point2x = actual_position[1][0]
                point2y = actual_position[1][1] - 50

                point3x = actual_position[2][0]
                point3y = actual_position[2][1] - 50

                point4x = actual_position[3][0]
                point4y = actual_position[3][1] - 50
                actual_position = [[point1x, point1y], [point2x, point2y], [point3x, point3y], [point4x, point4y]]
                letter_pressed = ''

            # Move DOWN
            if event.key == pygame.K_DOWN:
                point1x = actual_position[0][0]
                point1y = actual_position[0][1] + 50

                point2x = actual_position[1][0]
                point2y = actual_position[1][1] + 50

                point3x = actual_position[2][0]
                point3y = actual_position[2][1] + 50

                point4x = actual_position[3][0]
                point4y = actual_position[3][1] + 50
                actual_position = [[point1x, point1y], [point2x, point2y], [point3x, point3y], [point4x, point4y]]
                letter_pressed = ''


            if event.key != pygame.K_DOWN and event.key != pygame.K_UP and event.key != pygame.K_LEFT and event.key != pygame.K_RIGHT:
                letter_pressed = event.unicode

            print actual_position

            # Find the vector according to the position
            for index, vec in enumerate(vector1_coordinates):
                if vec == actual_position:
                    vectorList[0]['vec'][index] = letter_pressed
                    current_vector = ['V-1', index, 0]

            for index, vec in enumerate(vector2_coordinates):
                if vec == actual_position:
                    vectorList[1]['vec'][index] = letter_pressed
                    current_vector = ['V-2', index, 1]

            for index, vec in enumerate(vector3_coordinates):
                if vec == actual_position:
                    vectorList[2]['vec'][index] = letter_pressed
                    current_vector = ['V-3', index, 2]

            for index, vec in enumerate(vector4_coordinates):
                if vec == actual_position:
                    vectorList[3]['vec'][index] = letter_pressed
                    current_vector = ['V-4', index, 3]

            for index, vec in enumerate(vector5_coordinates):
                if vec == actual_position:
                    vectorList[4]['vec'][index] = letter_pressed
                    current_vector = ['V-5', index, 4]

            for index, vec in enumerate(vector6_coordinates):
                if vec == actual_position:
                    vectorList[5]['vec'][index] = letter_pressed
                    current_vector = ['V-6', index, 5]

    # Cleare the screen
    screen.fill(WHITE)

    draw()
    # Line to divide
    pygame.draw.line(screen, BLUE, [180, 0], [180, 500], 2)

    # Box with the current position
    pygame.draw.polygon(screen, BLUE, actual_position, 3)

    # Write the vector identifier
    text = font.render("Vectores correctos", True, BLACK)
    screen.blit(text, [2, 2])

    text = font.render("V-1", True, BLACK)
    screen.blit(text, [210, 10])

    text = font.render("V-2", True, BLACK)
    screen.blit(text, [550, 150])

    text = font.render("V-3", True, BLACK)
    screen.blit(text, [460, 110])

    text = font.render("V-4", True, BLACK)
    screen.blit(text, [300, 200])

    text = font.render("V-5", True, BLACK)
    screen.blit(text, [560, 400])

    text = font.render("V-6", True, BLACK)
    screen.blit(text, [400, 450])

    # Draw the letter pressed
    text = font_big.render(letter_pressed, True, BLACK)
    screen.blit(text, [actual_position[0][0], actual_position[0][1]])

    # Show in the vector corrects and full
    for index, list in enumerate(complete_list):
        text = font_middle.render(list, True, BLUE)
        screen.blit(text, vector_complete[index][0])

    # Show the letters in each vector
    for index, vec in enumerate(vector1_coordinates):
        letter = vectorList[0]['vec'][index]
        text = font_big.render(letter, True, BLACK)
        screen.blit(text, vec[0])

    for index, vec in enumerate(vector2_coordinates):
        letter = vectorList[1]['vec'][index]
        text = font_big.render(letter, True, BLACK)
        screen.blit(text, vec[0])

    for index, vec in enumerate(vector3_coordinates):
        letter = vectorList[2]['vec'][index]
        text = font_big.render(letter, True, BLACK)
        screen.blit(text, vec[0])

    for index, vec in enumerate(vector4_coordinates):
        letter = vectorList[3]['vec'][index]
        text = font_big.render(letter, True, BLACK)
        screen.blit(text, vec[0])

    for index, vec in enumerate(vector5_coordinates):
        letter = vectorList[4]['vec'][index]
        text = font_big.render(letter, True, BLACK)
        screen.blit(text, vec[0])

    for index, vec in enumerate(vector6_coordinates):
        letter = vectorList[5]['vec'][index]
        text = font_big.render(letter, True, BLACK)
        screen.blit(text, vec[0])


    # Verify vectors corrects
    for index, item in enumerate(vectorList):
        for vec in item['vec']:
            if vec != '':
                item['full'] = True
                vec = vec.lower()
                full_vector = ''.join(item['vec'])
                if full_vector == words_list[index]:
                    complete_list[index] = "V-" + str(index + 1)
                else:
                    complete_list[index] = ''
            else:
                item['full'] = False

    if complete_list[0] != '' and complete_list[1] != '' and complete_list[2] != '' and complete_list[3] != '' and complete_list[4] != '' and complete_list[5] != '':
        load_image = pygame.image.load('crucigrama/winner.jpg')
        image = pygame.transform.scale(load_image, (100, 200))
        screen.blit(image, (90, 300))
        text = font_middle.render("Ganaste!", True, BLACK)
        screen.blit(text, [5, 350])

    if len(current_vector) > 0:
        # Verify the work correct
        if letter_pressed == words_list[current_vector[2]][current_vector[1]]:
            showCorrect = True
        else:
            showCorrect = False

        text = font.render("si (", True, BLACK)
        screen.blit(text, [640, 20])

        tx = str(letter_pressed)
        text = font.render(tx, True, BLUE)
        screen.blit(text, [670, 20])

        text = font.render(" = ", True, BLACK)
        screen.blit(text, [680, 20])

        text = font.render(str(current_vector[0]), True, BLUE)
        screen.blit(text, [700, 20])

        text = font.render("CORRECTO ", True, BLUE)
        screen.blit(text, [730, 20])

        vector = "[ " + str(current_vector[1]) + " ]"

        if showCorrect:
            text = font.render("Letra correcta!", True, GREEN)
            screen.blit(text, [680, 60])
            load_image = pygame.image.load('crucigrama/smile.jpeg')
            image = pygame.transform.scale(load_image, (100, 100))
            screen.blit(image, (950, 150))

        text = font.render(str(vector), True, BLUE)
        screen.blit(text, [830, 20])

        text = font.render(str(vector), True, BLUE)
        screen.blit(text, [830, 20])

        text = font.render(") entonces", True, BLACK)
        screen.blit(text, [870, 20])

        text = font.render("sino", True, BLACK)
        screen.blit(text, [640, 100])

        if not showCorrect:
            text = font.render("Letra incirrecta!", True, RED)
            screen.blit(text, [680, 140])
            load_image = pygame.image.load('crucigrama/sad.png')
            image = pygame.transform.scale(load_image, (100, 100))
            screen.blit(image, (950, 150))

        text = font.render("finsi", True, BLACK)
        screen.blit(text, [640, 160])

    # Preguntas
    text = font.render("Preguntas:", True, BLACK)
    screen.blit(text, [630, 300])

    text = font_small.render("V1: Permite interconexion inalambrica de dispositivos electronicos.", True, BLACK)
    screen.blit(text, [630, 320])

    text = font_small.render("V2: Instalacion con maquinarias para fabricar, confeccionar, elaborar etc.", True, BLACK)
    screen.blit(text, [630, 340])

    text = font_small.render("V3: Dispositivo electronico inalambrico. Lo usamos diario.", True, BLACK)
    screen.blit(text, [630, 360])

    text = font_small.render("V4: Nombre generico a las ditintas ramas del saber humano.", True, BLACK)
    screen.blit(text, [630, 380])

    text = font_small.render("V5: Relacionado a los dedos. Termino asociado a la tecnologia.", True, BLACK)
    screen.blit(text, [630, 400])

    text = font_small.render("V6: Maquina automatica capaz de sustituir a los humanos.", True, BLACK)
    screen.blit(text, [630, 420])

    # Update the screen
    pygame.display.flip()

    # Limited to 20 frames per second
    clock.tick(20)

# Close the program
pygame.quit()

