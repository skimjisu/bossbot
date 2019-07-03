
# 보스 로봇 마이그레이선 v1.0

import os
import sys
import asyncio
import discord 

from discord.ext.commands import commands 

access_token = os.environ["BOT_TOKEN"]

app = discord.Client()

client = commands.Bot(command_prefix='/')
voice_client = None

class BossBot(discord.Client):
    def __init_(self):
        self.aiolocks = defaultdict(asyncio.Lock)
        self.voice_client_connectLock = asyncio.Lock()
        self.voice_client_moveLock = asyncio.Lock()
        
        
async def AutoJoin_Channels(self, channels):
    join_servers_ed = []
    
    for channels in channels:
        if channels.server in join_servers_ed:
            #서버 출력부....
            continue

@app.event
async def on_ready():
    print(app.user.id)
    print("Bot is Ready")
    
@client.command()    
async def vc_join(ctx):
    #voicechannel 입장
    vc = ctx.author.voice.channel
    #voicechannel 접속
    await vc.connect()    

@app.event
async def on_message(message):
    if message.content.startswith("실험"):
       await message.channel.send("테스트 성공")

app.run (access_token)
        
