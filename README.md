# Telegram Image Compressor Bot

A Telegram bot built with Python that compresses JPG, JPEG, and PNG images and sends the optimized images back to users.

The bot receives images, downloads them, compresses them using the Pillow library, and returns the compressed file along with information about the original and final file sizes.

## Features

- Receive images through Telegram.
- Support JPG, JPEG, and PNG formats.
- Compress PNG images using optimization.
- Compress JPEG images with quality set to 40.
- Display the original image size.
- Display the compressed image size.
- Send the compressed image back to the user as a document.

## Technologies Used

- Python
- pyTelegramBotAPI
- Pillow (PIL)

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/marziehamiri/Telegram-imageCompressor_bot.git
```

**2. Navigate to the project directory**

```bash
cd Telegram-imageCompressor_bot
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

**5. Install the required libraries**

```bash
pip install -r requirements.txt
```

## Configuration

Create a Telegram bot using [BotFather](https://t.me/BotFather) and obtain your bot token.

Set your bot token in the `TOKEN` variable in `bot.py`.

**Security note:** Do not upload your actual bot token to GitHub. Use environment variables to keep it private.

## Usage

1. Start the bot by running:

```bash
python main.py
```

2. Open your Telegram bot.
3. Send the `/start` command.
4. Send a JPG, JPEG, or PNG image.
5. Receive the compressed image and its size information.

## Project Structure

```text
Telegram-imageCompressor_bot/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

1. The bot receives an image from the user.
2. It downloads the image from Telegram.
3. Pillow opens the image.
4. The image is compressed according to its format:
   - PNG: Optimization enabled.
   - JPEG: Quality set to 40 with optimization enabled.
5. The bot calculates the original and compressed file sizes.
6. The compressed image and size information are sent back to the user.

## Author

Marzieh Amiri

