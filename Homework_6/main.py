import import_date_txt as txt
import import_date_json as json
import import_date_html as html
import export_date as ex

flag = True
while flag:
    m = int (input ('\nвыберите один из вариантов: 1 - импорт (ввод);  2 - экспорт (вывод); 3 - выход из программы:   ' ))
    if (m == 1 ):
        var = int (input ('\nВыберите формат файла для ввода справочника : 1 - bd.txt;  2 - bd.json;  3 - bd.html:  '))
        if var == 1:
            txt.file_txt()
        elif var == 2:
            json.json_tel_num ()
        else:
            html.file_html ()
    elif m == 2:
        var = int (input( 'выберите файл для вывода (экспорта): 1 - bd.txt;  2 - bd.json;  3 - bd.html:  '))
        if var == 1:
            print ('\nсправочник bd.txt:\n')
            ex.file_output_txt('bd.txt')
        elif var == 2:
            print ('\nсправочник bd.json:\n')
            ex.file_output_json('bd.json')
        else:
            print ('\nсправочник bd.html:\n')
            ex.file_output_html('bd.html')
    else:
        print ('программа завершена')
        break
        

    