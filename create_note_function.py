# Импортируем дату и время
from datetime import datetime, date

today = date.today()   # Создаем переменную с сегодняшной датой
while True:           # Вводим все значения для нашего словаря
    note = {"username:": input("Введите ваше имя: "),
            "title:": input("Введите заголовок заметки: "),
            "content:": input("Введите описание заметки: "),
            "status:": input("Введите статус заметки: "),
            "created_name:": today.strftime("%d-%m-%Y"),
            "issue_date:": input("Введите дату дедлайна в формате 'день-месяц-год: ")}

    # Проверяем формат даты
    try:
        datetime.strptime(note["issue_date:"], "%d-%m-%Y")
        break
    except ValueError:
        print("Введено неккоректное значение, убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024")
        continue

# Создаем функцию, принимающую в себя наш словарь
def create_note(note):
    print("Ваша заметка:")
    for keys, values in note.items():
        print(keys)
        print(values)



create_note(note)
