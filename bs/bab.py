import requests as req
from bs4 import BeautifulSoup as bs


url = 'https://www.pusan.ac.kr/kor/CMS/MenuMgr/menuListOnBuilding.do?mCode=MN202'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'}

web = req.get(url, headers = headers)

def bbab():
    soup = bs(web.content, 'html5lib')
    # print(soup)
    menucard = soup.select('.menu-tbl')
    # print(menucard)
    won = soup.select('.menu-tit01')
    # print(won)
    menu = soup.select('.menu-tit01+p')
    # print(menu)
    day = soup.select('.day') 
    date = soup.select('.date') 
    for d, dd, w, m in zip (day, date, won, menu):
        print(d.text, dd.text)
        print(w.text+'\n'+m.text)
        print('-'*20)

if __name__=='__main__':
    mel()