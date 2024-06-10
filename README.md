# QR-Code-Generator

# Purpose: 
Create a QR Code as a PNG image when a user uploads a file of a specific format to the bot.

# Features:

1. Responds to the /start command with a welcome message.
2. Supports file formats: jpg, png, mp4, mp3, 3gp, wav, zip, rar, txt, doc, docx, docs, ppt, word, pdf, html, xml.
3. Generates a QR Code using the qrcode library.
4. Sets the QR Code data to the URL of the uploaded file, accessible via the Telegram API.
5. Saves the QR Code as a PNG image.
6. Sends the QR Code image back to the user as a photo.


# How it works:

1. User sends a file to the bot.
2. Bot checks the file format and generates a QR Code if it's supported.
3. QR Code data is set to the URL of the uploaded file.
4. QR Code image is saved as a PNG file.
5. Bot sends the QR Code image back to the user.


# Requirements:

1. Python 3.x
2. qrcode library (install with pip install qrcode)
3. Telegram Bot token (replace YOUR_TELEGRAM_BOT_TOKEN with your actual token)

# Summary:

1. The bot responds to the /start command by sending a welcome message.
2. When a user uploads a file, the generate_qr_code function is triggered.
3. The function checks the file format by extracting the file extension from the file path.
4. If the file format is supported, the function generates a QR Code using the qrcode library.
5. The QR Code data is set to the URL of the uploaded file, which can be accessed using the Telegram API.
6. The QR Code image is saved as a PNG file.
7. The bot sends the QR Code image back to the user as a photo.

Note that you need to replace YOUR_TELEGRAM_BOT_TOKEN with your actual Telegram Bot token. Also, make sure to install the qrcode library by running pip install qrcode in your terminal.
