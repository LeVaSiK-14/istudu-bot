import telebot
from constant import text_program, text_english_new, text_comp, token, text_arab, text_english_child, text_english_pro, text_kurg_teenager, text_kyrg_child, school, ORT, text_maths, contacts, geo_url
from telebot import types
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    btn_my_site = types.InlineKeyboardButton(text='наше местоположение', url=geo_url)
    keyboard.add('англ.яз для начинающих', 'англ.яз для продолжающих', 'англ.яз для детей')
    keyboard.add('Програмирование', 'Компютерные курсы', 'Кырг.яз для детей')
    keyboard.add('Кырг.яз для подростков', 'Арабский язык', 'подготовка к школе')
    keyboard.add('подготовка к орт', 'курсы математики', 'наши контакты', btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'англ.яз для начинающих':
        bot.send_message(message.chat.id, text_english_new)
    elif message.text.lower() == 'англ.яз для продолжающих':
        bot.send_message(message.chat.id, text_english_pro)
    elif message.text.lower() == 'англ.яз для детей':
        bot.send_message(message.chat.id, text_english_child)
    elif message.text.lower() == 'програмирование':
        bot.send_message(message.chat.id, text_program)
    elif message.text.lower() == 'компютерные курсы':
        bot.send_message(message.chat.id, text_comp)
    elif message.text.lower() == 'кырг.яз для детей':
        bot.send_message(message.chat.id, text_kyrg_child)
    elif message.text.lower() == 'кырг.яз для подростков':
        bot.send_message(message.chat.id, text_kurg_teenager)
    elif message.text.lower() == 'арабский язык':
        bot.send_message(message.chat.id, text_arab)
    elif message.text.lower() == 'подготовка к школе':
        bot.send_message(message.chat.id, school)
    elif message.text.lower() == 'подготовка к орт':
        bot.send_message(message.chat.id, ORT)
    elif message.text.lower() == 'курсы математики':
        bot.send_message(message.chat.id, text_maths)
    elif message.text.lower() == 'наши контакты':
        bot.send_message(message.chat.id, contacts)
    elif message.text.lower() == 'наше местоположение':
        bot.send_message(message.chat.id, geo_url)
    else:
        bot.send_message(message.chat.id, 'ивините, но я вас не понимаю вы какие-то странные')



bot.polling()