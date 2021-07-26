import discord
import os
from replit import db
from keep_alive import keep_alive

client = discord.Client()

commandWord = ['$deposit', '$delete']

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
  if message.content.startswith('$deposit') and message.author.id == 689071825044373525 :
    typeMsg = message.content.split(" ", 2)[1]
    Dmsg = message.content.split(" ", 2)[2]
    depositMsg(typeMsg,Dmsg)
    await message.channel.send('I got it!')
    await message.channel.purge(limit = 10)
    keys = db.keys()
    for x in keys:
      newMsg = x + "   " + db[x]
      await message.channel.send(newMsg)
  if message.content.startswith('$print') and message.author.id == 689071825044373525:
    await message.channel.purge(limit = 10)
    keys = db.keys()
    for x in keys:
      newMsg = x + "   " + db[x]
      await message.channel.send(newMsg)
  if message.content.startswith('$delete') and message.author.id == 689071825044373525:  
    keyDel = message.content.split()[1]
    del db[keyDel]
    await message.channel.send('Eliminate!')
  if any(word in message.content for word in commandWord):
        await message.delete()
  if message.content.startswith('$clear') and message.author.id == 689071825044373525:
    await message.channel.purge(limit = 10)

keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)



