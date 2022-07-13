import telebot
from config import TOKEN, currenc
from extensions import APIException, MoneyExchange

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'starty'])
def help_command(message):
    reply = 'Что бы начать пользоваться ботом введите сообщение вида:\n' \
            '<имя валюты цену которой нужно узнать>\n' \
            '<имя валюты в которой надо узнать цену первой валюты>\n' \
            '<количество первой валюты>\n' \
            'Что бы узнать доступные валюты наберите /values'
    bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=['values'])
def values(message):
    currency = ',\n'.join([i.capitalize() for i in currenc.keys()])
    reply = 'Виды доступых валют для конвертирования:\n' + currency + '.'
    bot.send_message(message.chat.id, reply)


@bot.message_handler(content_types=['text'])
def converter(message):
    input_info = message.text.split(' ')
    try:
        if len(input_info) != 3:
            raise APIException('Введено некорректное значение')
        first_currency, second_currency, amount = input_info
        return_amount = exchanger.exchange_money(first_currency, second_currency, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка при вводе: {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду {e}')
    else:
        reply = f'За {amount} {first_currency} вы получите {return_amount} {second_currency}'
        bot.send_message(message.chat.id, reply)


if __name__ == '__main__':
    exchanger = MoneyExchange()
    bot.polling(none_stop=True)
