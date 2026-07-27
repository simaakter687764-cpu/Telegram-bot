from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8608170736:AAEw4eVdjTqAThiksT1Xd102n1po2emEh5A"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 আসসালামু আলাইকুম! আমাদের বটে স্বাগতম।")

async def coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 আপনার ব্যালেন্স: 0 Coin")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛠️ সাহায্যের জন্য অ্যাডমিনের সাথে যোগাযোগ করুন।")

async def cap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📦 বর্তমান Capacity: 100")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("coin", coin))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("cap", cap))

print("Bot Running...")
app.run_polling()
