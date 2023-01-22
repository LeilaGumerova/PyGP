import pygame

pygame.init()

with open("C:/TEMP/PyGP/Game1/Helping/Max_scores.txt", "r") as file:  # Файл с максимальным результатом
    max_scores = int(file.read())

scores = 0  # Текущее количество очков
health = 2  # Текущее количество жизней

display_width = 500  # Ширина дисплея
display_heigth = 760  # Высота дисплея
display = pygame.display.set_mode((display_width, display_heigth))  # Дисплей

usr_width = 125  # Ширина спрайта пользователя
usr_heigth = 118  # Высота спрайта пользователя
usr_x = display_width // 2 - 60  # Положение спрайта пользователя по x
usr_y = display_heigth - usr_heigth  # Положение спрайта пользователя по y

clock = pygame.time.Clock()  # Время
