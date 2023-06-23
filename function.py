from note import Note
from helpFunction import *
import json
import datetime
class NoteFunction:
    def __init__(self):
        self.note = []
        self.file_name = "notes.json"  # Имя файла для сохранения заметок
# Создание заметки
    def create_note(self):
        id = create_id(self.note)
        date = create_date()
        header = input("Введите заголовок: ")
        text = input("Введите текст заметки: ")
        note = Note(id, date, header, text)
        self.note.append(note)
        self.save_notes()

# Вывод всех заметок на экран
    def read_notes(self):
        s = ''
        for i in range(len(self.note)):
            note = self.note[i].print_note()
            s += f"\n{note}\n"
        return s

# Сохранение заметок
    def save_notes(self):
        notes_data = []
        for note in self.note:
            note_data = {
                "id" : note.id,
                "date" : note.date,
                "header" : note.header,
                "text" : note.text
            }
            notes_data.append(note_data)
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(notes_data, file, indent=4)
        print("Заметка сохранена")

# Загрузка заметок из файла
    def load_notes(self):
        try:
            self.note = []
            with open(self.file_name, "r") as f:
                data = json.load(f)
            note_to_notes = {}
            for note in data:
                id = note["id"]
                date = note["date"]
                header = note["header"]
                text = note["text"]
                note = Note(id, date, header, text)
                self.note.append(note)
            print("Заметки загружены!")
        except FileNotFoundError:
            print("Файл не найден.")
#Сортировка по дате
    def sort_notes(self, type_sort):
        try:
            date_list = sorted(transform_date(self.note), reverse=type_sort)
            new_date_list = []
            for date in date_list:
                yyyy = date[:4]
                mm = date[4:6]
                dd = date[6:8]
                h = date[8:10]
                m = date[10:12]
                s = date[12:14]
                i = yyyy + '.' + mm + '.' + dd + ' ' + h + ':' + m + ':' + s
                new_date_list.append(i)
            new_list = []
            for date in new_date_list:
                for note in self.note:
                    if date == note.date:
                        new_list.append(note)
            self.note = new_list
            for i in range(len(self.note)):
                note = self.note[i]
                print(note.print_note())
        except UnboundLocalError:
                print("Список пуст! Загрузите заметки или создайте их.")
#Удаление всех заметок
    def del_all(self):
        self.note = []
        return self.note

# Удаление заметки
    def del_note(self):
        note = self.find_id()
        print("Заметка удалена")
        self.note.remove(note)
        return self.note
#Поиск заметки по id
    def find_id(self):
        search_id = input_id()
        count = 0
        for note in self.note:
            id = int(note.id)
            if search_id == id:
                print(note.print_note())
                count += 1
                return note
                break
        if count == 0:
            print("Заметки не найдены.")

#Поиск заметки по дате
    def find_date(self):
        search_date = input_date()
        count = 0
        for note in self.note:
            date = note.date
            if search_date in date:
                print(note.print_note())
                count += 1
        if count == 0:
            print("Заметки не найдены.")

#Редактирование заметки
    def edit_note(self):
        note = self.find_id()
        note.header = input("Введите новый заголовок: ")
        note.text = input("Введите новый текст: ")




