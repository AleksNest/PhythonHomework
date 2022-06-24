from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler


bot = Bot(token='5594488827:AAG1tLzTOpSE1_tEABaf43GT3uf0iukcGdI')
updater = Updater(token='5594488827:AAG1tLzTOpSE1_tEABaf43GT3uf0iukcGdI', use_context=True)
dispatcher = updater.dispatcher

START = 1
DATE0 = 2
DATE1 = 3
DATE2 = 4
DATE3 = 5
DATE4 = 6

    
  
def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'КАЛЬКУЛЯТОР  ')
    context.bot.send_message(update.effective_chat.id, '/start - запуск калькулятора')
    context.bot.send_message(update.effective_chat.id, 'выбирете тип чисел: 1 - рациональные, 2 - комплексные  ')
    
    return START


def input_data_0(update, context):
    global type_number
    type_number = update.message.text
    if type_number == '1':
        context.bot.send_message(update.effective_chat.id, 'Введи арифметическое выражение без знака "=": ')
        
    else:
        context.bot.send_message(update.effective_chat.id, 'Введи действительную часть первого числа: ')

    return DATE0


    
def input_data_1(update, context):
    global first_number_dv
    if type_number == '1':
        calc = update.message.text
        print(calc)
        rezult = eval (calc)
        context.bot.send_message(update.effective_chat.id, f'результат: {rezult}')
        return ConversationHandler.END
    else:
        first_number_dv = update.message.text
        print(first_number_dv)
        context.bot.send_message(update.effective_chat.id, 'Введи мнимую часть первого числа: ')

    return DATE1


def input_data_2(update, context):
    global first_number_mn
    if type_number != '1':
        first_number_mn = update.message.text
        print(first_number_mn)
        context.bot.send_message(update.effective_chat.id, 'Введите действительную часть второго числа: ')

    return DATE2

def input_data_3(update, context):
    global second_number_dv
    if type_number != '1':
        second_number_dv = update.message.text
        print(second_number_dv)
        context.bot.send_message(update.effective_chat.id, 'Введи мнимую часть второго числа: ')

    return DATE3



def input_data_4(update, context):
    global second_number_mn
    if type_number != '1':
        second_number_mn = update.message.text
        print(second_number_mn)
        context.bot.send_message(update.effective_chat.id, 'Введи арифметическую операцию : ')

    return  DATE4

def operation(update, context):
    if type_number != '1':
        text = update.message.text
        if text == '+':
            date_mn = float(first_number_mn) + float(second_number_mn)
            date_dv = float(first_number_dv) + float(second_number_dv)
            if date_mn > 0:
                rezult = str(date_dv)+'+'+str(date_mn)+'i'
            else:
                rezult = str(date_dv)+str(date_mn)+'i'
            context.bot.send_message(update.effective_chat.id, f'результат: {rezult}')
        elif text == '*':
            date_mn = float(first_number_dv)*float(second_number_mn)+float(second_number_dv)*float(first_number_mn)
            date_dv = float(first_number_dv) * float(second_number_dv)-float(first_number_mn)*float(second_number_mn)
            if date_mn > 0:
                rezult = str(date_dv)+'+'+str(date_mn)+'i'
            else:
                rezult = str(date_dv)+str(date_mn)+'i'
            context.bot.send_message(update.effective_chat.id, f'результат: {rezult}')
        elif text == '/':
            date_mn = float(first_number_mn) / float(second_number_mn)
            date_dv = float(first_number_dv) / float(second_number_dv)
            if date_mn > 0:
                rezult = str(date_dv)+'+'+str(date_mn)+'i'
            else:
                rezult = str(date_dv)+str(date_mn)+'i'
            context.bot.send_message(update.effective_chat.id, f'результат: {rezult}')
        elif text == '-':
            date_mn = float(first_number_mn) - float(second_number_mn)
            date_dv = float(first_number_dv) - float(second_number_dv)
            if date_mn > 0:
                rezult = str(date_dv)+'+'+str(date_mn)+'i'
            else:
                rezult = str(date_dv)+str(date_mn)+'i'
            context.bot.send_message(update.effective_chat.id, f'результат: {rezult}')

    return ConversationHandler.END


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'выход из калькулятора')
    return ConversationHandler.END

 
start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
zero_handler = MessageHandler(Filters.text, input_data_0)
first_handler = MessageHandler(Filters.text, input_data_1)
second_handler = MessageHandler(Filters.text, input_data_2)
third_handler = MessageHandler(Filters.text, input_data_3)
fourth_handler = MessageHandler(Filters.text, input_data_4)
operation_handler = MessageHandler(Filters.text, operation)


conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states={START: [zero_handler],
                                            DATE0: [first_handler],
                                            DATE1: [second_handler],
                                            DATE2: [third_handler],
                                            DATE3: [fourth_handler],
                                            DATE4: [operation_handler],},
                                    fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler) 
print ('server start')
updater.start_polling()
updater.idle()