# FUCK TOGA migrate to Tkiner
import tkinter as tk
from tkinter import messagebox, ttk
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("генерал пароль by  Andreyka445 / VeroX")
        self.window.geometry("400x200")
        self.window.resizable(False, False)
        
        self.create_widgets()
    
    def create_widgets(self):
        # Zagolovok
        title_label = tk.Label(self.window, text="Генератор паролей", 
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # сюда пиши длину пароля
        length_frame = tk.Frame(self.window)
        length_frame.pack(pady=5)
        
        tk.Label(length_frame, text="Длина пароля:", 
                font=("Arial", 10)).pack(side=tk.LEFT)
        
        self.length_var = tk.IntVar(value=12)
        length_spinbox = tk.Spinbox(length_frame, from_=4, to=32, 
                                   width=5, textvariable=self.length_var,
                                   font=("Arial", 10))
        length_spinbox.pack(side=tk.LEFT, padx=5)
        
        # здесб  будет пароль
        password_frame = tk.Frame(self.window)
        password_frame.pack(pady=10, padx=20, fill=tk.X)
        
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(password_frame, textvariable=self.password_var, 
                                 font=("Arial", 12), width=30, state='readonly',
                                 relief=tk.SUNKEN, bd=2)
        password_entry.pack(fill=tk.X)
        
        # кнопки
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)
        
        generate_btn = tk.Button(button_frame, text="СГЕНЕРИРОВАТЬ", 
                               command=self.generate_password, 
                               width=15, height=2,
                               bg="#4CAF50", fg="white",
                               font=("Arial", 10, "bold"))
        generate_btn.pack(side=tk.LEFT, padx=5)
        
        copy_btn = tk.Button(button_frame, text="КОПИРОВАТЬ", 
                           command=self.copy_password,
                           width=15, height=2,
                           bg="#2196F3", fg="white",
                           font=("Arial", 10, "bold"))
        copy_btn.pack(side=tk.LEFT, padx=5)
    
    def generate_password(self):
        try:
            length = self.length_var.get()
            if length < 4 or length > 32:
                messagebox.showerror("фак ю , длинна тольоко от 4 до 32 букав и символов!")
                return
            
            password = generate_password(length)
            self.password_var.set(password)
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число!")
    
    def copy_password(self):
        password = self.password_var.get()
        if password:
            self.window.clipboard_clear()
            self.window.clipboard_append(password)
            messagebox.showinfo("урооо", "пароль скопирован")
        else:
            messagebox.showwarning("сначчала пароль сделай")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = PasswordGenerator()
    app.run()


        
