import discord 
import os
import requests 
import json

token = os.getenv('TOKEN')
client = discord.Client()
def get_quote():
  response = requests.get #('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote= json_data[0]['q'] + ' -' + json_data[0]["a"]
  return(quote)



@client.event 
async def on_ready():
 print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('-hello'):
    await message.channel.send("hi")
  if message.content.startswith('-hi'):
    await message.channel.send("hi")
  if message.content.startswith('-how are you'):
    await message.channel.send("Im fine you tell")
  if message.content.startswith('-im fine'):
    await message.channel.send("Good")
  if message.content.startswith('-whatsup'):
    await message.channel.send("sup")
  if message.content.startswith('-help TGZ'):
    await message.channel.send("-hello , -hi , -how are you , -im fine , -whatsup ")
      
  
  
  
  if message.content.startswith('-quote'):
    quote= get_quote()
    await message.channel.send(quote)

client.run(os.getenv('TOKEN'))
