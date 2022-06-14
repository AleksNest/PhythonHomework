import re
def check_tel (tel_number):
    flag = True
    while flag:
        for i in tel_number:
            if re.match(r'[7-8]{1}[0-9]{9}', tel_number) and len(tel_number) == 11:
                flag = False
            else:
                tel_number = input ('Введите корректнеый номер  телефона: ')
