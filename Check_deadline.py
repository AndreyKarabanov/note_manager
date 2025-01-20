from datetime import datetime, date


today = date.today()
my_day = today.strftime("%d-%m-%Y")
print("Текущая дата:", my_day)  # Выводим текущую дату


while True:
    date2 = input("Введите дату дедлайна (в формате день-месяц-год): ") # Вводим дату окончания дедлайна
    try:
        date1 = datetime.strptime(my_day, '%d-%m-%Y')
        date3 = datetime.strptime(date2, '%d-%m-%Y') # Проверяем в правильном ли формате осуществился ввод
        break
    except ValueError:(
        print("Введено неккоректное значение, убедитесь, что вводите дату в формате день-месяц-год, например: 10-12-2024")) # Если формат не правильный, повторяем цикл
num_days = (date3 - date1).days # Производим вычитание двух дат, и в дальнейшем выводим результат
if date3 < date1:
    print("Внимание! Дедлайн истек", abs(num_days), "дней назад")
if date3 == date1:
    print("Дедлайн сегодня!")
else:
    print("До дедлайна осталось: ", num_days, "дней")
