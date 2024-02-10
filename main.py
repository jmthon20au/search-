import telebot
import requests
token = '6409265475:AAHcWjQp0cw_9LNIbZmy93sE-hxUJ8wJGGU'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='المطور', url="https://t.me/altaee_z"))
    bot.reply_to(message,'''- Welcome To WallCraft Bot

- This Bot Give You The Best WallPapers About Anything You Want

- أرسل كلمة لجلب الصور الخاصة بها ''',reply_markup=markup)
@bot.message_handler(func=lambda message: True)
def handle_image_request(message):
    word = message.text
    amnt = 10
    res = requests.get(f'https://api-uc.wallpaperscraft.com/images?screen[width]\u003d720\u0026screen[height]\u003d1440\u0026lang\u003den\u0026limit\u003d{amnt}\u0026types[]\u003dfree\u0026types[]\u003dprivate\u0026offset\u003d60\u0026query\u003d{word}\u0026cost_variant\u003dandroid_cost_1\u0026sort\u003drating\u0026uploader_types[]\u003dwlc\u0026uploader_types[]\u003duser\u0026uploader_types[]\u003dwlc_ai_art').json()['items']
    for i, item in enumerate(res):
        url = item['variations']['adapted']['url']
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='قناة تحديثات البوت', url="https://t.me/my00002"))
        bot.send_photo(message.chat.id, photo=url,reply_markup=markup)
bot.polling()
