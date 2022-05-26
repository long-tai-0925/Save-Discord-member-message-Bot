# 導入Discord模組
import discord
# 從discord.ext中導入commands
from discord.ext import commands
# 使用時請標示原作

# 定義client的益思並設定前綴(更改command_prefix='?'中的?即可更改前綴)
client = commands.Bot(command_prefix='.')

# 偵測
@client.event 
# 偵測當BOT準備好時
async def on_ready():
    # 打開log.txt文件(可自行改名)並將它見稱為log
    with open("log.txt", "a") as log:
        #在log.txt裡撰寫"-----------------重啟後訊息的開端-----------------"並在前後都空一行(方便查看)
        #在Python中"\n"代表換行
        log.write(f"\n-----------------重啟後訊息的開端-----------------\n")

# 偵測
@client.event
# 在偵測到訊息時啟動
async def on_message(message):
    # 打開log.txt文件(可自行改名)並將它見稱為log
    with open("log.txt", "a") as log:
        #在log.txt裡撰寫"名稱：{message.author}\n內容：{message.content}\n頻道：{message.channel}\n群組：{message.guild}\n\n------------------------------\n"並在前後都空一行(方便查看)
        #在Python中"\n"代表換行
        log.write(f"名稱：{message.author}\n內容：{message.content}\n頻道：{message.channel}\n群組：{message.guild}\n\n------------------------------\n")
        # 這行我忘記甚麼意思了
    message.content = message.content.casefold()

# 這是每個BOT最重要的地方 他決定了你BOT能否運行 你務必輸入正確的Token
client.run("在這裡輸入你的Token")
