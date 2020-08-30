import pygame
import random
pygame.init()
list_map = []
gridSize = int(input("Enter Grid Size(40 Below is recommended; after 50, bugs may occur): "))
RandomLive = input("Start with Random Live cells(y/n)? ") == "y"
for row in range(gridSize):
    list_map.append([])
    for item in range(gridSize):
        if RandomLive:
            list_map[row].append(random.randrange(0, 2))
        else:
            list_map[row].append(0)
print(list_map)
window_size = (800, 800)
win = pygame.display.set_mode(window_size)
run = True
mouse_pos = (0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
isClick = False
isClickTwo = False


def draw_grid():
    blockSize = window_size[0] // gridSize
    color_grid = red
    for x in range(window_size[0]):
        for y in range(window_size[1]):
            pygame.draw.rect(win, color_grid, (x * blockSize, y * blockSize, blockSize, blockSize), 1)


def translate_list_to_map(map_list, a, b):
    for i in range(gridSize ** 2):
        if map_list[a][b] == 0:
            pygame.draw.rect(win, black, (b * (window_size[0] // gridSize),
                                          a * (window_size[0] // gridSize),
                                          window_size[0] // gridSize,
                                          window_size[0] // gridSize), 0)
        elif map_list[a][b] == 1:
            pygame.draw.rect(win, white, (b * (window_size[0] // gridSize),
                                          a * (window_size[0] // gridSize),
                                          window_size[0] // gridSize,
                                          window_size[0] // gridSize), 0)
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
    for i in range(gridSize ** 2):

        if y != 0:
            if map_list[x][y - 1] == 1:
                k += 1

        if y != gridSize - 1:
            if map_list[x][y + 1] == 1:
                k += 1

        if x != 0:
            if map_list[x - 1][y] == 1:
                k += 1

        if x != gridSize - 1:
            if map_list[x + 1][y] == 1:
                k += 1

        if x != 0 and y != 0:
            if map_list[x - 1][y - 1] == 1:
                k += 1

        if x != gridSize - 1 and y != 0:
            if map_list[x + 1][y - 1] == 1:
                k += 1

        if x != 0 and y != gridSize - 1:
            if map_list[x - 1][y + 1] == 1:
                k += 1

        if x != gridSize - 1 and y != gridSize - 1:
            if map_list[x + 1][y + 1] == 1:
                k += 1

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

        y += 1
        k = 0
        if y == len(map_list[x]):
            x += 1
            y = 0
        if x == len(map_list):
            break


def translate_mouse_pos_to_list_loc(map_list, z, x):
    m = 0
    n = 0
    startM = 0
    endM = window_size[0] // gridSize
    startN = 0
    endN = window_size[0] // gridSize

    for xPos in range(gridSize):
        if startM < x < endM:
            m = xPos
            break
        startM += window_size[0] // gridSize
        endM += window_size[0] // gridSize

    for zPos in range(gridSize):
        if startN < z < endN:
            n = zPos
            break
        startN += window_size[0] // gridSize
        endN += window_size[0] // gridSize
    print(n)

    if map_list[m][n] == 0:
        map_list[m][n] = 1


def reDrawGameWindow(is_click, pos):
    translate_list_to_map(list_map, 0, 0)
    draw_grid()
    translate_mouse_pos_to_list_loc(list_map, pos[0], pos[1])
    if is_click:
        next_gen(list_map)
    pygame.display.update()


while run:
    for events in pygame.event.get():

        if events.type == pygame.QUIT:
            run = False
            pygame.quit()

        if events.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        isClick = True

    reDrawGameWindow(isClick, mouse_pos)
