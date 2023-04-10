from processing_writing import *
def hint():
    print('Выберите действие:' + '\n' + 
        '\t' + '1) "i" - импортировать данные в телефонный справочник' + '\n' +
        '\t' + '2) "v" - просмотр телефонного справочника' + '\n' +
        '\t' + '3) "f" - поиск' + '\n' +
        '\t' + '4) "a" - добавить запись в телефонный справочник' + '\n' +
        '\t' + '5) "o" - экспортировать данные из телефонного справочника' + '\n' +
        '\t' + '6) "m" - редактировать телефонный справочник' + '\n' +
        '\t' + '7) "e" - выйти из телефонного справочника')
    return input('Выполнить команду: ').lower()

def hint_find():
    print('Выберите тип поиска:' + '\n' + 
        '\t' + '1) "s" - по фамилии' + '\n' +
        '\t' + '2) "n" - по имени' + '\n' +
        '\t' + '3) "t" - по номеру телефона' + '\n' +
        '\t' + '4) "e" - завершить') 
    return input('Выполнить команду: ').lower()

def interface():
    print('<<< Телефонный справочник >>>')
    key = hint()
    key = checking_command(key, ('i', 'v', 'f', 'a', 'o', 'm', 'e'), \
                           'Введена некорректная команда, повторите ввод!!!')
    while key != 'e':
        if key == 'i':
            import_writing()
        elif key == 'v':
            viewer_writing()
        elif key == 'f':
            key_f = hint_find()
            key_f = checking_command(key_f, ('s', 'n', 't', 'e'), \
                           'Введена некорректная команда, повторите ввод!!!')
            while key_f != 'e':
                result_search = search_writing(key_f)
                if len(result_search) != 0:
                    print_result_search(result_search)
                else:
                    print('Ничего не найдено!!!')
                input('Для продолжения, нажмите "Enter"')
                key_f = hint_find()
                key_f = checking_command(key_f, ('s', 'n', 't', 'e'), \
                           'Введена некорректная команда, повторите ввод!!!')
        elif key == 'a':
            add_writing(True)
        elif key == 'o':
            export_writing()
        elif key == 'm':
            key_m = hint_find()
            key_m = checking_command(key_m, ('s', 'n', 't', 'e'), \
                           'Введена некорректная команда, повторите ввод!!!')
            while key_m != 'e':
                editing_phone_book(key_m)
                input('Для продолжения, нажмите "Enter"')
                key_m = hint_find()
                key_m = checking_command(key_m, ('s', 'n', 't', 'e'), \
                           'Введена некорректная команда, повторите ввод!!!')
        input('Для продолжения, нажмите "Enter"')
        key = hint()
        key = checking_command(key, ('i', 'v', 'f', 'a', 'o', 'm', 'e'), \
                           'Введена некорректная команда, повторите ввод!!!')
    print('До свидания!!!')