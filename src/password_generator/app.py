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

# Zagalovok
 title_label = toga.Label(
            'Генератор паролей', 
            style=Pack(font_size=20, padding_bottom=10)
        )
# конетинер для выбора длинны 
length_box = toga.Box(style=Pack(direction=ROW, padding=5))
        length_label = toga.Label('длина пароль:', style=Pack(padding_right=5))
 # поле для ввода доины
        self.length_input = toga.NumberInput(
            min_value=4, 
            max_value=32, 
            value=12,
            style=Pack(width=100)
        )
 # выводим пароль
        self.password_input = toga.TextInput(
            placeholder='пароль:', 
            readonly=True,
            style=Pack(padding=5, flex=1)
        )
 # контейнер для ионокфв   


        
