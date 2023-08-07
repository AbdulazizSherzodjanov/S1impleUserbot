from telethon import events
import handlers.client

client = handlers.client.client
# ------------------------------------------------------------------ About
@events.register(events.NewMessage(pattern=".about"))
async def about(event):
    await event.edit("""S1mple Userbot🎴 
    👨‍💻Programmer : t.me/@PyCoder_off1cial
    """)


# --------------------------------------------------------------------------