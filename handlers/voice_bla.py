from telethon import events
import handlers.client
client = handlers.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.chiyqiriq'))
async def chiyqiriq(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/ovozqanibot_kulgili_ovozlar/781")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.qachon_otiramiz'))
async def qachon(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/ovozqanibot_kulgili_ovozlar/780")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.ablahsanlar'))
async def ablah(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/ovozqanibot_kulgili_ovozlar/779")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.qanaqa_pul'))
async def qanaqa_pul(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/ovozqanibot_kulgili_ovozlar/777")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.naruto_music'))
async def naruto_music(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/uzb_animes/583")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.qis'))
async def qis(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/ovozqanibot_kulgili_ovozlar/773")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.shunaqa_degin'))
async def shunaqa_degin(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/ovozqanibot_kulgili_ovozlar/768")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.shunaqalar_bor'))
async def shunaqalar_bor(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/ovozqanibot_kulgili_ovozlar/763")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.kuchenskiy_salom'))
async def kuchenskiy_salom(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/ovozqanibot_kulgili_ovozlar/761")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.pidarazlar'))
async def pidarazlar(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/ovozqanibot_kulgili_ovozlar/742")
    await send_file.message.delete()