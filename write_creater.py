from HomeTask7.user import get_user as us

info = us()
def write_csv ():
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def write_txt ():
    file = 'Phonebook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Имя: {info[0]}\n\nФамилия: {info[1]}\n\nДата рождения: {info[2]}\n\nНомер телефона: {info[3]}\n\n\n')
        