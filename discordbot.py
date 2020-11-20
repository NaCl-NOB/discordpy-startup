from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']

# 起動時に動作する処理
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='大英帝国'))
    
    
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
   
@bot.command()   
async def neko(ctx):
    await ctx.send(random.choice(('ﾔｰ','ﾔｰ','ﾔｰ','ﾔｰ','ﾔｰ','ﾔｰ','ﾔｰﾃﾞ','ﾔｰﾃﾞ','ﾔｰﾃﾞ','ﾔｰﾃﾞ','ﾔｰﾃﾞ','ええ加減にせぇや','何がおもろいん?','......うちも暇やないんやけど')))
    #await ctx.send('ﾔｰ')


    
bot.run(token)
