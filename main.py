import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import telebot
from telebot import types
import urllib.parse

# Токен автоматтык түрдө Render'дин Environment бөлүмүнөн алынат
TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)

# --- ВЕБ-СЕРВЕР ДЛЯ RENDER (ПОРТ КАТАСЫ БОЛБОШ ҮЧҮН) ---
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot is running successfully!")

def run_health_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), HealthCheckHandler)
    server.serve_forever()
# -----------------------------------------------------------

def create_tg_url(text):
    return f"https://t.me/nurt1lek_ff?text={urllib.parse.quote(text)}"

def main_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("💎 Free Fire", callback_data="ff"),
        types.InlineKeyboardButton("🪖 PUBG Mobile", callback_data="pubg"),
        types.InlineKeyboardButton("⭐ Telegram Stars", callback_data="stars")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🔥 Nurtilek Shop'ко кош келиңиз 💎\n\n"
        "🎮 Оюндарга донат\n"
        "⚡ Тез жана коопсуз\n\n"
        "👇 Бөлүмдү тандаңыз:",
        reply_markup=main_menu()
    )

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "home":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(
            call.message.chat.id,
            "🔥 Nurtilek Shop 💎\n\nБөлүмдү тандаңыз:",
            reply_markup=main_menu()
        )

    elif call.data == "ff":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        b1 = types.InlineKeyboardButton("💎 110 = 85 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: Free Fire\n📦 Товар: 110 Алмаз\n💵 Баасы: 85 сом\n🆔 Менин ID: "))
        b2 = types.InlineKeyboardButton("💎 341 = 270 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: Free Fire\n📦 Товар: 341 Алмаз\n💵 Баасы: 270 сом\n🆔 Менин ID: "))
        b3 = types.InlineKeyboardButton("💎 572 = 450 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: Free Fire\n📦 Товар: 572 Алмаз\n💵 Баасы: 450 сом\n🆔 Менин ID: "))
        b4 = types.InlineKeyboardButton("💎 1166 = 850 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: Free Fire\n📦 Товар: 1166 Алмаз\n💵 Баасы: 850 сом\n🆔 Менин ID: "))
        b5 = types.InlineKeyboardButton("💎 2398 = 1600 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: Free Fire\n📦 Товар: 2398 Алмаз\n💵 Баасы: 1600 сом\n🆔 Менин ID: "))
        b6 = types.InlineKeyboardButton("💎 6160 = 3900 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: Free Fire\n📦 Товар: 6160 Алмаз\n💵 Баасы: 3900 сом\n🆔 Менин ID: "))
        
        v1 = types.InlineKeyboardButton("🎟 Lite (90💎) = 46 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: Free Fire\n📦 Товар: Lite Voucher (90💎)\n💵 Баасы: 46 сом\n🆔 Менин ID: "))
        v2 = types.InlineKeyboardButton("🎟 Weekly (450💎) = 170 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: Free Fire\n📦 Товар: Weekly Voucher (450💎)\n💵 Баасы: 170 сом\n🆔 Менин ID: "))
        v3 = types.InlineKeyboardButton("🎟 Monthly (2600💎) = 799 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: Free Fire\n📦 Товар: Monthly Voucher (2600💎)\n💵 Баасы: 799 сом\n🆔 Менин ID: "))

        markup.add(b1, b2)
        markup.add(b3, b4)
        markup.add(b5, b6)
        markup.add(v1)
        markup.add(v2, v3)
        markup.add(types.InlineKeyboardButton("⬅️ Башкы менюга кайтуу", callback_data="home"))

        text = (
            "🔥 *FREE FIRE ДОНАТ* 🔥\n\n"
            "⚡ *Без задержки түшөт!* ⚡\n"
            "✅ Отзывдар бар\n"
            "🆔 Через ID\n"
            "⚡ 10 секундда түшөт\n\n"
            "👇 Керектүү донатты тандаңыз (басканда дароо личка ачылат):"
        )
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

    elif call.data == "pubg":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        p1 = types.InlineKeyboardButton("💎 60 UC = 95 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: PUBG Mobile\n📦 Товар: 60 UC\n💵 Баасы: 95 сом\n🆔 Менин ID: "))
        p2 = types.InlineKeyboardButton("💎 325 UC = 450 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: PUBG Mobile\n📦 Товар: 325 UC\n💵 Баасы: 450 сом\n🆔 Менин ID: "))
        p3 = types.InlineKeyboardButton("💎 660 UC = 850 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: PUBG Mobile\n📦 Товар: 660 UC\n💵 Баасы: 850 сом\n🆔 Менин ID: "))
        p4 = types.InlineKeyboardButton("💎 1800 UC = 2200 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: PUBG Mobile\n📦 Товар: 1800 UC\n💵 Баасы: 2200 сом\n🆔 Менин ID: "))
        p5 = types.InlineKeyboardButton("💎 3850 UC = 4300 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: PUBG Mobile\n📦 Товар: 3850 UC\n💵 Баасы: 4300 сом\n🆔 Менин ID: "))
        p6 = types.InlineKeyboardButton("💎 8100 UC = 8500 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: PUBG Mobile\n📦 Товар: 8100 UC\n💵 Баасы: 8500 сом\n🆔 Менин ID: "))
        
        s1 = types.InlineKeyboardButton("🎁 Prime (1 ай) = 150 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: PUBG Mobile\n📦 Товар: Prime подпискасы\n💵 Баасы: 150 сом\n🆔 Менин ID: "))
        s2 = types.InlineKeyboardButton("🎁 Prime Plus (1 ай) = 700 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Оюн: PUBG Mobile\n📦 Товар: Prime Plus подпискасы\n💵 Баасы: 700 сом\n700 сом\n🆔 Менин ID: "))

        markup.add(p1, p2)
        markup.add(p3, p4)
        markup.add(p5, p6)
        markup.add(s1, s2)
        markup.add(types.InlineKeyboardButton("⬅️ Башкы менюга кайтуу", callback_data="home"))

        text = (
            "🪖 *PUBG Mobile Донат* (сом)\n\n"
            "👇 Керектүү UC же подписканы тандаңыз:"
        )
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

    elif call.data == "stars":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup(row_width=2)
        st1 = types.InlineKeyboardButton("50 ⭐️ = 91 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Товар: Telegram Stars (50 ⭐️)\n💵 Баасы: 91 сом\n🆔 Менин @username: "))
        st2 = types.InlineKeyboardButton("75 ⭐️ = 130 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Товар: Telegram Stars (75 ⭐️)\n💵 Баасы: 130 сом\n🆔 Менин @username: "))
        st3 = types.InlineKeyboardButton("100 ⭐️ = 170 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Товар: Telegram Stars (100 ⭐️)\n💵 Баасы: 170 сом\n🆔 Менин @username: "))
        st4 = types.InlineKeyboardButton("150 ⭐️ = 255 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Товар: Telegram Stars (150 ⭐️)\n💵 Баасы: 255 сом\n🆔 Менин @username: "))
        st5 = types.InlineKeyboardButton("200 ⭐️ = 335 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Товар: Telegram Stars (200 ⭐️)\n💵 Баасы: 335 сом\n🆔 Менин @username: "))
        st6 = types.InlineKeyboardButton("250 ⭐️ = 410 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Товар: Telegram Stars (250 ⭐️)\n💵 Баасы: 410 сом\n🆔 Менин @username: "))
        st7 = types.InlineKeyboardButton("300 ⭐️ = 495 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Товар: Telegram Stars (300 ⭐️)\n💵 Баасы: 495 сом\n🆔 Менин @username: "))
        st8 = types.InlineKeyboardButton("350 ⭐️ = 575 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Товар: Telegram Stars (350 ⭐️)\n💵 Баасы: 575 сом\n🆔 Менин @username: "))
        st9 = types.InlineKeyboardButton("400 ⭐️ = 660 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Товар: Telegram Stars (400 ⭐️)\n💵 Баасы: 660 сом\n🆔 Менин @username: "))
        st10 = types.InlineKeyboardButton("450 ⭐️ = 735 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Товар: Telegram Stars (450 ⭐️)\n💵 Баасы: 735 сом\n🆔 Менин @username: "))
        st11 = types.InlineKeyboardButton("500 ⭐️ = 815 сом", url=create_tg_url("Салам! Заказ берейин дегем:\n🎮 Товар: Telegram Stars (500 ⭐️)\n💵 Баасы: 815 сом\n🆔 Менин @username: "))

        markup.add(st1, st2)
        markup.add(st3, st4)
        markup.add(st5, st6)
        markup.add(st7, st8)
        markup.add(st9, st10)
        markup.add(st11)
        markup.add(types.InlineKeyboardButton("⬅️ Башкы менюга кайтуу", callback_data="home"))

        text = (
            "Донат ⭐️ *Telegram'га @username аркылуу* 🔥 (сом менен)\n\n"
            "❗️ Бул чек эмес, мындан көп дагы киргизип беребиз.\n\n"
            "👇 Керектүү жылдызча санын тандаңыз:"
        )
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

    bot.answer_callback_query(call.id)

# --- ЗАПУСК БОТА И ВЕБ-СЕРВЕРА ---
if __name__ == '__main__':
    threading.Thread(target=run_health_server, daemon=True).start()
    bot.infinity_polling()
