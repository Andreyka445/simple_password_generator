import random
import string

# длина пароля
length = 12
# Символы
characters = "abcdefghijkmnoprstuvwxyzABCDEFGHIJKMNOPRSTUWXYZ123456789"
# Генерим пароль
password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
# результ
print = (f"(пароль {password}")
