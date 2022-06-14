from datetime import datetime as dt
from time import time

def name_logger(data):
    time  = dt.now().strftime('%H:%M')           
    with open('log.csv', 'a+', encoding='utf-8' ) as file:
        file.write('{} -  Имя: {};  '.format(time, data))

def surname_logger(data):
    time  = dt.now().strftime('%H:%M')           
    with open('log.csv', 'a+', encoding='utf-8' ) as file:
        file.write('{} -  Фамилия: {};  '.format(time, data))   

def tel_number_logger(data):
    time  = dt.now().strftime('%H:%M')           
    with open('log.csv', 'a+', encoding='utf-8' ) as file:
        file.write('{} -  телефон: {};  '.format(time, data))      

def description_logger(data):
    time  = dt.now().strftime('%H:%M')           
    with open('log.csv', 'a+', encoding='utf-8' ) as file:
        file.write('{} -  описание: {}\n'.format(time, data))      
