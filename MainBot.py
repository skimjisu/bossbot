
# 보스 로봇 마이그레이선 v1.0

import os
import sys
import asyncio
import discord 
from discord.ext.commands import Bot 

access_token = os.environ["BOT_TOKEN"]

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
            
            
        
        
