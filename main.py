# 導入Discord模組
import discord
# 從discord.ext中導入commands
from discord.ext import commands
import datetime
# 使用時請標示原作

#此def是其他人的 但我忘記原作是誰
def gettime():
    x = datetime.datetime.now()
    err = datetime.timedelta(hours=6)
    x += err
    y = x.year
    m = ['1月', '2月', '3月', '4月', '5月', '6月', '7月',
         '8月', '9月', '10月', '11月', '12月'][x.month - 1]
    d = x.day
    h = x.hour
    mi = x.minute
    s = x.second
    w = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'][(x.weekday() + 1) % 7]
    res = f"{y}年{m}{d}日{w},{h}點{mi}分{s}秒"
    return res

# 定義client的益思並設定前綴(更改command_prefix='?'中的?即可更改前綴)
client = commands.Bot(command_prefix='.')

# 偵測
@client.event
# 在偵測到訊息時啟動
async def on_message(message):
    # 當發訊息的是Bot時
    if message.author.bot:
        # 上面判斷式成立就結束整個on_message
        return
    # 打開與伺服器名稱相同的.txt文件(可自行改名)並將它簡稱為log
    with open(f"DC/discord_message/{message.guild}.txt", "a") as log:
        #在log.txt裡撰寫"名稱：{message.author}\n內容：{message.content}\n頻道：{message.channel}\n群組：{message.guild}\n\n------------------------------\n"並在前後都空一行(方便查看)
        #在Python中"\n"代表換行
        log.write(f"名稱：{message.author}\n內容：{message.content}\n群組：{message.guild}\n頻道：{message.channel}\n時間：{gettime()}\n------------------------------\n")
    # 打開全部訊息.txt文件(可自行改名)並將它簡稱為log
    with open(f"DC/discord_message/全部訊息.txt", "a") as log:
        #在log.txt裡撰寫"名稱：{message.author}\n內容：{message.content}\n頻道：{message.channel}\n群組：{message.guild}\n\n------------------------------\n"並在前後都空一行(方便查看)
        log.write(f"{message.author}：{message.content} 群組：{message.guild},頻道：{message.channel},時間：{gettime()}\n")
    # 這段我忘了
    message.content = message.content.casefold()
    
client.run(UR_TOKEN")
