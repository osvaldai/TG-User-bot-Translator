import asyncio
from pyrogram import Client, filters
import translators as ts


api_id = 0  # add your api id

api_hash = ''  # add hash

app = Client(name='translate', api_id=api_id, api_hash=api_hash)


@app.on_message(filters.command('tr', prefixes='.') & filters.me)
def tr(_, msg):
    mes_txt = str(msg.text).replace('.tr', '')
    print(msg.text)
    translate = ts.google(mes_txt, from_language='auto', to_language='en')
    print(translate)  # default: from_language='auto', to_language='en'
    # output language_map
    # print(ts._google.language_map)
    msg.edit(translate)


app.run()
