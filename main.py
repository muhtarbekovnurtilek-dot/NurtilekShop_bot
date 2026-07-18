import telebot

TOKEN = "8469117365:AAHBuPCMromQLJoEuagEZ9es5TQQ7B6koYs"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🔥 Nurtilek Shop работает!")

print("Бот запущен")

bot.infinity_polling()
