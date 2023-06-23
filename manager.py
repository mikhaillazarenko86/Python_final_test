from function import NoteFunction
func = NoteFunction()

def print_menu():
    print("Заметки")
    print("1. Создать заметку")
    print("2. Показать все заметки")
    print("3. Сохранить заметки")
    print("4. Загрузить заметки")
    print("5. Удалить все заметки")
    print("6. Сортировка заметок по дате")
    print("7. Поиск заметок")
    print("8. Изменить заметку")
    print("9. Удалить заметку")
    print("0. Exit")
def print_sortmenu():
    print("1. Сортировка от старой к новой заметке")
    print("2. Сортировка от новой к старой заметке")
def print_choise():
    print("1. Да")
    print("2. Нет")
def print_searchmenu():
    print("1. Найти заметку по id")
    print("2. Найти заметку по дате")
def create():
    return func.create_note()

def read():
    print(func.read_notes())
def save():
    func.save_notes()
def load():
    func.load_notes()
def sort(type_sort):
    func.sort_notes(type_sort)
def del_all():
    func.del_all()
def del_note():
    func.del_note()
def search_id():
    func.find_id()
def search_date():
    func.find_date()
def edit_note():
    func.edit_note()