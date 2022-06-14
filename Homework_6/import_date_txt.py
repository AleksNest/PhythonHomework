'''
 Ввод данных в формате:   фамилия, имя , телефон, описание
'''
import user_interface as u

def file_txt():
    with open ('bd.txt', 'a+', encoding='utf-8') as file:
        file.write(', '.join(u.Date_input()) + '\n')
   
