from email import message
from telethon import  events
import handlers.client

client = handlers.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.infinite'))
async def infinite(event):
    chat = await event.get_chat()
    await event.edit("""
🚽 = 2 Minutes
🚽 + 📱 = 5 Minutes
🚽 + 📱 + ⁣📶 = 10 Minutes
🚽 + 📱 + 📶 + 🔋 = Infinite
""")