# Подключение библиотек
import pygame, random

pygame.init()

# Подключение нужных параметров и изображений
from Parametrs import display, display_width, display_heigth
from Images import *


class Rubbish:
    # инициализация переменных
    def __init__(self, x, y, rubbish_width, rubbish_height, rubbish_image, speed):
        # Положение по x и y, ширина и высота мусора, его изображение и скорость
        self.x = x
        self.y = y
        self.rubbish_width = rubbish_width
        self.rubbish_height = rubbish_height
        self.rubbish_image = rubbish_image
        self.speed = speed

    # Перемещение мусора
    def rubbish_move(self):
        if self.y <= display_heigth + self.rubbish_height:
            display.blit(self.rubbish_image, (self.x, self.y))
            self.y += self.speed
        else:  # Если вышел за границы
            self.y = -self.rubbish_height - random.randint(30, 500)
            self.x = random.randint(0, display_width)
            self.speed = random.randint(2, 5)


# Существующий мусор
def create_rubbish_arr(array):
    array.append(Rubbish(20000, 10000, 60, 44, rubbish_img[0], 3))
    array.append(Rubbish(20000, 10000, 78, 49, rubbish_img[1], 5))
    array.append(Rubbish(20000, 10000, 95, 87, rubbish_img[2], 4))
    array.append(Rubbish(20000, 10000, 68, 68, rubbish_img[3], 2.5))


# Функция для рисовки мусора
def draw_rubbish_array(array):
    for rubbish in array:
        rubbish.rubbish_move()
