from telethon import  events
import time
pol =  ["""🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴
🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴
🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴""",
"""🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵
🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵
🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵""","""🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴
🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴
🔵🔵🔵🔵🖱🖱🔴🔴🔴🔴""","""🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵
🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵
🔴🔴🔴🔴🖱🖱🔵🔵🔵🔵""",]
@events.register(events.NewMessage(outgoing=True, pattern=r'\.police'))
async def police(event):
    chat = await event.get_chat()
    for p in pol:
        time.sleep(0.9)
        await event.edit(p)