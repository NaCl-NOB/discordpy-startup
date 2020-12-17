import discord
import traceback
import random
import hoge
import io
import re
import asyncio
import pathlib
import os
import numpy as np
from discord.ext import commands

BOT_PREFIX = ('!')
#bot = commands.Bot(command_prefix= BOT_PREFIX)
client = commands.Bot(command_prefix = BOT_PREFIX)
#token = os.environ['DISCORD_BOT_TOKEN']
# Botの起動とDiscordサーバーへの接続
#client.run(token)

@client.event
async def on_ready():
        # 起動したらターミナルにログイン通知が表示される
        print('ログインしました')
        await client.change_presence(activity=discord.Game(name='布教活動'))

@client.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(
        traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send('(´・ω・｀)？')


@client.command()
async def ping(ctx):
    await ctx.send('pong')

@client.command()
async def pong(ctx):
    await ctx.send('ping')

@client.command()
async def neko(ctx):
    await ctx.send(random.choice(('ﾔｰ', 'ﾔｰ', 'ﾔｰ', 'ﾔｰ', 'ﾔｰ', 'ﾔｰ', 'ﾔｰﾃﾞ', 'ﾔｰﾃﾞ', 'ﾔｰﾃﾞ', 'ﾔｰﾃﾞ', 'ﾔｰﾃﾞ', 'ええ加減にせぇや', '何がおもろいん?', '......うちも暇やないんやけど')))


#以降はオゾン層さんからの頂き物の改造

@client.command()
async def hoge():
    await client.channel.send("fuga")


# ユーザーの発言に対する反応を書く

@client.event
async def on_message(message):
  # コマンドと同時に使う用のまじない
  # cf. https://github.com/Rapptz/discord.py/issues/186
    await client.wait_until_ready()
    await client.process_commands(message)
  # BOTとメッセージの送信者が同じ場合は何もしない
    if client.user == message.author:
      return

    guild = message.guild

  # 文の最初が一致した場合にメッセージを返す
    if message.content.startswith("ステルス"):
      await message.channel.send("「ス」めー。")
    if message.content.startswith("平沢"):
      await message.channel.send("東京の平沢です。")
    if message.content.startswith("回"):
      await message.channel.send("今日もタービンは回っている")
    if message.content.startswith("おはよう"):
      await message.channel.send("ご機嫌よう")
    if message.content.startswith("何だかんだ"):
      await message.channel.send("次は、神田です")
    if message.content.startswith("ｳﾙ"):
      await message.channel.send("うるさい。")
    if message.content.startswith("うるさい"):
      await message.channel.send("やかましい。.wav")
    if message.content.startswith("!AO-1"):
      await message.channel.send(":blue_circle:")
      
    # 後でメンションにする
      """
    if message.content.startswith("asso"):
      await message.channel.send(":pleading_face:")
    if message.content.startswith("コンギョ"):
      await message.channel.send(":flag_kp: :rocket: :boom:")
    if message.content.startswith("かに"):
      await message.channel.send(":crab:")
    if message.content.startswith("塩"):
      await message.channel.send(":salt:")
    if message.content.startswith("ﾊﾞｹ"):
      await message.channel.send(":japanese_ogre:")
      """

    if message.content.startswith("java"):
      await message.channel.send(":coffee:")
  

# 文中の内容が一致した場合にメッセージを返す
    if True in [i in message.content for i in ["死ね", "氏ね", "ﾀﾋね", "馬鹿にし", "馬鹿じゃね", "下がってろ"]]:
      async with message.channel.typing():
        await asyncio.sleep(0.5)
        await message.channel.send("なんや喧嘩か？")


    if True in [i in message.content for i in ["出禁", "dekin", ":dekin:", "出来ん", "Dekin", "できん", "デキン"]]:
      async with message.channel.typing():
        await asyncio.sleep(0.5)
        await message.channel.send("||~~出禁に出来ん~~||")

      # 後でメンションにする
      """
      if message.guild.id == 494052154290601985:
        await message.add_reaction("<:dekin:556403106045493258>")
      else:
        await message.channel.send(":u7981:")
      """
         
      #bakanekoさんのコード    
      """
    if message.content.startswith('!chatcount'):
        if message.author.bot:
            return
        if message.content != "!chatcount":
            search_name = message.content.split(" ", 1)[1]
            print(search_name)
            search_name = search_name
            search_name = [men for men in message.guild.members if men.name == search_name][0]
            search_name = message.guild.get_member(display_name.id)
        else:
            search_name = message.guild.get_member(message.author.id)
        
        async with message.channel.typing():
            count = 0
            async for message in message.channel.history(limit=2500):
                if message.guild.get_member(message.author.id) == search_name:
                    # メッセージのカウントを増やす
                    count += 1
            await message.channel.send(("{}は、このチャンネルの直前2500回の発言中{}回発言しているみたいやで".format(search_name.name, count)))
      """
        
    # 文中の内容が一致した場合に、数種類のメッセージのうち1つをランダムに選んで返す
    elif True in [i in message.content for i in ["ｱｶﾈﾁｬﾝ", "琴葉", "琴葉茜", "あかねちゃん", "茜ちゃん"]]:
      async with message.channel.typing():
        await asyncio.sleep(0.5)
        say_list = ["呼んだ？", "やぁ。", "やかましい。.wav", "せやな", "やあやあ諸君", "ｱｶﾈﾁｬﾝやで", "なんや？", "みんな大好きｱｶﾈﾁｬﾝやで", "zzz", "......"]
        async with message.channel.typing():
          await asyncio.sleep(0.75)
          # メッセージを選ぶ確率を指定する
          await message.channel.send(random.choices(say_list, k=1, weights=[0.80,1.40,0.50,1.20,1.10,0.70,1.50,0.70,0.30,0.10])[0])
# botの動作に必要なトークンの記述(ここでは環境変数に登録したbotのトークンを呼び出して使用している)
client.run(os.environ.get("DISCORD_BOT_TOKEN"))
