# Создаем список со словарями с заметками
notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено', 'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]

number = 0
# Создаем функцию для поиска заметок
def search_notes(notes, keyword=None, status=None):
    global number
    for i in notes:    # Завершает цикл при пустом словаре
        if i == {}:
            print("Список ваших заметок пуст")
            break
        else: keyword = input("Введите ключевое слово: ")    # Поиск по ключевому слову
        for i in notes:
            for key, value in i.items():
                if keyword in value:
                    number += 1
                    print("---------------------")
                    list_1 = ["Найдена заметка №", number, ":"]
                    print(*list_1)
                    for keys, values in i.items():
                        print(keys, ":", values)


        else:
            print("Такой заметки нет")


        status = input("Введите статус заметки: ")      # Поиск по статусу заметки
        for i in notes:
            for key, value in i.items():
                if status in value:
                    number += 1
                    print("---------------------")
                    list_1 = ["Найдена заметка №", number, ":"]
                    print(*list_1)
                    for keys, values in i.items():
                        print(keys, ":", values)
        else:
            print("Такой заметки нет")

        print("Введите ключевое слово и статус заметки: ")   # Поиск по ключевому слову и статусу
        keyword = input("Ключевое слово заметки: ")
        status = input("Статус заметки: ")
        for i in notes:
            for key, value in i.items():
                if keyword and status in value:
                    number += 1
                    print("---------------------")
                    list_1 = ["Найдена заметка №", number, ":"]
                    print(*list_1)
                    for keys, values in i.items():
                        print(keys, ":", values)
        break


# Выводим функцию на экран
search_notes(notes)




