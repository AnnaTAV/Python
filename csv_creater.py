def createre ():
    file = 'Phonebook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Имя;Фамилия;Дата рождения;Номер телефона\n')
        