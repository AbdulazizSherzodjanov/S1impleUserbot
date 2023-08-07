from email import message
from telethon import  events
import handlers.client

client = handlers.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.whale'))
async def whale(event):
    chat = await event.get_chat()
    await event.edit("""
⁣  💦 💦
   💦     
   💧    🐳 🐳
 ⁣🐳🐳🐳    🐳
🐳🎱🐳🐳🐳 🐳
🐳🐳🐳🐳🐳🐳
 🐳🐳🐳🐳🐳
    """)