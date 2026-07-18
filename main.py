import telebot

TOKEN = 8469117365:AAHBuPCMromQLJoEuagEZ9es5TQQ7B6koYs

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🔥 Добро пожаловать в Nurtilek Shop 💎\n\n"
        "Донат Free Fire, PUBG и другие игры.\n"
        "Пиши для заказа!"
    )

@bot.message_handler(func=lambda message: True)
def text(message):
    bot.send_message(
        message.chat.id,
        "Спасибо за сообщение! Скоро отвечу ✅"
    )

print("Бот запущен!")

bot.infinity_polling()
