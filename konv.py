try:
    user_input = input("Введіть число: ")
    number = int(user_input)
    print("Ціле число:", number)
except ValueError:
    print("Помилка: введені дані не можна конвертувати в ціле число.")