from datetime import datetime

def get_user ():
    info = []
    
    first_name = input('Введите имя:\n ')
    info.append(first_name)
    
    second_name = input('Введите фамилию:\n ')
    info.append(second_name)
    
    birthday = input('Введите дату рождения. Формат dd.mm.yyyy:\n ')
    info.append(birthday)    
    
    phone_number = ''
    valid =False
    while not valid:
        try:
            phone_number = input('Введите номер телефона:\n ')
            if len(phone_number) != 11:
                print('Номер телефона введен некорректно! Введите 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
   
    return info
    