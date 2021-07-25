import discord
import os
from replit import db

client = discord.Client()

def depositMsg(typeMsg,Dmsg):
  db[typeMsg] = Dmsg



@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
  if message.content.startswith('$deposit'):
    typeMsg = message.content.split()[1]
    Dmsg = message.content.split()[2]
    depositMsg(typeMsg,Dmsg)
    await message.channel.send('I got it!')
  if message.content.startswith('$print'):
    keys = db.keys()
    for x in keys:
      newMsg = x + "   " + db[x]
      await message.channel.send(newMsg)
  if message.content.startswith('$delete'):  
    keyDel = message.content.split()[1]
    del db[keyDel]
    await message.channel.send('Eliminate!')


my_secret = os.environ['TOKEN']
client.run(my_secret)



