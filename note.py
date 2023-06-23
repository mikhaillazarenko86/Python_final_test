import datetime
class Note:

    def __init__(self, id, date, header, text):
        self.id = id
        self.header = header
        self.text = text
        self.date = date


    def print_note(self):
        return f"Номер заметки: {self.id}\n Дата создания: {self.date}\n Заголовок: {self.header}\n Основной текст: {self.text}"



