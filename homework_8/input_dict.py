import logger as l


def input_data_students():
    with open ('pupil.txt', 'r', encoding ='utf-8') as f:
        id_pupil = f.readlines()[-1].split(';')[0]
    id_str = int(id_pupil)+1
    str1 = ''
    str1 = 'ID, имя' + str(id_str)
    name = input('введите имя:  ')
    l.logger(name, str1)
    surname = input ('введите фамилию:  ' )
    l.logger(name, 'фамилия')
    school = input ('название учебного заведения:  ')
    l.logger(school, 'школа')
    mark = input ('введитет средний балл:   ')
    l.logger(mark, 'средний балл')
    bithday = input ('введите дату рождения:  ')
    l.logger(bithday, 'дата рождения')
    with open ('pupil.txt', 'r', encoding ='utf-8') as f:
        id_pupil = f.readlines()[-1].split(';')[0]
    
    with open ('pupil.txt', 'a', encoding ='utf-8') as f:
        f.write(f'{int(id_pupil)+1};{name} {surname};{school};{mark};{bithday}\n')
    
    
    
def input_data_parants():
    name = input('введите имя:  ')
    l.logger(name, 'имя родителя')
    name2 = input('введите отчество:  ')
    l.logger(name2, 'отчество родителя')
    surname = input ('введите фамилию:  ' )
    l.logger(surname, 'фамилия родителя')
    tel = input ('введите контиактный телефон:  ')
    l.logger(tel, 'телефон родителя')
    
    flag = False
    with open ('pupil.txt', 'r', encoding ='utf-8') as f:
        date = f.readlines()
    
    for row in date:
        if surname in row:
            flag = True
            id_pupil = row.split(';')[0]
            break
    else:
        print (f'нет ученика с фамилией {surname}')
    if flag:
        with open ('parants.txt', 'a', encoding ='utf-8') as f:
            f.write(f'{id_pupil};{name} {name2} {surname};{tel}\n')
