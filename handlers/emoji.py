from telethon import events
emojies = ['😀😁😂','🤣😃😄','😅😆😉','😊😋😎',
'😍😘🥰','😗😙😚','☺🙂🤗','🤩🤔🤨','😮😥😣','😏🙄😶','😑😐🤐','😯😪😫','🥱😴😌','😛😜😝',
'🤤😒😓','😔😕🙃','🤑😲☹','🙁😖😞','😟😤😬','🤯😩😨','😧😦😭','😢😠😡','🤬😷🤒','🤕🤢🤮','🤠🥺🥳','😇🤧😠','😰🥶😵']
import time
@events.register(events.NewMessage(outgoing=True, pattern=r'\.emoji'))
async def emoji(event):
    chat = await event.get_chat()
    for d in emojies:
        time.sleep(0.9)
        await event.edit(d)
    