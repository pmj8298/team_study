# 영화 순위 뽑기
import requests as req
from bs4 import BeautifulSoup as bs
url = "https://m.moviechart.co.kr/rank/realtime/index/image"
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
web = req.get(url, headers = headers)
def movie():
    soup = bs(web.content, 'html.parser')
    title = soup.select('.movie-title h3 a')
    str = ''
    for i, (t) in enumerate(title, 1):
        str += f"{i}위: {t.text.strip()}\n"
    print(str)
    
if __name__=='__main__':
    mel()