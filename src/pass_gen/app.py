import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# генерим пароль
if __name__ == "__main__":
    generated_password = generate_password()
    print(f"пасс гее: {generated_password}")
