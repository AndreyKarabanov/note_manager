# Создаем словари
list_ = [{"Имя": "Андрей",
          "Заголовок": "Война и мир"},
         {"Имя": "Олег",
          "Заголовок": "Хоббит"},
         {"Имя": "Максим",
          "Заголовок": "Сталкер"}]
# Создаем функцию
def delete_note_function():
    print("Текущие заметки:")
    for user in list_[:]:
        print(user)
# При вводе любого имени или заголовка удаляет словарь и выводит оставшиеся
    user_input = input("Введите имя пользователя или заголовок для удаления заметки: ")

    for i, book in enumerate(list_):

        if book["Имя"].lower() == user_input.lower():
            del list_[i]
            print("Успешно удалено. Остались следующие заметки:")
            break
        if book["Заголовок"].lower() == user_input.lower():
            del list_[i]
            print("Успешно удалено. Остались следующие заметки:")
            break
    else: print("Такого заголовка нет. Ваши заголовки:")

    for user in list_[:]:
        print(user)

delete_note_function()
