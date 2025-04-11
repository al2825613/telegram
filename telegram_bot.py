
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import subprocess

TOKEN = "7860410116:AAFpIea3bDqMHw9U0wdLlRNp5KYVZcU9WpE"  # ← غيّر التوكن بتاعك

def start(update: Update, context: CallbackContext):
    update.message.reply_text("أهلاً بيك! ابعت ID الحساب المستهدف علشان نبدأ التبليغ.")

def handle_id(update: Update, context: CallbackContext):
    target_id = update.message.text.strip()
    update.message.reply_text(f"جاري التبليغ على الحساب: {target_id}...
الرجاء الانتظار...")

    try:
        result = subprocess.run(
            ["python3", "report.py"],
            input=f"{target_id}
",
            text=True,
            capture_output=True
        )
        output = result.stdout.strip()[-4000:] or "تم التنفيذ ولكن بدون إخراج واضح."
        update.message.reply_text(f"النتيجة:

{output}")
    except Exception as e:
        update.message.reply_text(f"حدث خطأ أثناء التنفيذ:
{str(e)}")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_id))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
