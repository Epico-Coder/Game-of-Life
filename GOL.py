# Importing pygame + initialization

import pygame
pygame.init()

# Main List
list_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Displaying Window
window_size = (750, 750)
win = pygame.display.set_mode(window_size)

# Variables
run = True

mouse_pos = (0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

isClick = False
isClickTwo = False

# Draws borders


def draw_grid():
    blockSize = 30
    color_grid = red

    for x in range(window_size[0]):
        for y in range(window_size[1]):
            pygame.draw.rect(win, color_grid, (x * blockSize, y * blockSize, blockSize, blockSize), 1)


# Checks 1 or 0, displays accordingly


def translate_list_to_map(map_list, a, b):
    for i in range(625):
        if map_list[a][b] == 0:
            pygame.draw.rect(win, black, (b * 30, a * 30, 48, 48), 0)
        elif map_list[a][b] == 1:
            pygame.draw.rect(win, white, (b * 30, a * 30, 48, 48), 0)
        b += 1
        if b == len(map_list[a]):
            a += 1
            b = 0
        if a == len(map_list):
            break


# Next generation, rules


def next_gen(map_list):
    x = 0
    y = 0
    k = 0
    for i in range(625):

        # Checking Neighbours

        # Sides

        if y != 0:
            if map_list[x][y - 1] == 1:
                k += 1
        if y != 24:
            if map_list[x][y + 1] == 1:
                k += 1
        if x != 0:
            if map_list[x - 1][y] == 1:
                k += 1
        if x != 24:
            if map_list[x + 1][y] == 1:
                k += 1

        # Corners

        if x != 0 and y != 0:
            if map_list[x - 1][y - 1] == 1:
                k += 1

        if x != 24 and y != 0:
            if map_list[x + 1][y - 1] == 1:
                k += 1

        if x != 0 and y != 24:
            if map_list[x - 1][y + 1] == 1:
                k += 1

        if x != 24 and y != 24:
            if map_list[x + 1][y + 1] == 1:
                k += 1

        # Amt. of Neighbours

        if map_list[x][y] == 1:
            if k < 2:
                map_list[x][y] = 0

        if map_list[x][y] == 1:
            if k == 2 or k == 3:
                map_list[x][y] = 1

        if map_list[x][y] == 1:
            if k > 3:
                map_list[x][y] = 0

        if map_list[x][y] == 0:
            if k == 3:
                map_list[x][y] = 1

        # Resetting, going to next index

        y += 1
        k = 0
        if y == len(map_list[x]):
            x += 1
            y = 0
        if x == len(map_list):
            break

# Self-explanatory


def translate_mouse_pos_to_list_loc(map_list, z, x):
    m = 0
    n = 0

    if 0 < z < 30:
        m = 0
    if 30 < z < 60:
        m = 1
    if 60 < z < 90:
        m = 2
    if 90 < z < 120:
        m = 3
    if 120 < z < 150:
        m = 4
    if 150 < z < 180:
        m = 5
    if 180 < z < 210:
        m = 6
    if 210 < z < 240:
        m = 7
    if 240 < z < 270:
        m = 8
    if 270 < z < 300:
        m = 9
    if 300 < z < 330:
        m = 10
    if 330 < z < 360:
        m = 11
    if 360 < z < 390:
        m = 12
    if 390 < z < 420:
        m = 13
    if 420 < z < 450:
        m = 14
    if 450 < z < 480:
        m = 15
    if 480 < z < 510:
        m = 16
    if 510 < z < 540:
        m = 17
    if 540 < z < 570:
        m = 18
    if 570 < z < 600:
        m = 19
    if 600 < z < 630:
        m = 20
    if 630 < z < 660:
        m = 21
    if 660 < z < 690:
        m = 22
    if 690 < z < 720:
        m = 23
    if 720 < z < 750:
        m = 24

    if 0 < x < 30:
        n = 0
    if 30 < x < 60:
        n = 1
    if 60 < x < 90:
        n = 2
    if 90 < x < 120:
        n = 3
    if 120 < x < 150:
        n = 4
    if 150 < x < 180:
        n = 5
    if 180 < x < 210:
        n = 6
    if 210 < x < 240:
        n = 7
    if 240 < x < 270:
        n = 8
    if 270 < x < 300:
        n = 9
    if 300 < x < 330:
        n = 10
    if 330 < x < 360:
        n = 11
    if 360 < x < 390:
        n = 12
    if 390 < x < 420:
        n = 13
    if 420 < x < 450:
        n = 14
    if 450 < x < 480:
        n = 15
    if 480 < x < 510:
        n = 16
    if 510 < x < 540:
        n = 17
    if 540 < x < 570:
        n = 18
    if 570 < x < 600:
        n = 19
    if 600 < x < 630:
        n = 20
    if 630 < x < 660:
        n = 21
    if 660 < x < 690:
        n = 22
    if 690 < x < 720:
        n = 23
    if 720 < x < 750:
        n = 24

    # Changes index

    if map_list[n][m] == 0:
        map_list[n][m] = 1

# Displaying everything, calling main functions


def reDrawGameWindow(is_click, pos):
    translate_list_to_map(list_map, 0, 0)
    draw_grid()
    translate_mouse_pos_to_list_loc(list_map, pos[0], pos[1])
    if is_click:
        next_gen(list_map)
    pygame.display.update()


# Main loop

while run:
    for events in pygame.event.get():

        # Quit function

        if events.type == pygame.QUIT:
            run = False
            pygame.quit()

        # User enter live cell

        if events.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)

        # Running function

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        isClick = True

    reDrawGameWindow(isClick, mouse_pos)
