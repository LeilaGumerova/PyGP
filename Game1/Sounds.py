# Загрузка звука
import pygame

pygame.init()

pygame.mixer.music.load('C:/TEMP/PyGP/Game1/Sounds/background.mp3')  # Звук для фона
food_sound = pygame.mixer.Sound('C:/TEMP/PyGP/Game1/Sounds/Eating.mp3')  # Звук при ловле еды
rubbish_sound = pygame.mixer.Sound('C:/TEMP/PyGP/Game1/Sounds/Rubbish.mp3')  # Звуку при ловле мусора
loss_sound = pygame.mixer.Sound('C:/TEMP/PyGP/Game1/Sounds/loss.wav')  # Звук для потреи жизни
hp_sound = pygame.mixer.Sound('C:/TEMP/PyGP/Game1/Sounds/hp+.wav')  # Звук при поражении
button_sound = pygame.mixer.Sound('C:/TEMP/PyGP/Game1/Sounds/button.wav')  # Звук при анжатии на кнопку
hp_sound.set_volume(1.2)  # Установление громкости
