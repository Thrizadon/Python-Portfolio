import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from youtube_dl import YoutubeDL

load_dotenv() #this library works with .env files. loads environment variables from a .env file into the code
TOKEN = os.getenv('DISCORD_TOKEN')#This will call to the file where the discord bot token is stored
GUILD = os.getenv('DISCORD_GUILD')
##### Generic command stuff

bot = commands.Bot(case_insensitive=True, command_prefix="!") #add case insensitivity to commands to work regardless of how they are typed

@bot.command(name="ping")
async def ping(ctx):
    await ctx.channel.send("pong")
@bot.command(name="pong")
async def ping(ctx):
    await ctx.channel.send("ping")

##### bot fun events
class fun_events:
    @bot.event
    async def on_message(message):
        if "i'm happy" in message.content: #made it so event would occur if keywords are found together in any combination of words.
            await message.channel.send("Gooray!")
        await bot.process_commands(message) #this allows events to run alongside commands

##### automoderation

##### MusicBot
@bot.command(name="join")
async def join_voice(ctx):
    connected = ctx.author.voice
    if connected:
        await connected.channel.connect()

@bot.command(name="leave")
async def leave(ctx):
    if (ctx.voice_client): # If the bot is in a voice channel
        await ctx.guild.voice_client.disconnect() # Leave the channel
        await ctx.send('See ya later, goomans!')
    else: # But if it isn't
        await ctx.send("Uh, i'm not even in a voice channel...")


from MusicBot import music_cog
bot.add_cog(music_cog(bot))

##### bot ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


bot.run(TOKEN)
