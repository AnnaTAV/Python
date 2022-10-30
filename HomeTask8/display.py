message = '''Что вы хотите сделать?
0 - посмотреть
1 - добавить запись
2 - удалить запись
3 - записать в файл
4 - выйти\n'''

def display_data(data):
    for line in data:
        print(line)

def display_menu():
    answer = int(input(message))
    return answer

