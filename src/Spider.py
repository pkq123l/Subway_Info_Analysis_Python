import json
import requests
import sqlite3
from bs4 import BeautifulSoup
import threading


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

# 连接数据库
conn = sqlite3.connect('../city_line_new.db', check_same_thread=False)
cur = conn.cursor()
#cur.execute('drop table info')
cur.execute('create table info(city text,line text,name text)')
conn.commit()
# 关闭数据库
#conn.close()

lock = threading.Lock()
lock2 = threading.Lock()

def get_message(ID, cityname, name):
    '''
    地铁线路信息获取
    '''
    url = 'http://map.amap.com/service/subway?_1555502190153&srhdata=' + ID + '_drw_' + cityname + '.json'
    response = requests.get(url=url, headers=headers)
    html = response.text
    result = json.loads(html)
    for i in result['l']:
        for j in i['st']:
            # 判断是否含有地铁分线
            if len(i['la']) > 0:
                print(name, i['ln'] + '(' + i['la'] + ')', j['n'])
                try:
                    lock2.acquire(True)
                except:
                    pass
                cur.execute("insert into info(city, line, name) values(?, ?, ?)", (name, i['ln'] + '(' + i['la'] + ')', j['n']))
                try:
                    lock2.release()
                except:
                    pass
                #cur.execute('select * from info')
                #print(cur.fetchall())
                conn.commit()
                with open('../subway_new.csv', 'a+', encoding='gbk') as f:
                    f.write(name + ',' + i['ln'] + '(' + i['la'] + ')' + ',' + j['n'] + '\n')
            else:
                print(name, i['ln'], j['n'])
                try:
                    lock2.acquire(True)
                except:
                    pass
                cur.execute("insert into info(city, line, name) values(?, ?, ?)", (name, i['ln'], j['n']))
                try:
                    lock2.release()
                except:
                    pass
                # cur.execute('select * from info')
                #print(cur.fetchall())
                #conn.commit()
                with open('../subway_new.csv', 'a+', encoding='gbk') as f:
                    f.write(name + ',' + i['ln'] + ',' + j['n'] + '\n')

def get_city():
    '''
    城市信息获取
    '''
    url = 'http://map.amap.com/subway/index.html?&1100'
    response = requests.get(url=url, headers=headers)
    html = response.text
    # 编码
    html = html.encode('ISO-8859-1')
    html = html.decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    # 城市列表
    res1 = soup.find_all(class_="city-list fl")[0]
    res2 = soup.find_all(class_="more-city-list")[0]
    return res1, res2
    

if __name__ == '__main__':
    res1, res2 = get_city()

    for i in res1.find_all('a'):
        # 城市ID值
        ID = i['id']
        # 城市拼音名
        cityname = i['cityname']
        # 城市名
        name = i.get_text()
        # get_message(ID, cityname, name)
        t = threading.Thread(target=get_message, args=(ID, cityname, name,))
        t.start()
    for i in res2.find_all('a'):
        # 城市ID值
        ID = i['id']
        # 城市拼音名
        cityname = i['cityname']
        # 城市名
        name = i.get_text()
        # get_message(ID, cityname, name)
        t = threading.Thread(target=get_message, args=(ID, cityname, name,))
        t.start()
    
   
