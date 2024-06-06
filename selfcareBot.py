import telebot
import datetime
import time
import threading


bot = telebot.TeleBot('Введите токен')


@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(message.chat.id, 'Привет! \nЯ бот, который поможет тебе заботиться о своих базовых потребностях. \nЯ умею напоминать пить воду, принимать пищу, а также пить полезные БАДы 🙌🏻 \nВсе это поможет тебе чувствовать себя хорошо 🤍')
    reminder_thread1 = threading.Thread(target=send_water_reminder, args=(message.chat.id,))
    reminder_thread2 = threading.Thread(target=send_supplement_reminder, args=(message.chat.id,))
    reminder_thread3 = threading.Thread(target=send_food_reminder, args=(message.chat.id,))
    reminder_thread1.start()
    reminder_thread2.start()
    reminder_thread3.start()


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Если у тебя есть какие-то проблемы с ботом, напиши, пожалуйста @example1 \nМы обязательно тебе поможем!')


@bot.message_handler(commands=['menu'])
def menu_message(message):
    bot.send_message(message.chat.id, 'Давай посмотрим, какие функции у меня есть: '
                                      '\n/start - начало работы бота'
                                      '\n/help - помощь, если появились проблемы'
                                      '\n/menu - основные функции, которые есть в боте'
                                      '\n/water_info - факты о полезности воды'
                                      '\n/water_reminder - как я буду напоминать пить воду'
                                      '\n/supplement_reminder - какое расписание принятия БАДов'
                                      '\n/food_reminder - с какой регулярностью необходимо питаться')


@bot.message_handler(commands=['water_info'])
def water_info(message):
    bot.send_message(message.chat.id, 'А ты знаешь, почему так важно пить воду? \nЛови несколько фактов о полезности воды! \n\n'
                                      'Вода является основным компонентом нашего тела, составляя около 60% его массы, и играет критически важную роль в поддержании жизнедеятельности:'
                                      '\n🌀 Когда организм хорошо гидратирован, процессы метаболизма идут быстрее, что способствует увеличению уровня энергии. Это помогает чувствовать себя бодрее и активнее в течение дня.'
                                      '\n🌀 Питье воды помогает поддерживать баланс химических веществ в мозге, улучшая настроение и эмоциональное состояние.'
                                      '\n🌀 Вода помогает поддерживать оптимальный объем крови, улучшая транспортировку кислорода и питательных веществ к клеткам, что снижает усталость и повышает выносливость.'
                                      '\n\nРегулярное потребление достаточного количества воды — это простой, но эффективный способ поддержания здоровья, улучшения настроения и повышения энергии.'
                                      '\n\nПоэтому я обязательно буду напоминать тебе пить воду!\nДля того, чтобы узнать, как это работает, нажми /water_reminder')


@bot.message_handler(commands=['water_reminder'])
def water_rem(message):
    bot.send_message(message.chat.id, 'Для здоровья организма рекомендуется выпивать 2-3 литра воды в день! Это соответствует примерно 8-12 стаканам по 250 мл.'
                                      '\n\nЯ буду напоминать тебе пить воду 9 раз в день - каждые 1,5 часа, начиная с 09:00.\n\nКогда в организме будет достаточное количество воды, ты будешь отлично себя чувствовать 🍀')


@bot.message_handler(commands=['supplement_reminder'])
def supplement_rem(message):
    bot.send_message(message.chat.id, 'По показаниям врача есть 2 основные добавки, которые тебе рекомендуется принимать - это витамин Д и омега.\nОб их приеме я буду напоминать каждое утро в 09:30.'
                                      '\n\nДля хорошего самочувствия вечером отлично подходит теплый чай с медом и ромашкой.\nОб этом ты увидишь напоминание в 21:30.')


@bot.message_handler(commands=['food_reminder'])
def food_rem(message):
    bot.send_message(message.chat.id, 'Дисциплина - наше все. Особенно в случае насыщения организма необходимыми компонентами.'
                                      '\n\nНапоминание о принятии пищи будет приходить каждые 2,5 часа, начиная с 08:30.')


def send_water_reminder(chat_id):
    send1 = "20:05:30"
    send2 = "10:30"
    send3 = "12:00"
    send4 = "13:30"
    send5 = "15:00"
    send6 = "16:30"
    send7 = "18:00"
    send8 = "19:30"
    send9 = "21:00"
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == send1 or now == send2 or now == send3 or now == send4 or now == send5 or now == send6 or now == send7 or now == send8 or now == send9:
            bot.send_message(chat_id, 'Пора попить водички!\n\n🌀🌀🌀')
            time.sleep(61)
        time.sleep(1)


def send_supplement_reminder(chat_id):
    send01 = "20:05:45"
    send02 = "21:30"
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == send01:
            bot.send_message(chat_id, 'Доброе утро!☀️\n\nДля поддержания здоровья организма самое время принять витамин Д и омегу.')
            time.sleep(61)
        elif now == send02:
            bot.send_message(chat_id,'И снова вечер! День подходит к концу.\n\nДля хорошего сна и самочувствия можно выпить чай с медом и ромашкой 🌇')
            time.sleep(61)
        time.sleep(1)


def send_food_reminder(chat_id):
    send001 = "20:06:00"
    send002 = "11:00"
    send003 = "13:30"
    send004 = "16:00"
    send005 = "18:30"
    send006 = "21:00"
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == send001:
            bot.send_message(chat_id, '... и доброе утро! Завтрак тебя ждет!')
            time.sleep(61)
        elif now == send003:
            bot.send_message(chat_id, 'Самое время подкрепиться - время обеда!')
            time.sleep(61)
        elif now == send005:
            bot.send_message(chat_id, 'Ужин, однако, это прекрасно. Не забудь про него!')
            time.sleep(61)
        elif now == send002 or now == send004 or now == send006:
            bot.send_message(chat_id,'Время перекуса!\n\n🍓🥪🍪')
            time.sleep(61)
        time.sleep(1)


bot.polling(none_stop=True)