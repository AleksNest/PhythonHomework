from unicodedata import name
import tel_num_check as c
import logger as log

def Date_input ():
    date = []
    global name, surname, tel_number, description
    name = input ('Введите имя: ')
    log.name_logger (name)
    surname = input ('Введите фамилию: ')
    log.surname_logger (surname)
    tel_number = input ('Введите номер телефона: ')
    log.tel_number_logger (tel_number)
    c.check_tel(tel_number)
    description = input ('Введите описание: ')
    log.description_logger (description)
    date = [name, surname, tel_number, description]
    
    return date






    