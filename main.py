import telebot
from telebot import types

# ⚠️ Бул жерге @BotFather берген токенди жазыңыз
TOKEN = "8469117365:AAHBuPCMromQLJoEuagEZ9es5TQQ7B6koYs"

bot = telebot.TeleBot(TOKEN)

# Негизги меню (төмнкү баскычтар)
def get_main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("💎 Free Fire")
    btn2 = types.KeyboardButton("🪖 PUBG Mobile")
    btn3 = types.KeyboardButton("⭐ Telegram Stars")
    btn4 = types.KeyboardButton("📞 Заказ берүү")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🔥 Nurtilek Shop'ко кош келиңиз 💎\n\n"
        "🎮 Оюндарга донат\n"
        "⚡ Тез жана коопсуз\n"
        "💬 Колдоо кызматы: @nurt1lek_ff",
        reply_markup=get_main_keyboard()
    )

@bot.message_handler(func=lambda message: True)
def buttons(message):
    # --- FREE FIRE МЕНЮСУ ---
    if message.text == "💎 Free Fire":
        markup = types.InlineKeyboardMarkup(row_width=2)
        
        # Алмаздар
        b1 = types.InlineKeyboardButton("💎 110 = 85 сом", callback_data="buy_ff_110_85")
        b2 = types.InlineKeyboardButton("💎 341 = 270 сом", callback_data="buy_ff_341_270")
        b3 = types.InlineKeyboardButton("💎 572 = 450 сом", callback_data="buy_ff_572_450")
        b4 = types.InlineKeyboardButton("💎 1166 = 850 сом", callback_data="buy_ff_1166_850")
        b5 = types.InlineKeyboardButton("💎 2398 = 1600 сом", callback_data="buy_ff_2398_1600")
        b6 = types.InlineKeyboardButton("💎 6160 = 3900 сом", callback_data="buy_ff_6160_3900")
        
        # Ваучерлер
        v1 = types.InlineKeyboardButton("🎟 Lite (90💎) = 46 сом", callback_data="buy_ff_lite_46")
        v2 = types.InlineKeyboardButton("🎟 Weekly (450💎) = 170 сом", callback_data="buy_ff_weekly_170")
        v3 = types.InlineKeyboardButton("🎟 Monthly (2600💎) = 799 сом", callback_data="buy_ff_monthly_799")

        markup.add(b1, b2)
        markup.add(b3, b4)
        markup.add(b5, b6)
        markup.add(v1)
        markup.add(v2, v3)

        text = (
            "🔥 *FREE FIRE ДОНАТ* 🔥\n\n"
            "⚡ *Без задержки түшөт!* ⚡\n\n"
            "✅ Отзывдар бар\n"
            "🆔 Через ID\n"
            "⚡ 10 секундда түшөт\n\n"
            "👇 Керектүү товарды тандаңыз:"
        )
        bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

    # --- PUBG MOBILE МЕНЮСУ ---
    elif message.text == "🪖 PUBG Mobile":
        markup = types.InlineKeyboardMarkup(row_width=2)
        
        # UC кнопкалары
        p1 = types.InlineKeyboardButton("💎 60 UC = 95 сом", callback_data="buy_pubg_60uc_95")
        p2 = types.InlineKeyboardButton("💎 325 UC = 450 сом", callback_data="buy_pubg_325uc_450")
        p3 = types.InlineKeyboardButton("💎 660 UC = 850 сом", callback_data="buy_pubg_660uc_850")
        p4 = types.InlineKeyboardButton("💎 1800 UC = 2200 сом", callback_data="buy_pubg_1800uc_2200")
        p5 = types.InlineKeyboardButton("💎 3850 UC = 4300 сом", callback_data="buy_pubg_3850uc_4300")
        p6 = types.InlineKeyboardButton("💎 8100 UC = 8500 сом", callback_data="buy_pubg_8100uc_8500")
        
        # Подпискалар
        s1 = types.InlineKeyboardButton("🎁 Prime (1 ай) = 150 сом", callback_data="buy_pubg_prime_150")
        s2 = types.InlineKeyboardButton("🎁 Prime Plus (1 ай) = 700 сом", callback_data="buy_pubg_plus_700")

        markup.add(p1, p2)
        markup.add(p3, p4)
        markup.add(p5, p6)
        markup.add(s1, s2)

        text = (
            "🪖 *PUBG Mobile Донат* (сом)\n\n"
            "👇 Сатып алуу үчүн керектүү UC же подписканы тандаңыз:"
        )
        bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

    # --- TELEGRAM STARS МЕНЮСУ ---
    elif message.text == "⭐ Telegram Stars":
        markup = types.InlineKeyboardMarkup(row_width=2)
        
        st1 = types.InlineKeyboardButton("50 ⭐️ = 91 сом", callback_data="buy_stars_50_91")
        st2 = types.InlineKeyboardButton("75 ⭐️ = 130 сом", callback_data="buy_stars_75_130")
        st3 = types.InlineKeyboardButton("100 ⭐️ = 170 сом", callback_data="buy_stars_100_170")
        st4 = types.InlineKeyboardButton("150 ⭐️ = 255 сом", callback_data="buy_stars_150_255")
        st5 = types.InlineKeyboardButton("200 ⭐️ = 335 сом", callback_data="buy_stars_200_335")
        st6 = types.InlineKeyboardButton("250 ⭐️ = 410 сом", callback_data="buy_stars_410")
        st7 = types.InlineKeyboardButton("300 ⭐️ = 495 сом", callback_data="buy_stars_300_495")
        st8 = types.InlineKeyboardButton("350 ⭐️ = 575 сом", callback_data="buy_stars_350_575")
        st9 = types.InlineKeyboardButton("400 ⭐️ = 660 сом", callback_data="buy_stars_400_660")
        st10 = types.InlineKeyboardButton("450 ⭐️ = 735 сом", callback_data="buy_stars_450_735")
        st11 = types.InlineKeyboardButton("500 ⭐️ = 815 сом", callback_data="buy_stars_500_815")

        markup.add(st1, st2)
        markup.add(st3, st4)
        markup.add(st5, st6)
        markup.add(st7, st8)
        markup.add(st9, st10)
        markup.add(st11)

        text = (
            "Донат ⭐️ *Telegram'га @username аркылуу* 🔥 (сом менен)\n\n"
            "❗️ Бул чек эмес, кааласаңыз мындан көп дагы киргизип беребиз.\n"
            "Канча жылдыз керек экенин жазыңыз 😊\n\n"
            "👇 Керектүү жылдызча санын тандаңыз:"
        )
        bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

    elif message.text == "📞 Заказ берүү":
        # Бул жерге дагы түз личкага баруучу баскыч коштук
        link_markup = types.InlineKeyboardMarkup()
        btn_link = types.InlineKeyboardButton("💬 Администраторго жазуу", url="https://t.me/nurt1lek_ff")
        link_markup.add(btn_link)
        
        bot.send_message(
            message.chat.id,
            "📩 Заказ берүү же суроолор боюнча төмөнкү баскычты басып жазыңыз:",
            reply_markup=link_markup
        )

