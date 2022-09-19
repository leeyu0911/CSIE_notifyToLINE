# https://notify-bot.line.me/my/
import lineTool
from get_CSIE_web_announces import *
import time
from datetime import datetime

# 讀取 LINE token
with open('line_token.txt', 'r') as f:
    token = f.read()

while True:
    # 讀取發送歷史紀錄
    with open('history.txt', 'r') as f:
        historyURL = f.read()
    historyURL = historyURL.split('\n')[:-1]

    # 爬取系網站前十筆公告
    Status, Title, articleURL = get_scie_web_announces()

    # 如果沒發送過就發送通知
    for i in reversed(range(10)):
        if articleURL[i] not in historyURL:
            lineTool.lineNotify(token, f'[{Status[i]}]' + Title[i] + '\n' + articleURL[i])
            print(Title[i])

    # 發送完更新歷史紀錄 只存20筆紀錄 index越大記錄越新
    historyURL.extend(articleURL)
    if len(historyURL) > 20:
        historyURL = historyURL[-20:]
    with open('history.txt', 'w') as f:
        for item in articleURL:
            f.write("%s\n" % item)


    # lineTool.lineNotify(token, time.ctime())
    print(f"Last Check: {datetime.now()}")
    time.sleep(60)
