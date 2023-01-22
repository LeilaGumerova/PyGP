# Загрузка картинок
import pygame

pygame.init()

icon = pygame.image.load('C:/TEMP/PyGP/Game1/Helping/icon.png')  # Иконка для игры
perc_img = pygame.image.load('C:/TEMP/PyGP/Game1/Objects/perc.png')  # Спрайт для персонажа
m_perc_img = pygame.image.load('C:/TEMP/PyGP/Game1/Objects/m_perc.png')  # Зеркальный спрайт для персонажа
health_img = pygame.image.load('C:/TEMP/PyGP/Game1/Objects/heart.png')  # Загрузка спрайта для сердца
health_img = pygame.transform.scale(health_img, (30, 30))  # Отражение спрата для сердца
rubbish_img = [pygame.image.load('C:/TEMP/PyGP/Game1/Objects/rubbish1.png'),
               pygame.image.load('C:/TEMP/PyGP/Game1/Objects/rubbish2.png'),
               pygame.image.load('C:/TEMP/PyGP/Game1/Objects/rubbish3.png'),
               pygame.image.load('C:/TEMP/PyGP/Game1/Objects/rubbish4.png')]  # Спрайты дял мусора
food_img = [pygame.image.load('C:/TEMP/PyGP/Game1/Objects/food1.png'),
            pygame.image.load('C:/TEMP/PyGP/Game1/Objects/food2.png'),
            pygame.image.load('C:/TEMP/PyGP/Game1/Objects/food3.png'),
            pygame.image.load('C:/TEMP/PyGP/Game1/Objects/food4.png')]  # Спрайты для еды
land = pygame.image.load('C:/TEMP/PyGP/Game1/Helping/Land.jpg')  # Изобрадение заднего фона
