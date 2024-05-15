import pygame
from pygame.locals import *


pygame.init()
#screens
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("TIC TAC TOE")

#colors
white  = (255 , 255 , 255)
black = (0, 0, 0)
red = (255, 0 , 0)
green = (0 , 255 , 0)

#game variables
line_width = 6
markers = []
game_over = False
winner = 0
#drawing lines
def draw_grids():
    for line in range(1 , 3):
        pygame.draw.line(screen , black , (0 , line * 100) , (screen_width , line * 100) , line_width)
        pygame.draw.line(screen , black , (line * 100 , 0) , (line * 100 ,screen_height) , line_width)


for x in range(3):
    x = [0] * 3
    markers.append(x)

def draw_markers():
    y_pos = 0
    for x in markers:
        x_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen , green , (x_pos * 100 + 10 , y_pos * 100 + 10) , (x_pos * 100 + 90 , y_pos * 100 + 90) , 5)
                pygame.draw.line(screen , green , (x_pos * 100 + 90 , y_pos * 100 + 10) , (x_pos * 100 + 10 , y_pos * 100 + 90) , 5)
            if y == -1:
                pygame.draw.circle(screen , red ,(x_pos*100 + 50 , y_pos * 100 + 50) , 30)
            x_pos += 1
        y_pos += 1
def draw_winner(winner):
    font_text = pygame.font.SysFont(None , 40)
    if winner == 0:
        font = font_text.render("Tie" , 1 , (0 , 255 , 0))
    else:
        font = font_text.render("Player " + str(winner) + " wins" , 1 , (0 , 255 , 0))
    rect_1 = pygame.Rect(80 , 120 , 200 , 70)
    pygame.draw.rect(screen , (0 ,0 ,255) , rect_1)
    screen.blit(font , (80 , 150))

def check_winner():
    global game_over
    global winner

    for row in markers:
        if sum(row) == 3:
            game_over = True
            winner = 1
        if sum(row) == -3:
            game_over = True
            winner = 2
    for row in range(3):
        if markers[0][row] + markers[1][row] + markers[2][row] == 3:
           game_over = True
           winner = 1
        if markers[0][row] + markers[1][row] + markers[2][row] == -3:
            game_over = True
            winner = 2
    if markers[0][0] + markers[1][1] + markers[2][2] == 3:
        game_over = True
        winner = 1
    if markers[0][0] + markers[1][1] + markers[2][2] == -3:
        game_over = True
        winner = 2
    if markers[0][2] + markers[1][1] + markers[2][0] == 3:
        game_over = True
        winner = 1
    if markers[0][2] + markers[1][1] + markers[2][0] == -3:
        game_over = True
        winner = 2
    count = 0
    for x in markers:
        for y in x:
            if y != 0:
                count += 1
    if count == 9:
        game_over = True
        winner = 0
def main():
    player = 1
    run = True
    clicked = False
    while run:
        screen.fill(white)
        draw_grids()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                clicked = True
            if event.type == MOUSEBUTTONUP and clicked:
                pos = event.pos
                pos_x = pos[0] // 100
                pos_y = pos[1] //  100
                if markers[pos_y][pos_x] == 0:
                    markers[pos_y][pos_x] = player
                    player *= -1
                    clicked = False
        draw_markers()
        check_winner()
        if game_over == True:
            draw_winner(winner)
        pygame.display.update()
if __name__ == '__main__':
    main()
pygame.quit()