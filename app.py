#!/usr/bin/python

import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import urllib
import picamera
import serial

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    print('Chat:', content_type, chat_type, chat_id)
    print('Chat:', CHATID)

    if chat_id == CHATID:
        print(msg['text'])
        if msg['text'] == '/menu@coione_bot' or msg['text'] == '/menu':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
               [InlineKeyboardButton(text='Lamp ON', callback_data='/rele11')],
               [InlineKeyboardButton(text='Lamp OFF', callback_data='/rele10')],
               [InlineKeyboardButton(text='Light ON', callback_data='/rele21')],
               [InlineKeyboardButton(text='Light OFF', callback_data='/rele20')],
               [InlineKeyboardButton(text='Relay ON', callback_data='/rele30')],
               [InlineKeyboardButton(text='Relay OFF', callback_data='/rele31')],
               [InlineKeyboardButton(text='Fan ON', callback_data='/fan1')],
               [InlineKeyboardButton(text='Fan OFF', callback_data='/fan0')],
               [InlineKeyboardButton(text='Take a picture', callback_data='/pic')]
            ])

            bot.sendMessage(chat_id, 'MENU', reply_markup=keyboard)
    else:
        bot.sendMessage(chat_id, 'Access denied!')

def on_callback_query(msg):
    query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, chat_id, query_data)

    data = query_data
    if chat_id == CHATID:
        if data == '/pic':
            capture_frame()
            f = urllib.urlopen('/home/pi/telegram_bot/photos/photo.jpg')
            bot.sendPhoto(chat_id, ('photo.jpg', f))
        if data == '/fan1':
            ser.write('1');
        if data == '/fan0': 
            ser.write('2');
        if data == '/rele11':
            ser.write('3');
        if data == '/rele10': 
            ser.write('4');
        if data == '/rele21':
            ser.write('5');
        if data == '/rele20': 
            ser.write('6');
        if data == '/rele30': 
            ser.write('7');
        if data == '/rele31': 
            ser.write('8');
    else:
        bot.sendMessage(chat_id, 'Access denied!')
def capture_frame():
    with picamera.PiCamera() as cam:
        time.sleep(2)
        cam.rotation = 180
        cam.capture('/home/pi/telegram_bot/photos/photo.jpg')



#### START #####

TOKEN = sys.argv[1]
CHATID = int(sys.argv[2])

bot = telepot.Bot(TOKEN)
print(bot.getMe())

MessageLoop(bot, {'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread()

print ('Listening ...')

ser=serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

while 1:
    time.sleep(10)
