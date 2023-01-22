import pygame, random  # Подключение библотек

pygame.init()

from Sounds import *
from Images import *
from Parametrs import *


# Вывод колиества оставшихся жизней
def show_healht():
    global health
    show = 0
    x = 20
    while show != health:
        display.blit(health_img, (x, 20))
        x += 40
        show += 1


# Проверка, что жизни остались
def check_health():
    global health
    health -= 1
    if health == 0:  # Если жизней не осталось, то поражение
        pygame.mixer.Sound.play(loss_sound)  # Звук поражения
        health = 2
        return False
    else:
        pygame.mixer.Sound.play(rubbish_sound)  # Звук, довли мусора
        return True


x = -100  # Положение сердца по x
y = 1000  # Положение сердца по y


def plus_health():  # Передвижение дизни
    global x, y, health
    display.blit(health_img, (x, y))
    y += 12  # Перемещение жизни
    if y > display_heigth:  # Если сердце выщло за границу
        x = random.randint(0, display_width - 30)
        y = random.randint(-250, -10)

    if display_heigth >= y >= usr_y:  # Проверка совпадения с пользователем
        if usr_x <= x <= usr_x + usr_width:
            y = 1000
            if health < 5:  # Прибавка жизни, если их меньше 5
                health += 1
                pygame.mixer.Sound.play(hp_sound)
