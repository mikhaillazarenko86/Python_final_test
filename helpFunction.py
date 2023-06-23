import datetime
# Создание id  заметок
def create_id(list):
    if len(list) == 0:
        id = 1
    else:
        id = list[-1].id
        id += 1
    return id
#Получение текущей даты
def create_date():
    date = datetime.datetime.today().strftime("%Y.%m.%d")
    time = datetime.datetime.today().strftime("%H:%M:%S")
    date = date + ' ' + time
    return date

#Получаем список дат
def transform_date(list):
    date_list = []
    for i in range(len(list)):
        note = list[i]
        date = note.date
        date = date.split(' ')
        date = '.'.join(date)
        date = date.replace('.', '')
        date = date.replace(':', '')
        date_list.append(date)
    return date_list
#Ввод id заметки
def input_id():
    id = int(input("Введите id заметки: "))
    return id
#Ввод даты создания заметки
def input_date():
    yy = input("Введите год создания заметки: ")
    m = input("Введите месяц создания заметки: ")
    dd = input("Введите число создания заметки: ")
    return yy + '.' + m +'.' + dd