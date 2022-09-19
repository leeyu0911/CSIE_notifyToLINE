import requests
from bs4 import BeautifulSoup


def get_scie_web_announces():
    # get NCKU CSIE web announces
    csie = 'http://www.csie.ncku.edu.tw'
    url = csie + '/ncku_csie/announce/news/1000'
    response = requests.get(url)
    response.encoding = 'utf8'
    soup = BeautifulSoup(response.text, "html.parser")
    web_announces = soup.find_all("td")

    Status = []  # 公告標籤
    Title = []  # 標題
    articleURL = []  # 網址

    for i in range(len(web_announces)):
        # if i%2 == 0:
        #     Since.append(web_anounces[i].text)
        if i % 2 == 1:
            temp = web_announces[i].text.split('\xa0\xa0')  # ['一般', '[徵才公告]  AWS 2021校園招募']
            Status.append(temp[0])
            Title.append(temp[1])
            articleURL.append(csie + web_announces[i].find('a')['href'])
    Status.reverse(), Title.reverse(), articleURL.reverse()
    return Status, Title, articleURL