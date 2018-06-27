from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#获取所有的内链的列表

def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc #urlparse 这个把网页解析成六个部分，这里用两个部分拼装成了一个新的网页，意义不明。
    interanlLinks = [] #建立一个空集合
    for link in bsObj.findAll("a", href = re.compile("^(/|.*"+includeUrl+")")): # 正则表达式，^为匹配开头为“/”的链接，“|”代表左右任何一个都行，先匹配左面的；“.”是匹配换行符之外的任意字符，“*”是匹配前一个字符0次或者无限次。
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in interanlLinks:
                if(link.attrs['href'].startswith("/")):
                    interanlLinks.append(includeUrl+link.attrs['href'])
                else:
                    interanlLinks.append(link.attrs['href'])
    return interanlLinks
