# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.core.clipboard import Clipboard
import random
import string
import webbrowser

def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

class PasswordGenerator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15
        self.create_widgets()
    
    def create_widgets(self):
        # zagolovok
        title_label = Label(
            text=" прпр генерал пароль приветсувет тебя!",
            font_size='20sp',
            bold=True,
            size_hint_y=None,
            height='50dp'
        )
        self.add_widget(title_label)
        
        # dlina
        length_layout = BoxLayout(
            size_hint_y=None,
            height='50dp',
            spacing='10dp'
        )
        
        length_label = Label(
            text="Длина пароля:",
            font_size='16sp',
            size_hint_x=None,
            width='100dp'
        )
        
        self.length_spinner = Spinner(
            text='12',
            values=[str(i) for i in range(4, 33)],
            size_hint_x=None,
            width='80dp',
            font_size='16sp'
        )
        
        length_layout.add_widget(length_label)
        length_layout.add_widget(self.length_spinner)
        self.add_widget(length_layout)
        
        # pole vvoda
        self.password_input = TextInput(
            text='',
            font_size='18sp',
            size_hint_y=None,
            height='60dp',
            readonly=True,
            background_color=(0.95, 0.95, 0.95, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.add_widget(self.password_input)
        
        # Кнопки
        buttons_layout = BoxLayout(
            size_hint_y=None,
            height='70dp',
            spacing='10dp'
        )
        
        self.generate_btn = Button(
            text="ЖМИ",
            background_color=(0.3, 0.7, 0.3, 1),
            color=(1, 1, 1, 1),
            bold=True,
            font_size='14sp'
        )
        self.generate_btn.bind(on_press=self.generate_password)
        
        self.copy_btn = Button(
            text="COPY",
            background_color=(0.13, 0.59, 0.95, 1),
            color=(1, 1, 1, 1),
            bold=True,
            font_size='14sp'
        )
        self.copy_btn.bind(on_press=self.copy_password)
        
        buttons_layout.add_widget(self.generate_btn)
        buttons_layout.add_widget(self.copy_btn)
        self.add_widget(buttons_layout)
        
        # tg lonk
        made_by_label = Label(
            text="Сделано VeroX:",
            font_size='14sp',
            size_hint_y=None,
            height='40dp'
        )
        self.add_widget(made_by_label)
        
        self.telegram_btn = Button(
            text="https://t.me/Andreyka445real",
            font_size='12sp',
            size_hint_y=None,
            height='50dp',
            background_color=(0.2, 0.5, 0.8, 1),
            color=(1, 1, 1, 1)
        )
        self.telegram_btn.bind(on_press=self.open_telegram)
        self.add_widget(self.telegram_btn)
    
    def generate_password(self, instance):
        try:
            length = int(self.length_spinner.text)
            if length < 4 or length > 32:
                self.show_popup("Ошибка", "тольок  от 4 до 32 символов!")
                return
            
            password = generate_password(length)
            self.password_input.text = password
        except ValueError:
            self.show_popup("Ошибка", "ниид коррект намбер !")
    
    def copy_password(self, instance):
        password = self.password_input.text
        if password:
            Clipboard.copy(password)
            self.show_popup("Успех", "скопировано!")
        else:
            self.show_popup("Внимание", "сначала нада сгенерировать пароль!")
    
    def open_telegram(self, instance):
        webbrowser.open("https://t.me/Andreyka445real")
    
    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_layout.add_widget(Label(text=message, font_size='16sp'))
        
        close_btn = Button(text="OK", size_hint_y=None, height='50dp')
        
        popup = Popup(
            title=title,
            content=popup_layout,
            size_hint=(0.7, 0.4)
        )
        
        close_btn.bind(on_press=popup.dismiss)
        popup_layout.add_widget(close_btn)
        
        popup.open()

class PasswordGeneratorApp(App):
    def build(self):
        return PasswordGenerator()

if __name__ == "__main__":
    PasswordGeneratorApp().run()
