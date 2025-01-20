# Создаем функцию для нашего словаря

def update_note(**kwargs):
    print(kwargs)

# Наш словарь (заметка)
note = {'username': 'Андрей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'issue_date': '10-01-2025'}
# Выводим на экран нашу нынешнюю заметку
print("Ваша заметка:")
for keys, values in note.items():
    print(keys, ":")
    print(values)

from datetime import datetime

# Спрашиваем какой ключ пользователь хотел бы изменить
for i in note.keys():
    a = input("Какие данные вы хотите обновить? (username, title, content, status, issue_date): ")
    f = note.get(a)
    # Исключаем несуществующий ключ или пустой ввод
    if f == None:
        print("Введено неверное значение")
        continue
    # Проверяем правильность введенного формата даты и изменяем ее значение согласно вводу данных
    if a == "issue_date":
        b = input("Введите новое значение для " + a + ": ")
        try:
            datetime.strptime(b, "%d-%m-%Y")
            d = {a: b}
            note.update(d)
            print(note)
            break
        except ValueError:
            print("Введен неверный формат даты")
    # Изменяем значения ключей согласно вводу данных
    if f != None:
        b = input("Введите новое значение для " + a + ": ")
        d = {a: b}
        note.update(d)
        break

# Выводим обновленную функцию на экран
update_note(**note)
