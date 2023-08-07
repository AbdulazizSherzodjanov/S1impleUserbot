from telethon import  events,Button
import handlers.client

client = handlers.client.client
@events.register(events.NewMessage(pattern=".help"))
async def help(event):
    await event.edit("""
        S1mple UserBot🤖
📦 Umumiy Modullar :  
🎴 Reply qilgan so'zingizga sticker yasaydi :  .sticker     
🎴 Reply qilgan so'zingizga mem sticker yasaydi :  .mem
        🔉 Mem Audio Modullar🔉🎧
😨 Chiyqiriq -  .chiyqiriq
😂 Qachon o'tiramiz -  .qachon_otiramiz
🤣 Ablahsanlar -  .ablahsanlar
🙄 Qanaqa pul ? -  .qanaqa_pul
🦊 Naruto music -  .naruto_music
🤌 Qis -  .qis
🤨 Shunaqa degin ? -  .shunaqa_degin
🙄 Oramizda Shunaqalar ham bor -  .shunaqalar_bor
😎 Kuchenskiy salom -  .kuchenskiy_salom
🤣 Pidarazlar -  .pidarazlar
        🎴Art Modullar va Animatsiyalar 📦
💖 Love Bear 🐻 - .bear
👌 Good - .good
🌅 Good Morning - .morning
💖 Yurak - .heart
📝 Homework - .homework
♾ Infinite - .infinite
💪 Kachok - .kachok
🎵 Music - .music
🐳 Kit - .whale
👍 Good - .zor
🤧😇🥳 Emojilar - .emoji
    """)