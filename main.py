import telebot

# 1. Создаем бота (замени ТЕКСТ_В_КАВЫЧКАХ на свой токен)
bot = telebot.TeleBot("8469117365:AAHBuPCMromQLJoEuagEZ9es5TQQ7B6koYs")

# 2. Пример обработчика команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой новый бот NurtilekShop_bot.")

# 3. Пример обработчика простого текста
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Вы сказали: {message.text}")

# 4. Эта строчка ОБЯЗАТЕЛЬНО должна быть в самом конце файла
if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
