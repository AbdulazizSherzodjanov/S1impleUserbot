from telethon import  events
import handlers.client

client = handlers.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.sticker'))
async def quotly(event):
    chat = await event.get_chat()
    replylied = await event.get_reply_message()
    await client.edit_message(event.message,"Yuklanmoqda.......")
    x = await replylied.forward_to('@QuotLyBot')
    async with client.conversation('@QuotLyBot') as conu:
       xx =  await conu.get_response(x.id)
       await client.send_message(chat,xx)
       await event.message.delete()