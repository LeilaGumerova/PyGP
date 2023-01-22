# Подключение нужных бибилиотек
from Sounds import *
from Effects import *

pygame.init()

from Parametrs import display, display_width, display_heigth


class Button:  # Класс, отвечающий за кнопки
    def __init__(self, width, height):  # Высота и ширина кнопки
        self.width = width
        self.height = height

    def draw_button(self, x, y, message, action=None, font_size=30):  # Рисовка конпки
        mouse = pygame.mouse.get_pos()  # Положение мыши
        click = pygame.mouse.get_pressed()  # Нажата ли мышь

        if x < mouse[0] < x + self.width and y < mouse[
            1] < y + self.height:  # Изменение цвета кнопки, если мышь находится в ней
            pygame.draw.rect(display, (255, 0, 41), (x, y, self.width, self.height))

            if click[0] == 1 and action is not None:  # Если кнопка нажата, то выполнить действие
                pygame.mixer.Sound.play(button_sound)  # Звук нажатия кнопки
                pygame.time.delay(300)
                if action == quit:  # Запись результата при выходе из игры
                    file_1 = open('C:/TEMP/PyGP/Game1/Helping/Max_scores.txt', 'w')
                    file_1.write(str(max_scores))
                    file_1.close()
                    pygame.quit()
                    quit()
                action()  # Действие

        else:
            pygame.draw.rect(display, (100, 255, 251), (x, y, self.width, self.height))  # Просто рисовка кнопки

        print_text(message=message, text_x=x + 10, text_y=y + 10, font_size=font_size)  # Надпись на кнопке
