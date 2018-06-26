from urllib.request import urlopen
from  bs4 import BeautifulSoup
import re
pages = set()
def getlinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")): #只要包含wiki开头的链接
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getlinks(newPage)

getlinks("")
