from discord.ext import commands
import traceback
import random
import io
import asyncio
import os
#import numpy as np

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']
    
    
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
@bot.command() 
async def AO-1(ctx):
    await ctx.send(':blue_circle:')
    """
#以降はオゾン層さんからの頂き物の改造
@client.command()
async def hoge():
    await message.channel.send("fuga")


# ユーザーの発言に対する反応を書く

@client.event
async def on_message(message):
  # コマンドと同時に使う用のまじない
  # cf. https://github.com/Rapptz/discord.py/issues/186
  await client.process_commands(message)

  # BOTとメッセージの送信者が同じ場合は何もしない
  if client.user == message.author:
    return

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
  if message.content.startswith("asso"):
    await message.channel.send(":pleading_face:")
  if message.content.startswith("ｳﾙ"):
    await message.channel.send("うるさい。")
  if message.content.startswith("うるさい"):
    await message.channel.send("やかましい。.wav")
  if message.content.startswith("コンギョ"):
    await message.channel.send(":flag_kp: :rocket: :boom:")
  if message.content.startswith("かに"):
    await message.channel.send(":crab:")
  if message.content.startswith("塩"):
    await message.channel.send(":salt:")
  if message.content.startswith("ﾊﾞｹ"):
    await message.channel.send(":japanese_ogre:")
  if message.content.startswith("java"):
    await message.channel.send(":coffee:")
    

  # 文中の内容が一致した場合にメッセージを返す
  if True in [i in message.content for i in ["死ね", "氏ね", "ﾀﾋね", "馬鹿にし", "馬鹿じゃね", "下がってろ"]]:
    async with message.channel.typing():
      await asyncio.sleep(0.5)
      await message.channel.send("なんや喧嘩か？")


  if True in [i in message.content for i in ["出禁", "dekin", ":dekin:", "出来ん", "Dekin", "できん", "デキン"]]:
    if message.guild.id == 494052154290601985:
      await message.add_reaction("<:dekin:556403106045493258>")
    else:
      await message.channel.send(":u7981:")


  # 文中の内容が一致した場合に、数種類のメッセージのうち1つをランダムに選んで返す
  if True in [i in message.content for i in ["ｱｶﾈﾁｬﾝ", "琴葉", "琴葉茜", "あかねちゃん", "茜ちゃん"]]:
    async with message.channel.typing():
      await asyncio.sleep(0.5)
      say_list = ["呼んだ？", "やぁ。", "やかましい。.wav", "せやな", "やあやあ諸君", "ｱｶﾈﾁｬﾝやで", "なんや？", "みんな大好きｱｶﾈﾁｬﾝやで", "zzz", "......"]
      async with message.channel.typing():
        await asyncio.sleep(0.75)
        # メッセージを選ぶ確率を指定する
        await message.channel.send(random.choices(say_list, k=1, weights=[0.55, 0.3, 0.1, 0.05])[0])

""
  if True in [i in message.content for i in ["帰"]]:
    async with message.channel.typing():
      await asyncio.sleep(0.5)
      say_list = ["とっとと大阪に帰れ！.wav", "帰りなさい", "あのねぇ…"]
      async with message.channel.typing():
        await asyncio.sleep(0.75)
        await message.channel.send(random.choices(say_list, k=1, weights=[0.5, 0.3, 0.2])[0])


  if True in [i in message.content for i in ["ozone", "オゾン"]]:
    async with message.channel.typing():
      await asyncio.sleep(0.5)
      say_list = [":eyes:", ":eye: :eye:", ":eye_in_speech_bubble:", ":nazar_amulet:"]
      async with message.channel.typing():
        await asyncio.sleep(0.75)
        await message.channel.send(random.choices(say_list, k=1, weights=[0.55, 0.3, 0.1, 0.05])[0])


  if True in [i in message.content for i in ["chin", "ちん", "ホモ", "ゲイ", "レズ"]]:
    async with message.channel.typing():
      await asyncio.sleep(0.5)
      say_list = [":rolling_eyes:", "やめなさい", "BIG ROKURO IS \n**WATCHING YOU**", "私のこと何だと思ってるの？", "||ちんちん||"]
      async with message.channel.typing():
        await asyncio.sleep(0.75)
        await message.channel.send(random.choices(say_list, k=1, weights=[0.5, 0.3, 0.13, 0.06, 0.01])[0])


  if True in [i in message.content for i in ["寝ます", "ねます", "寝回す", "寝る","おやすみんんさ"]]:
    async with message.channel.typing():
      await asyncio.sleep(0.5)
      emoji = '\N{THUMBS UP SIGN}'
      await message.add_reaction(emoji)
      say_list = ["じゃあね。.wav", "ｵﾔｽﾐ ｺﾚｽﾅﾊﾁ ｺﾝﾆﾁﾊ", "私の夢見てね", "夢の中でも私を回して", "いい夢を"]
      async with message.channel.typing():
        await asyncio.sleep(0.75)
        await message.channel.send(random.choices(say_list, k=1, weights=[0.55, 0.25, 0.1, 0.075, 0.025])[0])
  elif True in [i in message.content for i in ["眠れない", "眠れん", "寝たい", "眠いん", "眠たい"]]:
    async with message.channel.typing():
      await asyncio.sleep(0.5)
      say_list = ["寝なきゃ回すわよ", "ろくろが1基、ろくろが2基、ろくろが3基、……", "釉薬キメて寝て:heart:", "釉薬いる？", "添い寝してあげる:heart:"]
      async with message.channel.typing():
        await asyncio.sleep(0.75)
        await message.channel.send(random.choices(say_list, k=1, weights=[0.55, 0.25, 0.1, 0.075, 0.025])[0])
"""

# botの動作に必要なトークンの記述(ここでは環境変数に登録したbotのトークンを呼び出して使用している)
#client.run(os.environ.get("DISCORD_TOKEN"))
# コード中に直接トークンを記述する場合は、以下のようにすれば動くかと
# client.run(トークンをここにコピペする)
    
bot.run(token)
