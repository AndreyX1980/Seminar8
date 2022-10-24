from logger import addData, line_by_line, search_by_name, to_the_column, deleteData
import match

def chooseUsers():
    print('__Телефонный справочник__\nВыбирите действие\n')
    print('"1" Вывод всех контактов построчно')
    print('"2" Вывод всех контактов в столбец')
    print('"3" Поиск контакта по имени')
    print('"4" Удаление записи')
    print('"5" Добавления новой записи\n')
    checkChoose = False
    while not checkChoose:
        try:
            data = int(input('Ввод: '))
            checkChoose = True if 0 < data < 6 else print('Такого варианта нет!')
        except: print('Повторите ваш выбор: ')
    match data:
        case 1:
            line_by_line()
            print('Все данные в файле "scan.csv".')
        case 2:
            to_the_column()
            print('Все данные в файле "scan.csv".')
        case 3:
            name = input('Введите имя: ')
            search_by_name(name)
            print('Все данные в файле "scan.csv".')
        case 4:
            name = input('Введите имя для удаления: ')
            deleteData(name)
            print('Все данные в файле "phone_book.txt".')
        case 5:
            name = input('Введите ФИ контакта для добавления: ')
            number = input('Введите номер тлф: ')
            commUs = input('Введите комментарий: ')
            addData(name, number, commUs)
            print('Все данные в файле "phone_book.txt".')