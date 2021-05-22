import pygame
from pygame import mixer
import time
import random

"""INITIALIZATION OF PYGAME"""
pygame.init()

"""CREATING SCREEN"""
screen = pygame.display.set_mode((800, 600))

"""ADDING ICON AND TITLE"""
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

"""BACKGROUND COLOR"""
mixer.music.load("background.wav")
mixer.music.play(-1)

"""CLOCK"""
clock = pygame.time.Clock()

"""CREATED BY TEXT!"""
font = pygame.font.Font("Kembara Cinta Demo.ttf", 40)

"""GAME OVER TEXT!"""
gfont = pygame.font.Font("Kembara Cinta Demo.ttf", 70)

"""PLAY AGAIN!"""
pfont = pygame.font.Font("Kembara Cinta Demo.ttf", 20)

"""SCORE"""
sfont = pygame.font.Font("Kembara Cinta Demo.ttf", 40)
scorees = 0


def score():
    scores = sfont.render("Score: " + str(scorees), True, (0, 0, 0))
    screen.blit(scores, (10, 10))


def made_by():
    creator = font.render("Created by: Utsav Shrestha", True, (0, 0, 0))
    screen.blit(creator, (450, 550))


def game_over():
    game = gfont.render("GAME OVER", True, (0, 0, 0))
    screen.blit(game, (270, 250))


repeat_control = True


def again():
    agains1 = pfont.render("----- WANT TO PLAY AGAIN -----", True, (0, 0, 0))
    agains2 = pfont.render("PRESS Y TO PLAY AGAIN", True, (0, 0, 0))
    agains3 = pfont.render("PRESS N TO QUIT", True, (0, 0, 0))
    agains4 = pfont.render("----- THANKS FOR PLAYING -----", True, (0, 0, 0))
    screen.blit(agains1, (260, 350))
    screen.blit(agains2, (260, 370))
    screen.blit(agains3, (260, 390))
    screen.blit(agains4, (260, 410))


def repeat():
    while repeat_control:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    global scorees
                    scorees = 0
                    main()
                elif event.key == pygame.K_n:
                    quit()


def mix():
    if flag1 == 2:
        game_over()
        pygame.display.update()
        time.sleep(3)
        again()
        pygame.display.update()
        repeat()
        pygame.display.update()


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0, 0, 0), [x[0], x[1], snake_block, snake_block])


def main():

    """SNAKE ATTRIBUTE"""
    x = 400
    y = 300
    x_change = 0
    y_change = 0
    snake_block = 10

    """LENGTH OF SNAKE"""
    snake_list = []
    length_of_snake = 1

    """FOOD"""
    foodx = random.randrange(0, 800, 10)
    foody = random.randrange(0, 600, 10)

    """CONTROL ATTRIBUTE"""
    a = 0
    b = 0
    c = 0
    d = 0

    """GAME LOOP"""
    over = False

    """FLAG"""
    global flag1
    flag1 = 1

    while not over:

        """BACKGROUND COLOR"""
        screen.fill((0, 0, 0))
       

        """BACKGROUND IMAGE"""
        background = pygame.image.load("background.png")
        screen.blit(background, (0, 0))

        """CHECKING GAME LOOP"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True

            """MOVEMENT OF SNAKE"""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and a == 0:
                    x_change = snake_block
                    y_change = 0
                    b = 1
                    c = 0
                    d = 0
                elif event.key == pygame.K_LEFT and b == 0:
                    x_change = -snake_block
                    y_change = 0
                    a = 1
                    c = 0
                    d = 0
                elif event.key == pygame.K_UP and c == 0:
                    x_change = 0
                    y_change = -snake_block
                    a = 0
                    b = 0
                    d = 1
                elif event.key == pygame.K_DOWN and d == 0:
                    x_change = 0
                    y_change = snake_block
                    a = 0
                    b = 0
                    c = 1

        x += x_change
        y += y_change

        """SNAKE"""
        pygame.draw.rect(screen, (255, 0, 0), (foodx, foody, snake_block, snake_block))

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for p in snake_list[:-1]:
            if p == snake_head:
                flag1 = 2


        our_snake(snake_block, snake_list)

        if x == foodx and y == foody:
            print("yummy")
            foodx = random.randrange(0, 800, 10)
            foody = random.randrange(0, 600, 10)
            yummy_sound = mixer.Sound("yummy.wav")
            yummy_sound.play()
            global scorees
            scorees += 1
            length_of_snake += 1

        """ADDING BOUNDARIES AND GAME OVER"""
        if x <= 0 or y <= 0 or x >= 790 or y >= 590:
            flag1 = 2


        score()
        made_by()
        clock.tick(10)
        pygame.display.update()

        if flag1 == 2:
            mix()


main()
