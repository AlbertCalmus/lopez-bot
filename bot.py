import os
import json
import random
import logging

from telegram.ext import Updater, CommandHandler

try:
  with open('config.json') as f:
    data = json.load(f)
except:
  print('Config file with token missing ! \n')

updater = Updater(token=data['token'])
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def mood(bot, update):
    sound_files = os.listdir('./sounds/')
    random.shuffle(sound_files)
    bot.send_voice(chat_id=update.message.chat_id, voice=open('./sounds/' + sound_files[0], 'rb'))


mood_handler = CommandHandler('mood', mood)
dispatcher.add_handler(mood_handler)

updater.start_polling()
print('LopezBot up and running!')