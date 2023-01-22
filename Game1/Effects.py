from Parametrs import *
import pygame

pygame.init()


# Функция для печати текста
def print_text(message, text_x, text_y, font_color=(0, 0, 0), font_type='C:/TEMP/PyGP/Game1/Helping/Srift.TTF',
               font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (text_x, text_y))
