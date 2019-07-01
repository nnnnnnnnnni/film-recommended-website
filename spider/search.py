# coding=utf-8
import datetime
import requests
from bs4 import BeautifulSoup
import json

#爱奇艺
url_1='https://so.iqiyi.com/so/q_'
url_2='?source=input'
#腾讯视频
url_3='https://v.qq.com/x/search/?q='
#豆瓣
url_4='http://v.juhe.cn/movie/index?smode=&pagesize=1&offset=&dtype=&key=77efd25d38d674df2b8f8956755859df&title='
#电影天堂
url_5='http://s.ygdy8.com/plus/so.php?typeid=1&keyword='

s=datetime.datetime.now()

def get_html(url):
    """get the content of the url"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text

def get_h5(url):
    """get the content of the url"""
    response = requests.get(url)
    response.encoding = 'gb2312'
    return response.text

def get_aqiyi(html):
    soup = BeautifulSoup(html,'lxml') 
    try:
        if(len(soup.select('.mod_result_list > li'))<=0):
            info = {
                'code' : 404,
                'from' : 'aqiyi',
            }
        else:
            item = soup.select('.mod_result_list > li .result_info')[0]
            info = {
                'title': item.select('h3 a')[0].get_text().replace('\n',''),
                'link' : item.select('h3 a')[0].get('href'),
                'cv'   : item.select('.result_info_txt')[0].get_text() if len(item.select('.result_info_txt'))>0 else 'undefined',
                'time' : item.select('.result_info_cont')[3].select('span')[0].get_text().replace('\r\n            ','').strip() if len(item.select('.result_info_cont'))>0 else 'undefined',
                'from' : 'aqiyi',
                'code' : 200
            }
    except:
        info = {
            'code' : 404,
            'from' : 'aqiyi',
        }
    return info

def get_txsp(html):
    soup = BeautifulSoup(html,'lxml') 
    item = soup.select('._infos')
    try:
        if(len(item)<=0):
            info = {
                'code' : 404,
                'from' : 'txsp',
            }
        else:
            info = {
                'title' : item[0].select('.result_title em')[0].get_text(),
                'link'  : item[0].select('.result_title a')[0].get('href'),
                'cv'    : item[0].select('.desc_text')[0].get_text().replace('详细\ue621',''),
                'time'  : item[0].select('.result_title .sub')[0].get_text().split('/')[2].replace('）',''),
                'from'  : 'txsp',
                'code'  : 200
            }
    except:
        info = {
            'code' : 404,
            'from' : 'aqiyi',
        }
    return info

def get_douban(html):
    html = json.loads(html)
    try:
        text = html['result'][0]
        info = {
            'title' : text['title'],
            'link'  : 'http://movie.mtime.com/'+text['movieid'],
            'cv'    : text['plot_simple'],
            'time'  : text['year'],
            'genres': text['genres'],
            'from'  : 'douban',
            'code'  : 200
        }
    except:
         info = {
            'code' : 404,
            'from' : 'aqiyi',
        }
    return info

def get_dytt(html):
    soup = BeautifulSoup(html,'lxml') 
    try:
        if(len(soup.select('.co_content8 table'))<=0):
            info = {
                'code' : 404,
                'from' : 'dytt',
            }
        else:
            item = soup.select('.co_content8 table')[0]
            info = {
                'title' : item.select('tr')[0].get_text().replace('\n',''),
                'link'  : 'http://ygdy8.com'+item.select('tr a')[0].get('href'),
                'time'  : item.select('font')[-1].get_text(),
                'from'  : 'dytt',
                'code'  : 200
            }
    except:
        info = {
            'code' : 404,
            'from' : 'aqiyi',
        }
    return info


def search(key):
    k1=key.encode('gb2312')
    s=str(k1).replace('\\x','%').split('\'')[1]
    aqiyi_html=get_html(url_1+key+url_2)
    txsp_html=get_html(url_3+key)
    douban_html=get_html(url_4+key)
    dytt_html=get_h5(url_5+s)

    aqiyi_result=get_aqiyi(aqiyi_html)
    txsp_result=get_txsp(txsp_html)
    douban_result=get_douban(douban_html)
    dytt_result=get_dytt(dytt_html)

    data = []
    data.append(aqiyi_result)
    data.append(txsp_result)
    data.append(douban_result)
    data.append(dytt_result)
    return data

