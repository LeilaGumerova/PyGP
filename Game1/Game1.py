# Подключание нужных библиотек
import os
import sys

sys.path.append(os.path.abspath("C:\TEMP\PyGP\Game1"))

from food import *
from rubbish import *
from button import *
from Effects import *
from Health import *

import pygame

pygame.init()

# Нужно ли совершить премещение
go_left = False
go_right = False


# Игровой цикл
def start_game_lovi():
    while run_game():
        pass


# Игровая функция
def run_game():
    global go_right, go_left, scores, health, heart_x, heart_y, game

    # Название, иконка и музыка
    pygame.display.set_caption('Лови!')
    pygame.display.set_icon(icon)
    pygame.mixer.music.play(-1)

    # Создание еды и мусора
    game = True
    rubbish_arr = []
    create_rubbish_arr(rubbish_arr)
    food_arr = []
    costum = perc_img
    create_food_arr(food_arr)

    # Очки и жизни
    scores = 0
    health += 2

    # Игровой цикл
    while game:
        # Проверка выхода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file_1 = open('C:/TEMP/PyGP/Game1/Helping/Max_scores.txt', 'w')  # Запись результата
                file_1.write(str(max_scores))
                file_1.close()
                pygame, quit()
                quit()
        # Проверка клавиш
        keys = pygame.key.get_pressed()
        # Проверка клавиши вправо
        if keys[pygame.K_RIGHT]:
            go_right = True
            costum = perc_img
        # Проверка клавиши влево
        elif keys[pygame.K_LEFT]:
            go_left = True
            costum = m_perc_img  # Отражение тележки

        # Идти вправо
        if go_right:
            right()
        # Идти влево
        if go_left:
            left()

        # Пауза
        if keys[pygame.K_ESCAPE]:
            pause()

        # Фон
        display.blit(land, (0, 0))

        # Проверка столкновения с мусором
        if check_rubbish(rubbish_arr):
            if not check_health():
                game = False

        # Сколько сейчас очков
        print_text('Scores: ' + str(scores), 370, 10)

        # Рисовка препятсвий
        draw_rubbish_array(rubbish_arr)

        # рисовка еды
        draw_food_array(food_arr)

        # рисовка персонажа
        display.blit(costum, (usr_x, usr_y))

        # Рисовка жизней
        show_healht()
        plus_health()

        # Начисление очков
        if check_food(food_arr):
            scores += 1

        # Обновление дисплэя
        pygame.display.update()
        clock.tick(60)

    # Запуск поражения
    return game_over()


# Функция хода вправо
def right():
    global usr_x, go_right
    if usr_x + 3 + usr_width <= display_width:
        usr_x += 3
    go_right = False


# Функция хода влево
def left():
    global usr_x, go_left
    if usr_x - 3 >= 0:
        usr_x -= 3
    go_left = False


# Пауза
def pause():
    global paused

    paused = True

    pygame.mixer.music.pause()

    # Конпка для продолжения
    cont_button = Button(200, 70)

    while paused:
        # проверка выхода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file_1 = open('C:/TEMP/PyGP/Game1/Helping/Max_scores.txt', 'w')
                file_1.write(str(max_scores))
                file_1.close()
                pygame.quit()
                quit()
        # проверка клавиш
        keys = pygame.key.get_pressed()

        # Рисовка кнопки для продолжения
        cont_button.draw_button(150, 360, 'Continue', cont, 50)

        # Обновление дисплея
        pygame.display.update()
        clock.tick(15)

    pygame.mixer.music.unpause()


# Продолжение игры
def cont():
    global paused
    paused = False


# Функция проверки столкновения с мусором
def check_rubbish(arr_proverki):
    for prov in arr_proverki:
        if display_heigth >= prov.y >= usr_y:
            if prov.x <= usr_x <= prov.x + prov.rubbish_width \
                    or prov.x <= usr_x + usr_width <= prov.x + prov.rubbish_width or \
                    usr_x <= prov.x <= usr_x + usr_width or \
                    usr_x <= prov.x + prov.rubbish_width <= usr_x + usr_width:  # Проверка столкновения
                prov.y = 1000
                return True
    return False


# Функция проверки ловли еды
def check_food(arr_proverki):
    for prov in arr_proverki:
        if display_heigth >= prov.food_y >= usr_y:
            if prov.food_x <= usr_x <= prov.food_x + prov.food_width \
                    or prov.food_x <= usr_x + usr_width <= prov.food_x + prov.food_width or \
                    usr_x <= prov.food_x <= usr_x + usr_width or \
                    usr_x <= prov.food_x + prov.food_width <= usr_x + usr_width:  # Проверка ловли
                pygame.mixer.Sound.play(food_sound)  # Звук при удачной ловле
                prov.food_y = 1000
                return True
    return False


def game_over():  # Функция окончания игры
    global scores, max_scores, stopped, health
    max_scores = max(scores, max_scores)  # Обновление максимального количества очков
    stopped = True
    health = 2
    while stopped:
        pygame.mixer.music.pause()  # Остановка музыки при паузе

        # проверка выхода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file_1 = open('C:/TEMP/PyGP/Game1/Helping/Max_scores.txt', 'w')  # Запись результата
                file_1.write(str(max_scores))
                file_1.close()
                pygame, quit()
                quit()

        rest_button = Button(115, 80)  # Кнопка для переигрывания
        esc_button = Button(100, 80)  # Кнопка для выхода

        # Вывод текста и рисовка кнопок
        print_text('Game over.', 190, 320)
        print_text('Max scores: ' + str(max(scores, max_scores)), 175, 350)
        rest_button.draw_button(80, 390, 'Start', start_game_lovi, 50)
        esc_button.draw_button(300, 390, 'Exit', main_page, 50)

        # Обновление дисплея
        pygame.display.update()
        clock.tick(15)


# Возвращение к меню
def main_page():
    global stopped
    stopped = False
    return True
