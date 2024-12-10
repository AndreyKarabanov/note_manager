# Создаем словарь для хранения информации о заметке
note = {}


# Сбор данных от пользователя
note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите описание заметки: ")
note["status"] = input("Введите статус заметки: ")
note["created_date"] = input("Введите дату создания заметки: ")
note["issue_date"] = input("Введите дату истечения заметки: ")


# Добавляем заголовки в список внутри словаря
note["titles"] = []
for i in range(5):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    note["titles"].append(title)


# Выводим собранные данные
print("\nСобранная информация о заметке:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")