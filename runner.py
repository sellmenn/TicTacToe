import pygame
from game import *
from copy import deepcopy
from time import sleep
from player import *

# Window Size
X_RES = 1280
Y_RES = 720

def runner():
    board = Board()
    pygame.init()
    screen = pygame.display.set_mode((X_RES, Y_RES))
    pygame.display.set_caption("Tic-Tac-Toe")
    clock = pygame.time.Clock()
    running = True
    o_list, x_list = list(), list()
    turn = "O"
    while running:
        screen.fill("black")
        if not board.end_game():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    coordinate = get_coordinate(pygame.mouse.get_pos())
                    center_pos = get_center_pos(coordinate)
                    if center_pos not in o_list and center_pos not in x_list:
                        if turn == "O":
                            o_list.append(center_pos)
                            board.make_move(coordinate)
                            turn = "X"
            if turn == "X" and not board.end_game():
                ai_move = best_move(board)
                board.make_move(ai_move)
                x_list.append(get_center_pos(ai_move))
                turn = "O"
        else:
            sleep(1)
            running = False
        draw_grid(screen)
        draw_o(screen, o_list)
        draw_x(screen, x_list)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

def draw_grid(screen):
    x, y = screen.get_size()
    pygame.draw.rect(screen, "white", pygame.Rect(300, 50, x - 600, y - 100), 5)
    # Draw horizontal lines
    pygame.draw.line(screen, "white", (300, 255), (979, 255), 5)
    pygame.draw.line(screen, "white", (300, 460), (979, 460), 5)
    # Draw vertical lines
    pygame.draw.line(screen, "white", (525, 50), (525, 669), 5)
    pygame.draw.line(screen, "white", (750, 50), (750, 669), 5)

def draw_o(screen, positions):
    for position in positions:
        pygame.draw.circle(screen, "white", position, 50, 1)

def draw_x(screen, positions):
    for position in positions:
        x, y = position
        pygame.draw.line(screen, "white", (x-50, y-50), (x+50, y+50), 1)
        pygame.draw.line(screen, "white", (x-50, y+50), (x+50, y-50), 1)

def get_coordinate(position):
    x, y = position
    coord_x, coord_y = 0, 0
    if 300 < x < 525:
        coord_y = 0
    elif 525 < x < 750:
        coord_y = 1
    elif 750 < x < 979:
        coord_y = 2
    if 50 < y < 255:
        coord_x = 0
    elif 255 < y < 460:
        coord_x = 1
    elif 460 < y < 669:
        coord_x = 2
    return coord_x, coord_y

def get_center_pos(coordinate):
    x, y = 0, 0
    coord_x, coord_y = coordinate
    if coord_x == 0:
        y = 150
    elif coord_x == 1:
        y = 355
    elif coord_x == 2:
        y = 560
    if coord_y == 0:
        x = 412
    elif coord_y == 1:
        x = 637
    elif coord_y == 2:
        x = 862
    return x, y

if __name__ == "__main__":
    runner()