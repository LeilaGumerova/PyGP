# Подключение библиотек
import os
import sys
import pygame

sys.path.append(os.path.abspath("C:\TEMP\PyGP\Game1"))

import Game1
from Game2 import Game2


# Содание меню
def show_menu():
    show = True

    # Оформление экрана, название, иконка
    display = pygame.display.set_mode((Game1.display_width, Game1.display_heigth))
    pygame.display.set_caption('ИГРЫ')
    main_icon = pygame.image.load('C:/TEMP/PyGP/main_icon.png')
    pygame.display.set_icon(main_icon)
    menu_bckg = pygame.image.load('C:/TEMP/PyGP/Menu.jpg')

    # Конпки для начала игр и выхода
    start_game_1_button = Game1.Button(320, 60)
    start_game_2_button = Game1.Button(320, 90)
    exit_button = Game1.Button(210, 90)

    while show:
        # проверка выхода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame, quit()
                quit()

        # Фон и рисовка конпок
        display.blit(menu_bckg, (0, 0))
        start_game_1_button.draw_button(100, 170, 'Start "Catch the food"', Game1.start_game_lovi, 39)
        start_game_2_button.draw_button(100, 240, 'Start "Flood it"', Game2.start_game_flood_it, 55)
        exit_button.draw_button(150, 340, 'QUIT', quit, 75)

        # Обновление экрана
        pygame.display.update()
        Game1.clock.tick(60)
