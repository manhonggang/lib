from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re #引入正则表达式

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
links = getLinks("/wiki/Kevin_Bacon") #维基百科后面区分大小写
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"] # 在KB相关的链接里随机找一个链接形成新的
    print(newArticle)
    links = getLinks(newArticle)