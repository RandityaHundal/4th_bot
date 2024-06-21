import discord
import requests
import json
from discord import Embed

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

def get_dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    json_data = json.loads(response.text)
    return json_data["message"]

def get_cat():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    json_data = json.loads(response.text)
    return json_data[0]["url"]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
        
        if message.content.startswith("$meme"):
            await message.channel.send(get_meme())
        
        if message.content.startswith("$dog"):
            await message.channel.send(get_dog())
        
        if message.content.startswith("$cat"):
            await message.channel.send(get_cat())

        if message.content.startswith("$monkey"):
            await message.channel.send("https://www.placemonkeys.com/500")

        
        if message.content.startswith("$cmds"):
            embed = Embed(title="Commands",
                          description="$hello - Hello World!\n$meme - random meme\n$dog - random image of a dog\n$cat - random image of a cat\n$monkey - random image of a monkey",
                          color=2326507)
            await message.channel.send(embed=embed)
        
        
        

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('secret')
