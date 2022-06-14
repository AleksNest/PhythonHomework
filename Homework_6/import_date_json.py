'''
 Ввод данных в формате: 
*фамилия*
*имя*
*телефон*
*описание*
'''
import user_interface as u

def json_tel_num ():
    json_tel = {}
    date = u.Date_input()
    name, surname, tel_number, description = date
    json_tel[tel_number] = {'name': name, 'surname': surname,'description': description}
    # for i, j in json_tel.items():
    #     print (i, j)
    # print (json_tel)
  
    with open('bd.json','a+',encoding='utf-8' ) as file:
        for key,val in json_tel.items():
            file.write('{}:{}\n'.format(key,val))
  