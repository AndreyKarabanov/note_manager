# Создаем словари
list_ = [{"Имя": "Андрей",
          "Заголовок": "Война и мир"},
         {"Имя": "Олег",
          "Заголовок": "Хоббит"},
         {"Имя": "Максим",
          "Заголовок": "Сталкер"}]
print("Текущие заметки:")
for user in list_[:]:
    print(user)
# При вводе любого имени или заголовка удаляет словарь и выводит оставшиеся
user_input = input("Введите имя пользователя или заголовок для удаления заметки: ")
for i, book in enumerate(list_):
    if book["Имя"] == user_input:
        del list_[i]
for i, book in enumerate(list_):
    if book["Заголовок"] == user_input:
        del list_[i]
print("Успешно удалено. Остались следующие заметки:")
for user in list_[:]:
    print(user)