import requests as req
from bs4 import BeautifulSoup as bs

url = 'https://finance.naver.com/sise/sise_market_sum.naver'
web = req.get(url)

def nsise():
    soup = bs(web.content, 'html.parser')
    
    title = soup.select('.type_2')
    name = soup.select('.tltle')
    
    atitle = soup.select('.type_2')
    aname = soup.select('td.number:nth-child(3)')
    
    for i, (n,a) in enumerate(zip(name,aname),1):
        print(f'{i}위: {n.text} {a.text}원')
if __name__=='__main__':
    mel()