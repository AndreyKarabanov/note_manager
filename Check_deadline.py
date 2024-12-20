from datetime import date

mylist = []
today = date.today()
mylist.append(today.strftime("%d-%m-%Y"))
print("Текущая дата:", mylist[0])  # Выводим текущую дату

from datetime import datetime
while True:
    date2 = input("Введите дату дедлайна (в формате день-месяц-год): ") # Вводим дату окончания дедлайна
    try:
        date1 = datetime.strptime(mylist[0], '%d-%m-%Y')
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
