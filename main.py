from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Callback identifiers
BUTTON_PROFILE = "profile"
BUTTON_REFER = "refer"
BUTTON_LOGIN = "login"
BUTTON_DEPOSIT = "deposit"
BUTTON_WITHDRAW = "withdraw"
BUTTON_PROJECT = "project"
BUTTON_SUPPORT = "support"

# START command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("👤 প্রোফাইল", callback_data=BUTTON_PROFILE)],
        [InlineKeyboardButton("🔗 রেফার করে আয় করুন", callback_data=BUTTON_REFER)],
        [InlineKeyboardButton("✅ কিভাবে লগইন/সাইন আপ করবো", callback_data=BUTTON_LOGIN)],
        [InlineKeyboardButton("💳 কিভাবে টাকা ডিপোজিট করবো", callback_data=BUTTON_DEPOSIT)],
        [InlineKeyboardButton("🏦 কিভাবে টাকা উত্তোলন করবো", callback_data=BUTTON_WITHDRAW)],
        [InlineKeyboardButton("🛒 কিভাবে প্রজেক্ট ক্রয় করবো", callback_data=BUTTON_PROJECT)],
        [InlineKeyboardButton("💬 কাস্টমার সাপোর্ট", callback_data=BUTTON_SUPPORT)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_msg = (
        "স্বাগতম Invest Sure-এ!\n"
        "আপনার উপার্জনের এক অনন্য সঙ্গী।\n\n"
        "নিচের অপশনগুলো থেকে বেছে নিন:"
    )
    
    await update.message.reply_text(welcome_msg, reply_markup=reply_markup)

# BUTTON callback handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    link = "🔗 বিস্তারিত জানতে দেখুন:\nhttps://Invest-Sure.netlify.app"

    if query.data == BUTTON_PROFILE:
        await query.edit_message_text(
            f"আপনার প্রোফাইল:\n\n"
            f"নাম: {query.from_user.first_name}\n"
            f"ID: {query.from_user.id}\n"
            f"ব্যালেন্স: 0 BDT\n"
            f"রেফার কোড: {str(query.from_user.id)[-6:]}\n"
            f"যোগদান: --"
        )
    
    elif query.data == BUTTON_REFER:
        refer_link = f"https://t.me/{context.bot.username}?start={query.from_user.id}"
        await query.edit_message_text(
            f"রেফার করে আয় করুন:\n\n"
            f"আপনার রেফার লিংক:\n{refer_link}\n\n"
            f"বন্ধুদের শেয়ার করুন ও আয় করুন!"
        )

    elif query.data == BUTTON_LOGIN:
        await query.edit_message_text(
            "✅ লগইন/সাইন আপ করতে:\n"
            "১. ওয়েবসাইটে যান\n"
            "২. নাম, মোবাইল ও পাসওয়ার্ড দিন\n"
            "৩. অ্যাকাউন্ট তৈরি করুন\n\n" + link
        )

    elif query.data == BUTTON_DEPOSIT:
        await query.edit_message_text(
            "💳 টাকা ডিপোজিট করতে:\n"
            "১. বিকাশ/নগদ/রকেট নাম্বারে পাঠান\n"
            "২. পেমেন্ট রেফারেন্স দিন\n"
            "৩. কনফার্ম করুন\n\n" + link
        )

    elif query.data == BUTTON_WITHDRAW:
        await query.edit_message_text(
            "🏦 টাকা উত্তোলন করতে:\n"
            "১. মিনিমাম ব্যালেন্স থাকতে হবে\n"
            "২. উত্তোলন অনুরোধ দিন\n"
            "৩. টাকা ২৪ ঘণ্টার মধ্যে পাবেন\n\n" + link
        )

    elif query.data == BUTTON_PROJECT:
        await query.edit_message_text(
            "🛒 প্রজেক্ট কিনতে:\n"
            "১. আপনার অ্যাকাউন্ট থেকে ব্যালেন্স ব্যবহার করুন\n"
            "২. প্রজেক্ট নির্বাচন করুন\n"
            "৩. কনফার্ম করুন\n\n" + link
        )

    elif query.data == BUTTON_SUPPORT:
        await query.edit_message_text(
            "💬 যেকোনো সমস্যা হলে:\n"
            "১. আমাদের সাপোর্ট পেইজে যান\n"
            "২. সমস্যা লিখে পাঠান\n"
            "৩. আমরা দ্রুত উত্তর দেবো\n\n" + link
        )

# MAIN bot launcher
if __name__ == '__main__':
    app = ApplicationBuilder().token("7575065892:AAFbxN-Eh5_rN0MAB6RVQ-SEfVlZFs6_FAQ").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()
