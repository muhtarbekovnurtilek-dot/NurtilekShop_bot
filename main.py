import telebot
from telebot import types

TOKEN = "8469117365:AAHBuPCMromQLJoEuagEZ9es5TQQ7B6koYs"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("💎 Free Fire")
    btn2 = types.KeyboardButton("🪖 PUBG Mobile")
    btn3 = types.KeyboardButton("⭐ Telegram Stars")
    btn4 = types.KeyboardButton("📞 Заказать")

    markup.add(btn1, btn2)
    markup.add(btn3, btn4)

    bot.send_message(
        message.chat.id,
        "🔥 Добро пожаловать в Nurtilek Shop 💎\n\n"
        "🎮 Донат в игры\n"
        "⚡ Быстро и безопасно\n"
        "💬 Поддержка: @nurt1lek_ff",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: True)
def buttons(message):

    if message.text == "💎 Free Fire":
        bot.send_message(message.chat.id, "💎 Free Fire донат\n\nПрайс скоро добавим")

    elif message.text == "🪖 PUBG Mobile":
        bot.send_message(message.chat.id, "🪖 PUBG Mobile донат\n\nПрайс скоро добавим")

    elif message.text == "⭐ Telegram Stars":
        bot.send_message(message.chat.id, "⭐ Telegram Stars\n\nПрайс скоро добавим")

    elif message.text == "📞 Заказать":
        bot.send_message(
            message.chat.id,
            "📩 Для заказа пиши сюда:\n@nurt1lek_ff"
        )


print("Бот запущен...")
bot.infinity_polling()
