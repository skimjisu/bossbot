
# 보스 로봇 마이그레이선 v1.0

import os
import sys
import asyncio
import discord 
from discord.ext.commands import Bot 

access_token = os.environ["BOT_TOKEN"]

app = discord.Client()

#class BossBot(discord.Client):
#    def __init_(self):
#        self.aiolocks = defaultdict(asyncio.Lock)
#        self.voice_client_connectLock = asyncio.Lock()
#        self.voice_client_moveLock = asyncio.Lock()
        
        
#async def AutoJoin_Channels(self, channels):
#    join_servers_ed = []
    
#    for channels in channels:
#        if channels.server in join_servers_ed:
#            #서버 출력부....
#            continue


#app.run (access_token)

async def BotStart():
    await app.run(access_token)
    
def running_loop(loop):
    loop.run_forever()

def init():
    asyncio.get_child_watcher() # 체크 해볼 필요 없어도 그만 있어도 그만....

    loop = asyncio.get_event_loop()
    loop.create_task(start())

    thread = threading.Thread(target=running_loop, args=(loop,))
    thread.start()    
    
@app.event
async def on_message(message):
    if message.content.startswith("실험"):
       await message.channel.send("테스트 성공")
        
@app.event
async def on_ready():
    print(app.user.id)
    print("Bot is Ready")

@app.event
async def on_message(message):
    if message.content.startswith("실험"):
       await message.channel.send("테스트 성공")
