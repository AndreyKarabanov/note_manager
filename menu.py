# Создаем бесконечный цикл и меню действий

while True:

    menu_ = ["Меню действий:",
             "1. Создать новую заметку",
             "2. Показать все заметки",
             "3. Обновить заметку",
             "4. Удалить заметку",
             "5. Найти заметки",
             "6. Выйти из программы"]
    for i in menu_:
        print(i)
        # Создаем переменную для ввода выбора действий из меню
    try:
        choise = int(input("Ваш выбор: "))

        # Исходя из выбранного действия, делаем обращения к предыдущим функциям

        if choise == 1:
            from create_note_function import create_note

            print("Заметка успешно создана")

        if choise == 2:
            from display_notes_function import display_notes

        if choise == 3:
            from update_notes_function import update_note

        if choise == 4:
            from delete_note import delete_note_function

        if choise == 5:
            from search_notes_function import search_notes

        if choise == 6:
            print("До свидания!")
            break

     # Выдаем ошибку при неккоректном вводе данных
        if choise >= 7:
            print("Неккоректный ввод")
            continue

    except ValueError:
        print("Неккоректный ввод")
        continue
