#Создаем список

list_ = []
print("Добро пожаловать в менеджер заметок! Вы можете добавить новую заметку.")
while True:

    #Создаем словарь с использованием ручного ввода данных

    note = {"Имя:": input("Введите ваше имя: "),
            "Заголовок:": input("Введите заголовок заметки: "),
            "Описание:": input("Введите описание заметки: "),
            "Статус:": input("Введите статус заметки: "),
            "Дата создания:": input("Введите дату создания заметки в формате 'день-месяц-год: "),
            "Дедлайн:": input("Введите дату дедлайна в формате 'день-месяц-год: ")}

    #Проверяем в правильном ли формате осуществился ввод даты

    from datetime import datetime
    try:
        datetime.strptime(note["Дата создания:"], "%d-%m-%Y")
        datetime.strptime(note["Дедлайн:"], "%d-%m-%Y")

    except ValueError:
        print("Введено неккоректное значение, убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024")
        continue

    #Добавляем словарь в список

    list_.append(note)

    #Даем пользователю возможность добавления других заметок

    two = input("Хотите добавить ещё одну заметку? (да/нет): ")
    if two == "да":
        continue
    if two == "нет":
        for user in list_[:]:
            print("Ваша заметка: ", user)
        break
    else:
        print("Введено неверное значение")
        break




