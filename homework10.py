from random import randint
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler

bot = Bot(token='5594488827:AAG1tLzTOpSE1_tEABaf43GT3uf0iukcGdI')
updater = Updater(token='5594488827:AAG1tLzTOpSE1_tEABaf43GT3uf0iukcGdI', use_context=True)
dispatcher = updater.dispatcher

global num_candy1, num_candy2, num_candy3
print ('\nИгра кто последний заберет конфеты, тот -  выиграл!\n')

from random import randint

def command_start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет, я бот хочешь сыграть в игру? Кто последний заберет конфеты - тот выиграл. ')
    context.bot.send_message(update.effective_chat.id, 'Выбери исходное кол конфет: /kol "кол"')

print ('\nИгра кто последний заберет конфеты, тот -  выиграл!\n')

def command_input1(update, context):   
    global num_candy1
    num_candy1 = context.args
    print (f'исходное кол кофет {num_candy1}')
    context.bot.send_message(update.effective_chat.id, 'введите максимальное кол конфет, которое можно брать: /max "кол"')

def command_input2(update, context):   
    global num_candy2, num_candy_ost, num_candy_take, count, turn, curr_player_turn, num_candy3
    num_candy2 = context.args
    print (f'максимальное кол конфет {num_candy2}')

# def command_input3(update, context):   
#     global num_candy3
#     num_candy3 = context.args
#     print (f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
   


   

    num_candy_ost = int (num_candy1[0])
    num_candy_take= int (num_candy2[0])   

    from random import randint

    count = 0 
    curr_player_turn = 0
    flag = True
    flag1 = 0


    print (f"Кол конфет в кучке: {num_candy_ost}, можно взять от 1 до {num_candy_take} конф.\n")
    context.bot.send_message(update.effective_chat.id, f"Кол конфет в кучке: {num_candy1}, можно взять от 1 до {num_candy2} конф.")

    while True:
        count += 1
        if num_candy_ost <= num_candy_take:
            print (f"Ход №{count} БОТ взял {num_candy_ost} конф., БОТ ПОБЕДИЛ!!!\n")
            context.bot.send_message(update.effective_chat.id, f"Ход №{count} БОТ: взял {num_candy_ost} конф., БОТ ПОБЕДИЛ!!!")
            break
    # 1 - ый ход 
        if count == 1 :                                                             
            turn = randint(1, num_candy_take)
            flag = False
            num_candy_ost -= turn
            print (f"Ход №{count} БОТ взял {turn} конф. В кучке {num_candy_ost} конф.")  
            context.bot.send_message(update.effective_chat.id, f"Ход №{count} БОТ взял {turn} конф. В кучке {num_candy_ost} конф.")  
    # ходы последующие
        else:
            if num_candy_ost % (num_candy_take + 1) != 0:
                flag = True   
                if flag1 == 0:                                                               #флаг - перелом игры, компьютер поменял стратегию игры
                    print ("---ВЫ ОШИБЛИСЬ! БОТ МЕНЯЕТ СТРАТЕГИЮ, НАЧИНАЕТ ВЫИГРЫВАТЬ----\n")
                    context.bot.send_message(update.effective_chat.id, "---ВЫ ОШИБЛИСЬ! БОТ МЕНЯЕТ СТРАТЕГИЮ, НАЧИНАЕТ ВЫИГРЫВАТЬ----")
                    flag1 += 1
            turn = num_candy_ost % (num_candy_take + 1) if flag == True else randint(1, num_candy_take)
            num_candy_ost -= turn
            flag1 = False
            print (f"Ход №{count} БОТ взял {turn} конф. В кучке {num_candy_ost} конф.")
            context.bot.send_message(update.effective_chat.id, f"Ход №{count}  БОТ взял {turn} конф. В кучке {num_candy_ost} конф.")
        
        count += 1
        if (flag == True):
            print (f"Введите количество конф. ")
            context.bot.send_message(update.effective_chat.id, f"Введите количество конф. ")
        else:
            print (f"Введите количество конф. Чтобы выиграть надо взять: {num_candy_ost % (num_candy_take + 1)} конф.")
            context.bot.send_message(update.effective_chat.id, f"Введите количество конф. Чтобы выиграть надо взять: {num_candy_ost % (num_candy_take + 1)} конф.")
        
        



        curr_player_turn = int(input())   # ВВОД ПОЛЬЗОВАТЕЛЯ 
        



        while curr_player_turn < 1 or  curr_player_turn > num_candy_take:
            print (f'Количество конфет должно быть от 1 до {num_candy_take}  повторите ввод: ')
            context.bot.send_message(update.effective_chat.id, f'Количество конфет должно быть от 1 до {num_candy_take}  повторите ввод: ')
            


            
            curr_player_turn = int(input())   # ВВОД ПОЛЬЗОВАТЕЛЯ
            
        


        num_candy_ost -= curr_player_turn

        if num_candy_ost == 0:
            print ("ВЫ ПОБЕДИЛИ!")
            context.bot.send_message(update.effective_chat.id, "ВЫ ПОБЕДИЛИ!")
            break
        else:
            print (f" Ход №{count} Вы взяли: {curr_player_turn}  конф. В кучке {num_candy_ost} конф. \n")
            context.bot.send_message(update.effective_chat.id, f" Ход №{count} Вы взяли: {curr_player_turn}  конф. В кучке {num_candy_ost} конф.")
            

updater.dispatcher.add_handler(CommandHandler('start', command_start))
updater.dispatcher.add_handler(CommandHandler('kol', command_input1))
updater.dispatcher.add_handler(CommandHandler('max', command_input2))
#updater.dispatcher.add_handler(CommandHandler('vvod', command_input3))



print ('server start')
updater.start_polling()
updater.idle()