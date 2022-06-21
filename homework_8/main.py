from input_dict import input_data_parants, input_data_students
from output_dict import output_data

flag = True
while flag:
    print ('Выбирете: \n1 - ввод данных в справочник\n2 - вывод данных из справочника\n3 - выход из справочника')
    var = input()
    if (var == '3'):
        flag = False
    else:
        if '1' in var:
            choice = input ('Выберитет таблицу: \n1 - ученики\n2 - родители\n')
            if '1' in choice:
                input_data_students()
            else:
                input_data_parants()
        else:
            output_data()
    