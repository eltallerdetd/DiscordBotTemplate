import os
from discord.ext import commands
from dotenv import load_dotenv
import urllib.request
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
KEY = os.getenv('KEY_YOUTUBE'); #Se agrego la key de la API de Youtube a .env para un mejor codigo

bot = commands.Bot(command_prefix='!') #Prefijo del bot

@bot.command(name='subs') #Funcion que mostrara los suscriptores de un canal de Youtube que le pasemos como parametro
async def subscriptores(ctx,username):
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + username + "&key=" + KEY).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    response = username + " tiene " + "{:,d}".format(int(subs)) + " suscriptores!"
    await ctx.send(response)

@bot.command(name='s') #Funcion que realizara la suma entre dos numeros enteros
async def sumar(ctx, num1,num2):
    response = int(num1)+int(num2)
    await ctx.send(response)

@bot.command(name='m') #Funcion que realizara la suma entre dos numeros enteros
async def multiplicar(ctx, num1,num2):
    response = int(num1)*int(num2)
    await ctx.send(response)

bot.run(TOKEN)