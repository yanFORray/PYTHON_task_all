from create_data import *
def import_writing():
    imp_path = input_path_file('Укажите путь и имя импортируемого файла: ')
    path_phone_book = input_path_file('Укажите путь и имя файла для импортирования данных: ')
    try:
        with open(imp_path.strip(), 'r', encoding='utf-8') as imp_file:
            with open(path_phone_book.strip(), '+a', encoding='utf-8') as phone_book:
                for writing in imp_file:
                    phone_book.seek(0)
                    if writing not in phone_book:
                        phone_book.write(writing)
        print('Данные перенесены')
    except:
        print('Указанный файл не найден')

def export_writing():
    exp_path = input_path_file('Укажите путь и имя файла для экспорта данных: ')
    path_phone_book = input_path_file('Укажите путь и имя экспортируемого файла: ')
    try:
        with open(path_phone_book.strip(), 'r', encoding='utf-8') as phone_book:
            with open(exp_path.strip(), '+a', encoding='utf-8') as exp_file:
                for writing in phone_book:
                    exp_file.seek(0)
                    if writing not in exp_file:
                        exp_file.write(writing)
        print('Данные перенесены')
    except:
        print('Указанный файл не найден')

def viewer_writing():
    try:
        with open('my_phone_book.txt', 'r', encoding='utf-8') as phone_book:
            list_viewer = []
            for writing in phone_book:
                list_viewer.append(tuple(writing.split('!')))
            print_result_search(list_viewer)
    except:
        print('Телефонного справочника нет')

def add_writing(key_add):
    try:
        with open('my_phone_book.txt', 'a', encoding='utf-8') as phone_book:
            while key_add:
                print('Добавьте контакт:')
                surname = input_surname('Фамилия: ')
                firstname = input_firstname('Имя: ')
                patronymic = input_patronymic('Отчество: ')
                num_phone = input_num_phone('Номер телефона: ')
                while not num_phone.isdigit():
                    print('''Номер телефона должен содержать только цифры!!!
Введите повторно номер телефона''')
                    num_phone = input_num_phone('Номер телефона: ')
                phone_book.write(f'{surname}!{firstname}!{patronymic}!{num_phone}\n')
                print('Контакт добавлен')
                sequel = input('Продолжить добавление контактов [yes/no]: ')
                sequel = checking_command(sequel, ('yes', 'no'), \
                                          'Введена некорректная команда, повторите ввод!!!')
                if sequel == 'no':
                    key_add = False
    except:
        print('Телефонного справочника нет')  

def search_writing(key_search):
    try:
        if key_search == 's':
            value = input_surname('Фамилия: ')
            ind = 0
        elif key_search == 'n':
            value = input_firstname('Имя: ')
            ind = 1
        else:
            value = input_num_phone('Номер телефона: ')
            ind = 3
        print('Результат поиска:')
        with open('my_phone_book.txt', 'r', encoding='utf-8') as phone_book:
            list_search = []
            for i, writing in enumerate(phone_book):
                writing = writing.split('!')
                if value.strip().lower() == writing[ind].strip().lower():
                    writing.append(i)
                    list_search.append(tuple(writing))
        return list_search
    except:
        print('Телефонного справочника нет')

def change_phone_book(value, ind, ind_chan, number):
    try:
        with open('my_phone_book.txt', 'r', encoding='utf-8') as phone_book:
            phone_book.seek(0)
            list_phone_book = phone_book.readlines()
        writing_chan = list_phone_book[ind_chan].split('!')
        writing_chan[ind] = value
        writing_chan = '!'.join(writing_chan)
        list_phone_book[ind_chan] = writing_chan
        with open('my_phone_book.txt', 'w', encoding='utf-8') as phone_book:
            phone_book.writelines(list_phone_book)
        print(f'Запись № {number} изменена')
    except:
        print('Телефонного справочника нет')

def change_writing(list_chan):
    if len(list_chan) > 1:
        num_writing = int(input('Изменить запись № '))
    else:
        num_writing = 1
    while not 0 < num_writing <= len(list_chan):
        print('Введенной записи нет, повторите ввод!!!')
        num_writing = int(input('Изменить запись № '))
    ind_chan = list_chan[num_writing - 1][4]
    print('Укажите, что нужно изменить в записи' + '\n' + 
          '\t' + '1) "sn" - фамилию' + '\n' +
          '\t' + '2) "fn" - имя' + '\n' +
          '\t' + '3) "pa" - отчество' + '\n' +
          '\t' + '4) "nt" - номер телефона')
    perform = input('Выполнить команду: ')
    perform = checking_command(perform, ('sn', 'fn', 'pa', 'nt'), \
                                'Введена некорректная команда, повторите ввод!!!')
    if perform == 'sn':
        change_phone_book(input_surname('Новая фамилия: '), 0, ind_chan, num_writing)
    elif perform == 'fn':
        change_phone_book(input_firstname('Новое имя: '), 1, ind_chan, num_writing)
    elif perform == 'pa':
        change_phone_book(input_patronymic('Новое отчество: '), 2, ind_chan, num_writing)
    else:
        num_phone = input_num_phone('Новый номер телефона: ')
        while not num_phone.isdigit():
            print('''Номер телефона должен содержать только цифры!!!
Введите повторно номер телефона''')
            num_phone = input_num_phone('Новый номер телефона: ')
        change_phone_book(num_phone + '\n', 3, ind_chan, num_writing)

def del_writing(list_del):
    try:
        if len(list_del) > 1:            
            num_writing = int(input('Удалить запись № '))
        else:
            num_writing = 1
        while not 0 < num_writing <= len(list_del):
            print('Введенной записи нет, повторите ввод!!!')
            num_writing = int(input('Удалить запись № '))
        ind_del = list_del[num_writing - 1][4]
        with open('my_phone_book.txt', 'r', encoding='utf-8') as phone_book:
            phone_book.seek(0)
            list_phone_book = phone_book.readlines()
        del list_phone_book[ind_del]
        with open('my_phone_book.txt', 'w', encoding='utf-8') as phone_book:
            phone_book.writelines(list_phone_book)
        print(f'Запись № {num_writing} удалена')
    except:
        print('Телефонного справочника нет')

def hint_edit():
    print('Дальнейшие действия:' + '\n' + 
          '\t' + '1) "sd" - удалить запись' + '\n' +
          '\t' + '2) "md" - изменить запись' + '\n' +
          '\t' + '3) "e" - выйти без редактирования телефонного справочника') 
    return input('Выполнить команду: ').lower()

def editing_phone_book(key_search):
    list_edit = search_writing(key_search)
    if len(list_edit) != 0:
        print_result_search(list_edit)
        perform = hint_edit()
        perform = checking_command(perform, ('sd', 'md', 'e'), \
                                   'Введена некорректная команда, повторите ввод!!!')
        if perform == 'sd':
            del_writing(list_edit)
        elif perform == 'md':
            change_writing(list_edit)
    else:
        print('Ничего не найдено!!!')

def checking_command(cmd, condition, msg):
    while cmd not in condition:
        print(msg)
        cmd = input('Выполнить команду: ')
    return cmd

def print_result_search(result):
    for i, elem in enumerate(result):
        print(f'Запись № {i + 1} \t| Фамилия: {elem[0]}')
        print(f'\t\t| Имя: {elem[1]}')
        print(f'\t\t| Отчество: {elem[2]}')
        print(f'\t\t| Номер телефона: {elem[3]}')