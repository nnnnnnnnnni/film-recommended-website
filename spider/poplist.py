# coding=utf-8
import datetime
import requests
from bs4 import BeautifulSoup

url='https://maoyan.com/board'


def get_html(url):
    """get the content of the url"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text

def get_content(html):
    data = []
    soup = BeautifulSoup(html,'lxml') 
    update_time=soup.select('#app .main .update-time')[0].get_text()
    ls=soup.select('#app .main .board-wrapper dd')
    for item in ls:
        link = 'http://maoyan.com'+item.select('a')[0].get('href')
        html=get_html(link)
        soup1 = BeautifulSoup(html,'lxml') 
        img = soup1.select('.avatar')[0].get('src').split('@')[0]
        info={
            'rank'  : item.select('i')[0].get_text(),
            'title' : item.select('a')[0].get('title'),
            'link'  : link,
            'img_url'   : img,
            'stars' : item.select('.star')[0].get_text().replace('\n        ','').strip(),
            'score' : item.select('.score i')[0].get_text()+item.select('.score i')[1].get_text()
        }
        data.append(info)
        if(len(data)==5):
            break
    return data


def pop_list():
    html=get_html(url)
    ls=get_content(html)
    return ls
