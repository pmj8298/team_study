import requests as req
from bs4 import BeautifulSoup as bs
url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'}
web = req.get(url, headers = headers)
soup = bs(web.content, 'html.parser')
print(web)
title = soup.select('.rank01')[:20] # 20위까지
name = soup.select('.checkEllipsis a')[:20]
str = ''
for i, (t, n) in enumerate(zip(title, name),1):
    str += f'{i}위: {t.text.strip()} / {n.text}\n' 
print(str, end=' ')