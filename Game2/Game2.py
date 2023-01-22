# Подключение нужных библиотек
import sys
import os

sys.path.append(os.path.abspath("C:\TEMP\PyGP\Game2"))

# Подключение диалога
from Start_dialog import *


def start_game_flood_it():  # Диалог
    app = QApplication(sys.argv)
    ex = Dialog_For_Parametrs()
    ex.show()
    sys.exit(app.exec())
