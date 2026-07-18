import telebot
from telebot import types

TOKEN = "8469117365:AAHBuPCMromQLJoEuagEZ9es5TQQ7B6koYs"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("💎 Free Fire", callback_data="ff")
    btn2 = types.InlineKeyboardButton("🪖 PUBG Mobile", callback_data="pubg")
    btn3 = types.InlineKeyboardButton("⭐ Telegram Stars", callback_data="stars")
    btn4 = types.InlineKeyboardButton("📞 Заказать", callback_data="order")

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn4)

    bot.send_message(
        message.chat.id,
        "🔥 Добро пожаловать в Nurtilek Shop 💎\n\n"
        "🎮 Донат в игры\n"
        "⚡ Быстрое выполнение\n"
        "✅ Безопасно\n\n"
        "Выберите нужный раздел 👇",
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "ff":
        bot.send_message(call.message.chat.id, "💎 Free Fire\nПрайс скоро добавим")

    elif call.data == "pubg":
        bot.send_message(call.message.chat.id, "🪖 PUBG Mobile\nПрайс скоро добавим")

    elif call.data == "stars":
        bot.send_message(call.message.chat.id, "⭐ Telegram Stars\nПрайс скоро добавим")

    elif call.data == "order":
        bot.send_message(
            call.message.chat.id,
            "📩 Для заказа пишите:\n@nurt1lek_ff"
        )


print("Бот запущен...")
bot.infinity_polling()
