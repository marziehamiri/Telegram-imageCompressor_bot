

import telebot
import os
from PIL import Image
from io import BytesIO

os.environ["HTTP_PROXY"] = "http://127.0.0.1:12334"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:12334"
# توکن ربات
TOKEN = "9219898463:AAHz9o_Tg6xegRUUj7hHl-QTEC9XHRPjTJo"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id,"سلام خوش آمدید لطفا عکس مورد نظرتان را بفرستید تا حجم آن کاهش پیدا کند")
@bot.message_handler(content_types=['photo', 'document'])
def compress_photo(message):

    # دریافت فایل
    if message.content_type == 'photo':
        file_id = message.photo[-1].file_id
    else:
        file = message.document

        if file.mime_type not in ['image/jpeg', 'image/png']:
            bot.reply_to(message, "لطفاً فقط عکس JPG، JPEG یا PNG ارسال کنید.")
            return

        file_id = file.file_id

    # دانلود عکس
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # باز کردن عکس
    image = Image.open(BytesIO(downloaded_file))

    # حجم اولیه
    original_size = len(downloaded_file)

    # آماده‌سازی خروجی
    output = BytesIO()

    # فشرده‌سازی
    if image.format == 'PNG':
        image.save(output, format='PNG', optimize=True)
    else:
        image = image.convert('RGB')
        image.save(output, format='JPEG',
                   quality=40, optimize=True)

    output.seek(0)

    # حجم نهایی
    compressed_size = output.getbuffer().nbytes

    # ارسال عکس فشرده‌شده
    bot.send_document(
        message.chat.id,
        output,
        visible_file_name='compressed.jpg'
    )

    # نمایش اطلاعات
    bot.send_message(
        message.chat.id,
        f"حجم اولیه: {original_size / 1024:.2f} KB\n"
        f"حجم نهایی: {compressed_size / 1024:.2f} KB"
    )



# اجرای ربات
print("Bot is running...")

bot.infinity_polling()