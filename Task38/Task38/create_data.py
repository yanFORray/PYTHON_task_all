def input_surname(msg):
    return input(msg)

def input_firstname(msg):
    return input(msg)

def input_patronymic(msg):
    return input(msg)

def input_num_phone(msg):
    return input(msg)

def input_path_file(msg):
    path_file = input(msg)
    expansion = path_file[len(path_file) - 4:]
    while expansion != '.txt':
        print('Файл должен быть с расширением ".txt"')
        path_file = input(msg)
        expansion = path_file[len(path_file) - 4:]
    return path_file