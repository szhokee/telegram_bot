import telebot
import random
from env import TOKEN

bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Yes')
button2 = telebot.types.KeyboardButton('No')
keyboard.add(button1, button2)




@bot.message_handler(commands=['start', 'hi'])
def start_function(message):

    
    msg = bot.send_message(message.chat.id, f'Привет {message.chat.first_name} начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(msg, answer_check)
    # bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJKYWOhPd8Q1IpF8sSABDlwjVJ3WCchAAJADgACK4PQSwb_vzMw9kX2LAQ')
    # bot.send_photo(message.chat.id, 'https://scontent.ffru2-1.fna.fbcdn.net/v/t39.30808-6/319645361_832496658043508_9121464079663942004_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=OUej9VqoWCsAX-SidZg&_nc_ht=scontent.ffru2-1.fna&oh=00_AfDOhNZlOi_8r1OankYJnwSCW78bGK055U2aij1qPyZKGQ&oe=63A712A0')

def answer_check(msg):
    if msg.text == 'Yes':
        bot.send_message(msg.chat.id, 'У тебя есть 3 попытки угадать число от 1 до 10')
        random_number = random.randint(1,10)
        p = 3                                       # попытки
        start_game(msg, random_number, p)

    else:
        bot.send_message(msg.chat.id, 'Its ok')
       
    # print(msg.text)

def start_game(msg, random_number, p):
    msg = bot.send_message(msg.chat.id, 'Введи число от 1 до 10: ')
    bot.register_next_step_handler(msg, check_func, random_number, p-1)


def check_func(msg, random_number, p):
    if msg.text == str(random_number):
        bot.send_message(msg.chat.id, 'Вы победили!')
    elif p == 0:
        bot.send_message(msg.chat.id, f'Вы проиграли! Число было - {random_number}')
    else:
        bot.send_message(msg.chat.id, f'Попробуй ещё раз, у тебя осталось {p} попыток')
        start_game(msg, random_number, p)




# @bot.message_handler()
# def echo_all(message):
#     bot.send_message(message.chat.id, message.text) #popugai

bot.polling()


# git init
# git add .
# git commit -m 'names commit'
# git remote add origin ss/https
# git push origin master