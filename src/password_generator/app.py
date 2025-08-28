import toga
from toga.style import Pack
from toga.tyle.pack import COLUMN, ROW
import random
import string
# оригинальная конструкция кода
def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

class PasswordGenerator(toga.App):
    def startup(self):
        # главный контейнер
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        
