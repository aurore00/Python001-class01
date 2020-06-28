import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


myurl = 'http://maoyan.com/films?showType=3'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Accept': "*/*",
    'Accept-Encoding': 'gazip, deflate, br',
    'Accept-Language': 'en-AU,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
    'Content-Type': 'text/plain',
    'Connection': 'keep-alive',
    'Origin': 'https://maoyan.com',
    'Referer': 'https://maoyan.com/films?showType=3',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'COOKIES': 'DA3E2700B7A311EA9C0AF732B1940F47F294C8C0EB1942E9B2D46FE7B0536BD9'
    
    }


response = requests.get(myurl, headers = header)
bs_info = bs(response.text, 'html.parser')
movie_dict = {'title': [], 'type': [], 'release': []}

for i in bs_info.findAll('div', attrs={'class': 'movie-item film-channel'})[:10]:
    list1 = i.findAll('div', attrs={'class': 'movie-hover-title'})
    title = list1[0].get('title')
    typ = list1[1].text.strip().split('\n')[1].strip()
    rels = list1[3].text.strip().split('\n')[1].strip()

    movie_dict['title'].append(title)
    movie_dict['type'].append(typ)
    movie_dict['release'].append(rels)

movie = pd.DataFrame(data = movie_dict)
movie.to_csv('./movie.csv', encoding='GBK', index=False, header=False)

