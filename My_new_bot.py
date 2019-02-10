import telebot
import datetime
import misc
import Min_fin

bot = telebot.TeleBot(misc.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе

    if '/' in message.text and len(message.text) >2 and today == now.day:
        bot.send_message(message.chat.id, 'Здравствуйте, {}'.format(message.chat.first_name))
        try:
            result = Min_fin.main(message.text)
            bot.send_message(message.chat.id, 'For {}: {}'.format(message.text[1:], result))

        except:
            bot.send_message(message.chat.id, 'Не удалось выполнить. До свидания, {}'.format(message.chat.first_name))
    else:
        bot.send_message(message.chat.id, 'Здравствуйте, {}'.format(message.chat.first_name))


if __name__ == '__main__':

    now = datetime.datetime.now()
    today = now.day
    hour = now.hour
    bot.polling(none_stop=True)