'''Задача 1  Напишите программу, удаляющую из текста все слова, содержащие "абв".
'''
text = 'слова на абв надо убрать'
print('исходный текст: ', text)
with open ('file3.txt', 'w') as data:        
    data.write('слова на абв надо убрать')
    f = open('file3.txt', 'r')
text = f.read()                  
f.close()  
def delete_w (text):
    return " ".join(list(filter(lambda x: 'абв' not in x, text.split ())))
print ('урезанный текст: ', delete_w(text))
with open ('file4.txt', 'w') as data:        
    data.write(delete_w(text))

'''Задача 2  Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
 Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
 Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"

'''
print ('\nИгра кто последний заберет конфеты, тот -  выиграл!\n')
from random import randint

def play_candy (num_candy_ost, num_candy_take):
    print ('Игра кто последний заберет конфеты, тот -  выиграл!\n')
    count = 0 
    curr_player_turn = 0
    flag = True
    flag1 = 0
    
   
    print (f"Кол конфет в кучке: {num_candy_ost}, можно взять от 1 до {num_candy_take} конф.\n")
    while True:
        count += 1
        if num_candy_ost <= num_candy_take:
            print (f"Ход №{count} от БОТА: взял {num_candy_ost} конф., БОТ ПОБЕДИЛ!!!\n")
            break
# 1 - ый ход 
        if count == 1 :                                                             
            turn = randint(1, num_candy_take)
            flag = False
            num_candy_ost -= turn
            print (f"Ход №{count} от БОТА: взял {turn} конф. В кучке {num_candy_ost} конф.")    
# ходы последующие
        else:
            if num_candy_ost % (num_candy_take + 1) != 0:
                flag = True   
                if flag1 == 0:                                                               #флаг - перелом игры, компьютер поменял стратегию игры
                    print ("---ВЫ ОШИБЛИСЬ! БОТ МЕНЯЕТ СТРАТЕГИЮ, НАЧИНАЕТ ВЫИГРЫВАТЬ----\n")
                    flag1 += 1
            turn = num_candy_ost % (num_candy_take + 1) if flag == True else randint(1, num_candy_take)
            num_candy_ost -= turn
            flag1 = False
            print (f"Ход №{count} от БОТА: взял {turn} конф. В кучке {num_candy_ost} конф.")
        
        count += 1
        if (flag == True):
            print (f"Введите количество конф. ")
        else:
            print (f"Введите количество конф. Чтобы выиграть надо взять: {num_candy_ost % (num_candy_take + 1)} конф.")
        curr_player_turn = int (input())
        
        while curr_player_turn < 1 or  curr_player_turn > num_candy_take:
            print (f'Количество конфет должно быть от 1 до {num_candy_take}  повторите ввод: ')
            curr_player_turn = int (input())
            
        num_candy_ost -= curr_player_turn

        if num_candy_ost == 0:
            print ("ВЫ ПОБЕДИЛИ!")
            break
        else:
            print (f" Ход №{count} от игрока: берет {curr_player_turn}  конф. В кучке {num_candy_ost} конф. \n")
           
play_candy (int (input ('введите исходное кол конфет: ')), int (input ('введите макс кол конфет, которое можно взять: ')))


'''Задача 3  Создайте программу для игры в "Крестики-нолики".
'''

board = list(range(1,10))                               # формирование поля из списка - 9 значений
print('\nИГРА КРЕСТИКИ - НОЛИКИ\n')

def draw_board(board):                                  # метод визуализации доски крестики нолики на консоле
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):                           # метод ввода данных в игру X или O, изменение списка board (проставляются X и O)
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята, повторите ввод")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):                                       # метод проверки игрового поля
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:                          # символы во всех трех сиволах равны, то возвращается символ победителя
            return board[each[0]]
    return False

def main(board):                                                    # метод реализации игры крестики нолики с помощью встроенных методов 
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp == 'X' or tmp == 'Y':
                print (f'\n {tmp} выиграл!')
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

main(board)


''' Задача 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
'''

print ('Задача 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.')

import random
import string
def main():
    def generate_random_string(length):
        letters = 'FC'
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string
    rle = generate_random_string(200)
    
    encoded = encode(rle)
    decoded = decode(encoded)
 
    print("Test Vector: " + rle)
    with open ('text1.txt', 'w') as f:        
        f.write(rle)
    print("Encoded Result: " + formatOutput(encoded))
    with open ('text2.txt', 'w') as f:        
        f.write(formatOutput(encoded))
    print("Decoded Result: " + decoded)
 
def encode(sequence):
    """Encode a sequence of characters and return the result as a list of tuples (data value and number of observed instances of value).
    Keyword arguments:
    sequence -- a sequence of characters to encode represented as a string.
    """
    count = 1
    result = []
 
    for x,item in enumerate(sequence): 
        if x == 0:
            continue
        elif item == sequence[x - 1]:
            count += 1
        else:        
            result.append((sequence[x - 1], count))
            count = 1            
    
    result.append((sequence[len(sequence) - 1], count))
 
    return result
 
 
def decode(sequence):
    """Decodes the sequence and returns the result as a string.
    Keyword arguments:
    sequence -- a list of tuples (data value and number of observed instances of value).
    """
    result = []
 
    for item in sequence:
        result.append(item[0] * item[1])
 
    return "".join(result)
 
 
def formatOutput(sequence):
    """Returns a print friendly version of the encoded data. 
    Keyword arguments:
    sequence -- list of tuples (data value and number of observed instances of value).
    """
    result = []
 
    for item in sequence:
        if (item[1] == 1):
            result.append(item[0])
        else:
            result.append(str(item[1]) + item[0])
 
    return "".join(result)
    
 
if __name__ == "__main__":
    main()
