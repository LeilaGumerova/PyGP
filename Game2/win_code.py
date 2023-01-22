import pygame  # Подключаем Pygame

COLORS = (pygame.Color('blue'), pygame.Color('red'), pygame.Color('green'))  # Цвета


def wining(moves):  # Функция для вывода сообщения о победе
    pygame.init()
    pygame.display.set_caption('Победа')  # Название окна

    screen = pygame.display.set_mode((310, 300))  # Создаем дисплей

    draw(screen, moves)  # Рисуем сообщение о победе

    while pygame.event.wait().type != pygame.QUIT:  # проверка выхода
        pygame.display.flip()
    pygame.quit()


def draw(screen, moves):  # Функция, рисующая сообщение о победе
    pygame.draw.rect(screen, COLORS[1], [0, 0, 310, 300])  # Фон
    pygame.font.init()  # Подключаем возможность писать
    my_font = pygame.font.SysFont('Comic Sans MS', 100)  # Подключаем шрифт
    text_surface = my_font.render("WIN!!!", False, (255, 255, 255))  # Надпись
    text_surface_num_of_moves = my_font.render(f"{str(moves)}/{str(moves)}", False,
                                               (255, 255, 255))  # Количество ходов(потраченные/все)
    screen.blit(text_surface, (0, 30))  # Вывод надписи
    screen.blit(text_surface_num_of_moves, (10, 150))  # Вывод количества ходов
