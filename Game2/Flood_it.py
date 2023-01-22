from Board import *  # Подключение поля


def flood_it(field_size, colors, dialog):  # Функция, отвечающая за игру
    dialog.close()  # Закрытие диалога ввода информации
    pygame.init()  # Запуск Pygame

    pygame.mixer.music.load(
        'C:/TEMP/PyGP/Game2/background.mp3')  # Подключение звука (вообще моя любимя песня - одна из точно)
    pygame.mixer.music.play()
    icon = pygame.image.load('C:/TEMP/PyGP/Game2/icon.png')  # Загрузка иконки
    pygame.display.set_icon(icon)  # Установка иконки
    pygame.display.set_caption('Flood it')  # Установка названия окна

    size = field_size * 30  # Размер поля
    screen = pygame.display.set_mode((size, size))  # Создание экрана

    board = Board(field_size, colors, screen)  # Создание поля
    running = True  # Игровой цикл
    clock = pygame.time.Clock()  # Время
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Проверка выхода
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # Проверка нажатия на мышь
                x, y = event.pos  # Координаты мыши
                board.click(x, y)  # Перекраска поля
        pygame.display.flip()  # Обновление экрана
        clock.tick(50)  # Время
    pygame.quit()  # Выход
