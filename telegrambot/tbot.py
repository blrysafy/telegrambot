import json
import telebot

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
TOKEN = config['BOT_TOKEN']
    
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start_message(message):
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f"Hey, {user_name}!")
bot.infinity_polling()