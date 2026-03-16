from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Bot token
TOKEN = "8668671133:AAFz2d61F6xFa4DzQO4rVsW1V-urobB5y58"  # BotFather'dan aldığın token

# Arşiv grubunun ID'si (şimdilik örnek, gerçek ID'yi terminalden alacağız)
TARGET_GROUP = -1003879780091  

# Özel karakter
SPECIAL_CHAR = "/s"  # Mesajlarda bu karakter varsa kopyalanacak

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    text = message.text

    if not text:
        return

    # ✅ Bu satır eklendi → mesaj geldiğinde terminale chat ID yazacak
    print("Chat ID:", update.effective_chat.id)

    if SPECIAL_CHAR in text:
        # Mesajı yazan admin mi kontrol et
        member = await context.bot.get_chat_member(
            chat_id=update.effective_chat.id,
            user_id=update.effective_user.id
        )

        if member.status in ["administrator", "creator"]:
            cleaned = text.replace(SPECIAL_CHAR, "").strip()
            await context.bot.send_message(
                chat_id=TARGET_GROUP,
                text=f"📌 Özel Not:\n\n{cleaned}"
            )

# Botu başlat
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))
app.run_polling()