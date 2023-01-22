# Подключение нужных библотек
import sys
import os
from random import sample, choice

# Подключение функций для победы и поражения
from win_code import *
from lose_code import *

sys.path.append(os.path.abspath("C:\TEMP\PyGP\Game2"))


class Board:  # Класс, отвечающий за поле для игры
    def __init__(self, size, colors, screen):  # Инициализация
        self.screen = screen  # Экран, на котором рисуем
        self.size = size  # Размер экрана
        self.was_move = 0  # Сколько было сделано ходов
        self.amount = size * colors // 3.5  # Максимум позволенных ходов
        COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (255, 255, 0), (255, 170, 0), (95, 26, 127),
                  (0, 255, 255)]  # Возможные цвета для клеток
        self.colors = []  # используемые цвета
        for i in range(colors):  # Выбор используемых цветов
            self.colors = sample(COLORS, colors)
        self.make_board()  # Заполнение поля

    def make_board(self):
        board = []  # Поле
        # Присвоение каждой клетки случайного цвета
        for i in range(self.size):
            one_str = []
            for j in range(self.size):
                one_str.append(choice(self.colors))
            board.append(one_str)
        self.now_color = board[0][0]  # Определение начального цвета
        self.board = board
        self.draw_board()  # рисуем поле

    def draw_board(self):  # Функция для рисование поля(по клеткам)
        for i in range(self.size):
            for j in range(self.size):
                pygame.draw.rect(self.screen, self.board[i][j], (i * 30, j * 30, 30, 30))

    def click(self, x, y):  # Функция, перекрашивающая часть поля, при нажатии на какю-нибудь клетку
        x = x // 30  # x-координата клетки
        y = y // 30  # y-координата клетки
        new_color = self.board[x][y]  # определение нового цвета
        if new_color != self.now_color:  # Проверка, что не перекрашиваем в тот же самый цвет
            self.was_move += 1  # Прибавлем ход
            self.was_changed = []  # Измененные клетки
            self.cell_repainting(0, 0, new_color)  # Перекраска клетки
            self.now_color = new_color  # Изменение текущего цвета
            win = True  # Все ли клетки закрашены
            # проверка все ли клетки закрашены
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] != self.now_color:
                        win = False
                        break
                if not win:
                    break
            if win:  # Если все, то победа
                wining(self.was_move)
            elif self.was_move == self.amount:  # Если не все, но ходы закончились, то поражение
                losing(self.was_move)

    def cell_repainting(self, x, y, new_color):  # Функция перекрашивающая клетку, если надо
        color = self.board[x][y]  # Цвет клетки
        if color == self.now_color:  # Проверка имеет ли клетка текущий цвет
            pygame.draw.rect(self.screen, new_color, (x * 30, y * 30, 30, 30))  # Перекраска
            self.was_changed.append([x, y])  # Добавление в список изменных клеток
            self.board[x][y] = new_color  # Изменение цвета клетки
            # Перкраска рядом стоящих клеток(рекурсией)
            rec_cell = [[x, y - 1], [x - 1, y], [x + 1, y], [x, y + 1]]
            for cell in rec_cell:
                if 0 <= cell[0] < self.size and 0 <= cell[1] < self.size and cell not in self.was_changed:
                    self.cell_repainting(cell[0], cell[1], new_color)
