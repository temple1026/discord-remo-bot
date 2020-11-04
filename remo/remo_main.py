# -*- coding: utf-8 -*-
import discord
from discord.ext import tasks
import asyncio
from remoapi import Remo

import datetime

def main():
    # from settings import TOKEN_DISCORD, remo_channel_id, second
    remo = Remo()
    config = remo.getConfig()

    remo_channel_id = int(config.get('info', 'channel'))
    second = int(config.get('info','second'))
    TOKEN_DISCORD = config.get('info','discord')

    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')


    @client.event
    async def on_message(message):
        if message.author != client.user:
            if message.content.startswith('remo') and (int(message.channel.id) == int(remo_channel_id)):
                time = datetime.datetime.now(remo.timezone)
                msg = "" + remo.get_message(time='{0:%Y-%m-%d %p%I-%M-%S}'.format(time), save=False)
                await message.channel.send(msg)


    @tasks.loop(seconds=60)
    async def sendRemoInfo():
        # channel = discord.Object(id=remo_channel_id)

        time = datetime.datetime.now(remo.timezone)
        if int(time.minute)%60 == 0:
            msg = remo.get_message(time='{0:%Y-%m-%d %p%I-%M-%S}'.format(time), save=True)
            channel = client.get_channel(remo_channel_id)
            await channel.send(msg)
        
    sendRemoInfo.start()
    client.run(TOKEN_DISCORD)


if __name__=="__main__":
    try: 
        main()

    except KeyboardInterrupt:
        print("Ctrl+C was pressed.")
    