import manager as m
def console():
    while True:

        m.print_menu()
        choice = input("Выберите команду: ")

        match choice:
            case "1":
                m.create()
            case "2":
                m.read()
            case "3":
                m.save()
            case "4":
                print(f"Загрузка заметок удалит все не сохраненные заметки!!!\n Загрузить заметки?")
                m.print_choise()
                choice = input("Выберите команду: ")
                match choice:
                    case "1":
                        m.load()
                    case "2":
                        m.print_menu()
            case "5":
                print(f"Удалить все заметки?")
                m.print_choise()
                choice = input("Выберите команду: ")
                match choice:
                    case "1":
                        m.del_all()
                    case "2":
                        m.print_menu()
            case "6":
                m.print_sortmenu()
                choice = input("Выберите команду: ")
                match choice:
                    case "1":
                        type_sort = False
                        m.sort(type_sort)
                    case "2":
                        type_sort = True
                        m.sort(type_sort)
            case "7":
                m.print_searchmenu()
                choice = input("Выберите команду: ")
                match choice:
                    case "1":
                        m.search_id()
                    case "2":
                        m.search_date()
            case "8":
                m.edit_note()
            case "9":
                m.del_note()
            case "0":
                break
            case _:
                print("Invalid choice. Please try again.")