import pygame
from game import *
from copy import deepcopy
from time import sleep
from player import *

def runner():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Tic-Tac-Toe")
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 25)
    option_o = font.render('Play as O', True, "white")
    option_x = font.render('Play as X', True, "white")
    o_rect = option_o.get_rect(center=(420, 720/2))
    x_rect = option_x.get_rect(center=(860, 720/2))
    running = True

    while running:
        turn = None
        player = None 
        while turn is None:
            screen.fill("black")
            screen.blit(option_o, o_rect)
            screen.blit(option_x, x_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if o_rect.collidepoint(x, y):
                        turn = "O"
                        player = turn
                    elif x_rect.collidepoint(x, y):
                        turn = "X"
                        player = "X"
            pygame.display.flip()
            clock.tick(30)
        board = Board()
        o_list, x_list = [], []
        while not board.end_game() and running:
            screen.fill("black")
            if turn != player:
                ai_move = best_move(board)
                board.make_move(ai_move)
                if player == "O":
                    turn = "O"
                    x_list.append(get_center_pos(ai_move))
                else:
                    turn = "X"
                    o_list.append(get_center_pos(ai_move))
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        coordinate = get_coordinate(pygame.mouse.get_pos())
                        center_pos = get_center_pos(coordinate)
                        if center_pos not in o_list and center_pos not in x_list:
                            if turn == player:
                                if player == "O":
                                    o_list.append(center_pos)
                                    turn = "X"
                                else:
                                    x_list.append(center_pos)
                                    turn = "O"
                                board.make_move(coordinate)          
            draw_grid(screen)
            draw_o(screen, o_list)
            draw_x(screen, x_list)
            pygame.display.flip()
            clock.tick(30)
        # Show winner
        utility = get_utility(board)
        if utility == 1:
            winner = "O"
        elif utility == -1:
            winner = "X"
        else:
            winner = "Draw"
        while running:
            screen.fill("black")
            text = font.render(f'Winner: {winner}', True, "white")
            text_rect = text.get_rect(center=(1280/2, 720/2))
            screen.blit(text, text_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            pygame.display.flip()
            clock.tick(30)

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

"""
Function which if passed a cursor position (X, Y), returns the corresponding coordinate on Board object as a tuple
"""
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

"""
Function which if passed a coordinate on Board, object, returns the center cursor position as a tuple
"""
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