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
  buttons_box = toga.Box(style=Pack(direction=ROW, padding=5, spacing=5))
 # КНОПКА ГЕНЕРАТЦАИ
        generate_btn = toga.Button(
            'НЕИИРОВАТЬ', 
            on_press=self.generate_password,
            style=Pack(flex=1)
        )
 # интерфейс
        length_box.add(length_label)
        length_box.add(self.length_input)
        
        buttons_box.add(generate_btn)
        buttons_box.add(copy_btn)
        
        main_box.add(title_label)
        main_box.add(length_box)
        main_box.add(self.password_input)
        main_box.add(buttons_box)
        
        # окно
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
   def generate_password(self, widget):
       # бекем кусок оригинала
        length = int(self.length_input.value)
        password = generate_password(length)
        self.password_input.value = password
   def copy_password(self, widget):
       if self.password_input.value:
           self.main_window.clipboard = self.password_input.value

def main():
    return PasswordGenerator()


        
