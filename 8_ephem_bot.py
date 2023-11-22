"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import os
from datetime import date
import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("bot_token")


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


constellation_for_planet = date.today()
str_constellation_for_planet = str(constellation_for_planet).replace("-", "/")
planets = {"Mercury": ephem.Mercury(str_constellation_for_planet), "Venus": ephem.Venus(str_constellation_for_planet),
           "Mars": ephem.Mars(str_constellation_for_planet), "Jupiter": ephem.Jupiter(str_constellation_for_planet),
           "Saturn": ephem.Saturn(str_constellation_for_planet), "Uranus": ephem.Uranus(str_constellation_for_planet),
           "Neptune": ephem.Neptune(str_constellation_for_planet)}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text("Список доступных комманд /commands")


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def commands(update, context):
    update.message.reply_text(
        """
        /planet Выберите планету Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune (пример: /planet Saturn)
        """
    )


def find_planet(update, context):
    get_planet_name = update.message.text.split()[1]
    check_planet = planets.get(get_planet_name)
    if check_planet != None:
        planet_constellation = ephem.constellation(planets[get_planet_name])
        update.message.reply_text(f"Планета {get_planet_name} в созвездии {planet_constellation[1]}")
    else:
        update.message.reply_text(f"Планета {get_planet_name} не найдена, попробуйте еще раз")


def main():
    mybot = Updater(token, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("commands", commands))
    dp.add_handler(CommandHandler("planet", find_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
