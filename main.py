import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import qrcode

logging.basicConfig(level=logging.INFO)

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! Send me a file to generate a QR Code.')

def generate_qr_code(update, context):
    file_id = update.message.document.file_id
    file_info = context.bot.get_file(file_id)
    file_format = file_info.file_path.split('.')[-1]

    if file_format in ['jpg', 'png', 'mp4', 'mp3', '3gp', 'wav', 'zip', 'rar', 'txt', 'doc', 'docx', 'docs', 'ppt', 'word', 'pdf', 'html', 'xml']:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f'https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}')
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save('qr_code.png')

        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('qr_code.png', 'rb'))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Unsupported file format.')

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.document, generate_qr_code))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
