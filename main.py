from telebot import TeleBot
from telebot.types import Message

TOKEN = '5570981281:AAGPwJv6fTSJeHen39f-YTKMVz_WQPGLPGQ'

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Salom bu test uchun bot")


if __name__ == '__main__':
    bot.infinity_polling()