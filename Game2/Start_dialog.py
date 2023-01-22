# Подключение нужных библиотек
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton

# Подключение игры
from Flood_it import *


class Dialog_For_Parametrs(QDialog):  # Класс для сбора информации о желаем поле и количестве цветов
    def __init__(self):  # Инициализация
        super().__init__()
        uic.loadUi('C:\TEMP\PyGP\Game2\Dialog_Widget.ui', self)  # Макет из QtDesigner
        self.setWindowTitle('Flood it')  # Установка названия окна
        for new_size in [6, 10, 14, 18, 22, 26]:  # Задание значений для желаемого размера поля
            self.size_of_field.addItem(str(new_size))
        for new_number_of_colors in [3, 4, 5, 6, 7, 8]:  # Задание значений для желаемого количества цветов
            self.number_of_colors.addItem(str(new_number_of_colors))
        self.start_game.clicked.connect(self.start_flood_it)  # Подключение функции начала игры

    def start_flood_it(self):  # Начало игры
        size_of_field = int(self.size_of_field.currentText())
        number_of_colors = int(self.number_of_colors.currentText())
        flood_it(size_of_field, number_of_colors, self)
