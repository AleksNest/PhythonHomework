def output_data():
    with open ('pupil.txt', 'r', encoding ='utf-8') as f:
        for i in f:
            row = i.split(';')
            id_pupil = row[0]
            name = row[1].split()[0]
            surname = row[1].split()[1]
            school = row[2]
            mark = row[3]
            bithday = row[4]
            print (f'id:{id_pupil}\nИмя: {name}\nФамилия: {surname}\nшкола: {school}\nОценка: {mark}\nДата рождения: {bithday}\n ')

    with open ('parants.txt', 'r', encoding ='utf-8') as f:
        for i in f:
            row = i.split(';')
            id_pupil = row[0]
            name = row[1].split()[0]
            name2 = row[1].split()[1]
            surname = row[1].split()[2]
            tel = row[2]
            print (f'id:{id_pupil}\nродитель:\nИмя: {name}\nОтчество: {name2}\nФамилия: {surname}\nтелефон: {tel}\n ')