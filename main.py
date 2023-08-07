# ------------------------------------------------ Modullar


import os
from telethon import events,TelegramClient
import handlers.client, handlers.about, handlers.quotly, handlers.voice_bla,handlers.help
import handlers.heart , handlers.whale,handlers.good,handlers.goodmorning,handlers.music,handlers.bear,handlers.zor
import handlers.kachok,handlers.homework,handlers.infinite
import handlers.emoji,handlers.police,handlers.heart,handlers.magicrun

# -------------------------------------------------------------


# ---------------------------------- Client
client = handlers.client.client
# ------------------------------------------

os.system("cls")

# ----------------------------------- Banner
print("""\u001b[33m
 █    ██   ██████ ▓█████  ██▀███   ▄▄▄▄    ▒█████  ▄▄▄█████▓
 ██  ▓██▒▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▓██  ▒██░░ ▓██▄   ▒███   ▓██ ░▄█ ▒▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▓▓█  ░██░  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  ▒██░█▀  ▒██   ██░░ ▓██▓ ░
▒▒█████▓ ▒██████▒▒░▒████▒░██▓ ▒██▒░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░
░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░
░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░▒░▒   ░   ░ ▒ ▒░     ░
 ░░░ ░ ░ ░  ░  ░     ░     ░░   ░  ░    ░ ░ ░ ░ ▒    ░
   ░           ░     ░  ░   ░      ░          ░ ░
                                        ░
\u001b[33m""")
# -----------------------------------------------------


# ---------------------------------- Check Run
print("\u001b[32m\nUserbot ishga tushdi\u001b[32m")
# -------------------------------------------------


# ----------------------------------sticker quotly
with client as quotly:
    quotly.add_event_handler(handlers.quotly.quotly)

with client as police:
    police.add_event_handler(handlers.police.police)
with client as homework:
    homework.add_event_handler(handlers.homework.homework)

# -----------------------------------------------------------
with client as help:
    help.add_event_handler(handlers.help.help)


with client as morning:
    morning.add_event_handler(handlers.goodmorning.morning)

with client as infinite:
    infinite.add_event_handler(handlers.infinite.infinite)
with client as zor:
    zor.add_event_handler(handlers.zor.zor)

with client as emoji:
    emoji.add_event_handler(handlers.emoji.emoji)

with client as music:
    music.add_event_handler(handlers.music.music)

with client as magic:
    magic.add_event_handler(handlers.music.music)

with client as kachok:
    kachok.add_event_handler(handlers.magicrun.magichandler)

with client as good:
    good.add_event_handler(handlers.good.good)

with client as heart:
    heart.add_event_handler(handlers.heart.heart)
with client as chiyqiriq:
    chiyqiriq.add_event_handler(handlers.voice_bla.chiyqiriq)
with client as whale:
    whale.add_event_handler(handlers.whale.whale)
with client as qachon:
    qachon.add_event_handler(handlers.voice_bla.qachon)
with client as bear:
    bear.add_event_handler(handlers.bear.bear)


with client as ablah:
    ablah.add_event_handler(handlers.voice_bla.ablah)

with client as qanaqa_pul:
    qanaqa_pul.add_event_handler(handlers.voice_bla.qanaqa_pul)



with client as naruto_music:
    naruto_music.add_event_handler(handlers.voice_bla.naruto_music)

with client as qis:
    qis.add_event_handler(handlers.voice_bla.qis)
with client as shunaqa_degin:
    shunaqa_degin.add_event_handler(handlers.voice_bla.shunaqa_degin)

with client as shunaqalar_bor:
    shunaqalar_bor.add_event_handler(handlers.voice_bla.shunaqalar_bor)

with client as kuchenskiy_salom:
    kuchenskiy_salom.add_event_handler(handlers.voice_bla.kuchenskiy_salom)

with client as pidarazlar:
    pidarazlar.add_event_handler(handlers.voice_bla.pidarazlar)



# ---------------------------------aboutme
with client as about:
    about.add_event_handler(handlers.about.about)


# --------------------------------------------------------





@client.on(events.NewMessage(outgoing=True, pattern=r'\.mem'))
async def shazam(event):
    chat = await event.get_chat()
    await client.edit_message(event.message, 'Loading........')
    replied = await event.get_reply_message()
    x = await replied.forward_to('@memocyteBot')
    async with client.conversation('@memocyteBot') as conu:
        xx = await conu.get_response(x.id)
        await client.send_message(chat, xx)
        await event.message.delete()


# ------------------------------------------------- HELP


# ------------------------------------------------ Start
client.start()
client.run_until_disconnected()
