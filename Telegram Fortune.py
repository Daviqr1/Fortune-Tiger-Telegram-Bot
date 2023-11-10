from datetime import datetime, timedelta #
import json, requests
import telebot.types as InlinekeyboardMarkup
import random
import telebot
import time
import bd
from pytz import timezone

api_key = 'insert-api-key'
chat_id = 'insert-chat-id'


LINK_SITE = ''

bot = telebot.TeleBot(api_key)


def ALERT_GAME1():
    tz = timezone('America/Sao_Paulo')
    now = datetime.now(tz)
    h = datetime.now().hour
    m = datetime.now().minute
    s = datetime.now().second

    if m > 59:
        h += 1
        m = 0
    if h == 9:
        m = f'0{h}'
    if m < 9:
        m = f'0{m}'
    if s > 9:
        s = f'0{s}'

    message_id = bot.send_message(chat_id=chat_id, text = f'''nova oportunidade de entrada as {h}:{m}:{s}''').message_id
    bd.message_ids1 = message_id
    time.sleep(15)
    bd.message_delete1= True
    return

while True:
    tz = timezone('America/Sao_Paulo')
    now = datetime.now(tz)
    h = datetime.now().hour
    m = datetime.now().minute
    s = datetime.now().second
    if m > 59:
        h += 1
        m = 0
    if h == 9:
        m = f'0{h}'

    if m < 9:
        m = f'0{m}'
    if s < 9:
        s = f'0{s}'
    print(f'{h}:{m}:{s}')

    #hora = datetime.datetime.now().strftime('%H:%M:'))	

    numero_aleatorio1 = random.randint(1, 10)
    numero_aleatorio2 =  random.randint(1, 10)
time.sleep(10)

for i in range(1,10):

    print(numero_aleatorio1, numero_aleatorio2)

    dados = bot.send_photo(chat_id=chat_id, photo=open('C:/Users/devid/Desktop/BOT_TIGER.png'), caption=(f'''

    ### SINAL ENTREGUE $$$

    !!!! QUENTE: {(numero_aleatorio1)} X NORMAL

    !!!! QUENTE: {(numero_aleatorio2)} X TURBO

    ### VÁLIDO POR 4 MIN

    {LINK_SITE}'''), parse_mode='MARKDOWN')

    time.sleep(240)
bot.send_message(chat_id=chat_id, text = (f'''
    ### CARTA LIBERADA $$$
    # GREEEN
    
''',dados.chat.id, dados.message_id), parse_mode='MARKDOWN', disable_web_page_preview=True)
    
time.sleep(60)
    



