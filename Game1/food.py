# Подключение библиотек
import pygame, random

# Подключение нужных параметров и изображений
from Parametrs import display, display_width, display_heigth
from Images import *

pygame.init()


class Food:
    # инициализация переменных
    def __init__(self, food_x, food_y, food_width, food_height, food_image, food_speed):
        # Положение по x и y, ширина и высота еды, его изображение и скорость
        self.food_x = food_x
        self.food_y = food_y
        self.food_width = food_width
        self.food_height = food_height
        self.food_image = food_image
        self.food_speed = food_speed

    # Перемещение еды
    def food_move(self):
        if self.food_y <= display_heigth + self.food_height:
            display.blit(self.food_image, (self.food_x, self.food_y))
            self.food_y += self.food_speed
        else:  # Если вышла за границу
            self.food_y = -self.food_height - random.randint(30, 500)
            self.food_x = random.randint(0, display_width)
            self.food_speed = random.randint(2, 5)


# Существующая еда
def create_food_arr(array):
    array.append(Food(20000, 1000, 47, 48, food_img[0], 7))
    array.append(Food(20000, 1000, 60, 60, food_img[1], 2))
    array.append(Food(20000, 1000, 49, 62, food_img[2], 4.5))
    array.append(Food(20000, 1000, 84, 84, food_img[3], 3))


# Функция для рисовки еды
def draw_food_array(array):
    for food in array:
        food.food_move()