# Товарларды баскандагы логика
@bot.callback_query_handler(func=lambda call: call.data.startswith("buy_"))
def callback_inline(call):
    prices_db = {
        # Free Fire
        "buy_ff_110_85": ("Free Fire", "110 Алмаз", "85 сом", "ID номериңизди жазыңыз:"),
        "buy_ff_341_270": ("Free Fire", "341 Алмаз", "270 сом", "ID номериңизди жазыңыз:"),
        "buy_ff_572_450": ("Free Fire", "572 Алмаз", "450 сом", "ID номериңизди жазыңыз:"),
        "buy_ff_1166_850": ("Free Fire", "1166 Алмаз", "850 сом", "ID номериңизди жазыңыз:"),
        "buy_ff_2398_1600": ("Free Fire", "2398 Алмаз", "1600 сом", "ID номериңизди жазыңыз:"),
        "buy_ff_6160_3900": ("Free Fire", "6160 Алмаз", "3900 сом", "ID номериңизди жазыңыз:"),
        "buy_ff_lite_46": ("Free Fire", "Lite Voucher (90💎)", "46 сом", "ID номериңизди жазыңыз:"),
        "buy_ff_weekly_170": ("Free Fire", "Weekly Voucher (450💎)", "170 сом", "ID номериңизди жазыңыз:"),
        "buy_ff_monthly_799": ("Free Fire", "Monthly Voucher (2600💎)", "799 сом", "ID номериңизди жазыңыз:"),
        
        # PUBG
        "buy_pubg_60uc_95": ("PUBG Mobile", "60 UC", "95 сом", "ID номериңизди жазыңыз:"),
        "buy_pubg_325uc_450": ("PUBG Mobile", "325 UC", "450 сом", "ID номериңизди жазыңыз:"),
        "buy_pubg_660uc_850": ("PUBG Mobile", "660 UC", "850 сом", "ID номериңизди жазыңыз:"),
        "buy_pubg_1800uc_2200": ("PUBG Mobile", "1800 UC", "2200 сом", "ID номериңизди жазыңыз:"),
        "buy_pubg_3850uc_4300": ("PUBG Mobile", "3850 UC", "4300 сом", "ID номериңизди жазыңыз:"),
        "buy_pubg_8100uc_8500": ("PUBG Mobile", "8100 UC", "8500 сом", "ID номериңизди жазыңыз:"),
        "buy_pubg_prime_150": ("PUBG Mobile", "Prime подпискасы", "150 сом", "ID номериңизди жазыңыз:"),
        "buy_pubg_plus_700": ("PUBG Mobile", "Prime Plus подпискасы", "700 сом", "ID номериңизди жазыңыз:"),
        
        # Stars
        "buy_stars_50_91": ("Telegram Stars", "50 ⭐️", "91 сом", "Колдонуучу атыңызды (@username) жазыңыз:"),
        "buy_stars_75_130": ("Telegram Stars", "75 ⭐️", "130 сом", "Колдонуучу атыңызды (@username) жазыңыз:"),
        "buy_stars_100_170": ("Telegram Stars", "100 ⭐️", "170 сом", "Колдонуучу атыңызды (@username) жазыңыз:"),
        "buy_stars_150_255": ("Telegram Stars", "150 ⭐️", "255 сом", "Колдонуучу атыңызды (@username) жазыңыз:"),
        "buy_stars_200_335": ("Telegram Stars", "200 ⭐️", "335 сом", "Колдонуучу атыңызды (@username) жазыңыз:"),
        "buy_stars_410": ("Telegram Stars", "250 ⭐️", "410 сом", "Колдонуучу атыңызды (@username) жазыңыз:"),
        "buy_stars_300_495": ("Telegram Stars", "300 ⭐️", "495 сом", "Колдонуучу атыңызды (@username) жазыңыз:"),
        "buy_stars_350_575": ("Telegram Stars", "350 ⭐️", "575 сом", "Колдонуучу атыңызды (@username) жазыңыз:"),
        "buy_stars_400_660": ("Telegram Stars", "400 ⭐️", "660 сом", "Колдонуучу атыңызды (@username) жазыңыз:"),
        "buy_stars_450_735": ("Telegram Stars", "450 ⭐️", "735 сом", "Колдонуучу атыңызды (@username) жазыңыз:"),
        "buy_stars_500_815": ("Telegram Stars", "500 ⭐️", "815 сом", "Колдонуучу атыңызды (@username) жазыңыз:")
    }

    if call.data in prices_db:
        game, count, price, input_type = prices_db[call.data]
        
        message_to_copy = (
            f"Салам! Заказ берейин дегем:\n"
            f"🎮 Оюн: {game}\n"
            f"📦 Товар: {count}\n"
            f"💵 Баасы: {price}\n"
            f"🆔 {input_type} [БУЛ ЖЕРГЕ ЖАЗЫҢЫЗ]"
        )

        response_text = (
            f"🛒 *Сиз тандадыңыз:* {game} — {count} / {price}\n\n"
            f"1️⃣ Төмөнкү текстти басыңыз (ал автоматтык түрдө көчүрүлөт):\n\n"
            f"`{message_to_copy}`\n\n"
            f"2️⃣ Андан соң төмөнкү баскычты басып, текстти администраторго жөнөтүңүз 👇"
        )
        
        # Сага түз шилтеме берүүчү Inline баскыч
        order_markup = types.InlineKeyboardMarkup()
        btn_to_admin = types.InlineKeyboardButton("💬 Администраторго жазуу", url="https://t.me/nurt1lek_ff")
        order_markup.add(btn_to_admin)
        
        bot.send_message(call.message.chat.id, response_text, parse_mode="Markdown", reply_markup=order_markup)
    
    bot.answer_callback_query(call.id)

print("Бот ийгиликтүү ишке кирди жана иштөөгө даяр...")
bot.infinity_polling()
