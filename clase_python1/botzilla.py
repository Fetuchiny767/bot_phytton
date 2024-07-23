import os, random
import discord
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

token = "MTI1NzQ5MTIzNTc3MDQ2NjMwNQ.GhFy9O.WNyh50xj2jUzU7jQm34AJagiDn2BCtEa9m7EFU"

bot = commands.Bot(command_prefix = "/", intents=intents)

@bot.event
async def on_ready():
    print("botzilla ready")

@bot.command()
async def hola(ctx):
    await ctx.send(f"hola, me llamo {bot.user}")

@bot.command()
async def server(ctx):
    await ctx.send(f"estas en merequetengue, un server para jugar")
    await ctx.send(f"lastimosamente todavia no esta completo")
    await ctx.send(f"pero con un poco de tiempo lo estara")

@bot.command()
async def canales(ctx):
    c = open('chanels.txt', 'r', encoding='utf-8')
    canal = c.read()
    await ctx.send(f"{canal}")
    c.close()

@bot.command()
async def owner_info(ctx):
    o = open('chanels.txt', 'r', encoding='utf-8')
    dueño = o.read()
    await ctx.send(f"{dueño}")
    o.close()

@bot.command()
async def dato_animal(ctx):
    files = os.listdir("img_ani")
    ani_r = random.choice(files)
    ani_path = os.path.join("img_ani", ani_r)
    await ctx.send(file=discord.File(ani_path))

bot.run(token)