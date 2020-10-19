from telebot import *
from telebot.types import *
from rextester_py import rexec

bot = TeleBot("1252694259:AAFYgBplceKvun37jLw21ET5aSKDjE42a2w")


@bot.message_handler(commands=['start'])
def welcome(message):
    url = "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/d1c73083904463.5d4ad074b6673.png"
    bot.send_photo(
        message.chat.id,photo=url,
        caption="<a href='https://github.com/000bakhtiyor'>Dastur kodi Githubdagi sahifada</a>\n\n<b>![Dasturlash_Tili]@[Kod]</b>\n\n<b><i>Misol :</i></b>  <b>!</b>python 3<b>@</b>print('hello world!')",
        parse_mode='html',
        )


@bot.message_handler(content_types=["text"])
def functions(message):
    try:
        if message.text[0]=="!":
            code = message.text[1:].split("@")
        
            bot.send_message(
                message.chat.id,
                text = rexec("{0}".format(code[0]), "{0}".format(code[1]), None).results,
                parse_mode='html'
            )
    except Exception as e:
            bot.send_message(
                message.chat.id,
                text = repr(e),
                parse_mode='html'
            )
    



bot.polling(none_stop=True)
