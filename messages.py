#!/usr/bin/python

import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import urllib
import picamera

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    print('Chat:', content_type, chat_type, chat_id)
    print('Chat:', CHATID)

    if chat_id == CHATID:
        if content_type == 'text':
            if msg['text'] == '/pic':
                capture_frame()
                f = urllib.urlopen('/home/pi/telegram_bot/photos/photo.jpg')
                bot.sendPhoto(chat_id, ('photo.jpg', f))
            else:
                bot.sendMessage(chat_id, msg['text'])
        else:
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                           [InlineKeyboardButton(text='Foto', callback_data='foto')],
                       ])

            bot.sendMessage(chat_id, 'Menu', reply_markup=keyboard)
    else:
        bot.sendMessage(chat_id, 'Access denied!')

def on_callback_query(msg):
    query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, chat_id, query_data)

    if chat_id == CHATID:
        capture_frame()
        f = urllib.urlopen('/home/pi/telegram_bot/photos/photo.jpg')
        bot.sendPhoto(chat_id, ('photo.jpg', f))
    else:
        bot.sendMessage(chat_id, 'Access denied!')
def capture_frame():
    with picamera.PiCamera() as cam:
        time.sleep(2)
        cam.rotation = -90
        cam.capture('/home/pi/telegram_bot/photos/photo.jpg')

TOKEN = sys.argv[1]
CHATID = int(sys.argv[2])

bot = telepot.Bot(TOKEN)
print(bot.getMe())

MessageLoop(bot, {'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread()

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
