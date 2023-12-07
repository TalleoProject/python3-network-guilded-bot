# Python 3 cryptonote network stats guilded bot
# Cryptonote network stats guilded bot that displays a variety of network information and statistics on demand
# Version 1.0
#
# DEPENDENCIES
# sudo apt-get install python3
# sudo apt-get -y install python3-pip
# python3 -m pip install guilded.py==1.6.0
#
# HOW TO USE
# Go to Settings -> Bots -> Create a bot
# Create a bot
# Click the three dots and select 'Manage auth tokens'
# Generate a bot token and add it to TOKEN value inside networkbot.py file
#
# RUN THE BOT (run from command line)
# python3 networkbot.py

import random
import asyncio
import aiohttp
import guilded
import json
from guilded.ext import commands
from guilded.ext.commands import Bot

# bot description
# bot description displayed in help section
description = '''Network bot displays a variety of information and statistics on almost any cryptonote network. To use the commands type them with the prefix of ampersand (&). You can find the commands and their use below. Add (&) in front of a command (EXAMPLE: &height)'''

# bot prefix (&)
# prefix used to call your bot's commands
BOT_PREFIX = ("&")

# secret bot token
# never give your secret bot token to anyone
TOKEN = "YOUR_SUPER_SECRET_BOT_TOKEN_GOES_HERE"

# daemon address
# address used to communicate with the network (127.0.0.1 for localhost)
HOST = "YOUR_DAEMON_ADDRESS_GOES_HERE"

# daemon RPC port
# port used to communicate with the network (your network's RPC port)
PORT = "YOUR_RPC_PORT_GOES_HERE"

# Create bot
class NetworkBot(Bot):
    def __init__(self, *args, **kwargs):
        super(NetworkBot, self).__init__(*args, **kwargs)

    async def on_bot_added(self, server, member):
        print(f'Bot added to server {server.name}')

    async def on_bot_removed(self, server, member):
        print(f'Bot removed from server {server.name}')

# start a bot
client = NetworkBot(command_prefix=BOT_PREFIX)

# commmand: &height
# network top block height
@client.command(description="Network top block height.", brief="Blockchain height.")
async def height(context: commands.Context):
    url = 'http://' + str(HOST) + ':' + str(PORT) + '/getheight'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        # you can customize the output message(s) below
        await context.reply("🌐 **Network height:** " + str(response['height']))

# commmand: &hash
# appx. network hash rate
@client.command(description="Appx. network hash rate.", brief="Network hash rate.")
async def hash(context: commands.Context):
    url = 'http://' + str(HOST) + ':' + str(PORT) + '/getinfo'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        # you can customize the output message(s) below
        await context.reply("🌐 **Network hash rate:** " + str(response['hashrate']) + " H/s")

# commmand: &diff
# current network difficulty
@client.command(description="Current network difficulty.", brief="Network difficulty.")
async def diff(context: commands.Context):
    url = 'http://' + str(HOST) + ':' + str(PORT) + '/getinfo'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        # you can customize the output message(s) below
        await context.reply("🌐 **Network difficulty:** " + str(response['difficulty']))

# commmand: &tx
# total network transactions
@client.command(description="Total network transactions.", brief="Network transactions.")
async def tx(context: commands.Context):
    url = 'http://' + str(HOST) + ':' + str(PORT) + '/getinfo'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        # you can customize the output message(s) below
        await context.reply("🌐 **Network transactions:** " + str(response['tx_count']))

# commmand: &txpool
# current transactions pool size
@client.command(description="Current transactions pool size.", brief="TX pool size.")
async def txpool(context: commands.Context):
    url = 'http://' + str(HOST) + ':' + str(PORT) + '/getinfo'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        # you can customize the output message(s) below
        await context.reply("🌐 **Transactions pool:** " + str(response['tx_pool_size']))

# commmand: &ver
# current daemon version
@client.command(description="Current daemon version.", brief="Daemon version.")
async def ver(context: commands.Context):
    url = 'http://' + str(HOST) + ':' + str(PORT) + '/getinfo'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        # you can customize the output message(s) below
        await context.reply("🌐 **Daemon Version:** " + str(response['version']))

# commmand: &stats
# key network stats all in one place
@client.command(description="Key network stats all in one place.", brief="Network stats.")
async def stats(context: commands.Context):
    url = 'http://' + str(HOST) + ':' + str(PORT) + '/getinfo'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        # you can customize the output message(s) below
        await context.reply("🌐  NETWORK STATS\n**Height:** " + str(response['height']) + "    \n**Hash rate:** " + str(response['hashrate']) + " H/s    \n**Difficulty:** " + str(response['difficulty']) + "    \n**TX total:** " + str(response['tx_count']) + "    \n**TX in the pool:** " + str(response['tx_pool_size']) + "    \n**Daemon version:** " + str(response['version'])
         )


client.run(TOKEN)
