from bs4 import BeautifulSoup
import requests
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def parse():
    URL = 'https://www.krsk.kp.ru/online/'
    #чтобы не приняли за робота
    HEADERS = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    #Делает запрос на сайт
    response = requests.get(URL, headers = HEADERS)
    #Парсит HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    #конкретный блок ищет
    items = soup.findAll('div', class_ ='sc-1tputnk-13 ixDVFm')
    #список в который будем заносить словарь
    comps = []
    #перебор с добавлением в список словаря уже конкретного текста из блока
    for item in items:
        comps.append({
            #объекты словаря(берем с какого-то одного объекта инфу и запихиваем сюда)
            'title' : item.find('a', class_ = 'sc-1tputnk-2 drlShK').get_text(strip = True),
            'time'  : item.find('span', class_ = 'sc-1tputnk-9 gpa-DyG').get_text(strip = True),  
            'link'  : item.find('a', class_ = 'sc-1tputnk-2 drlShK').get('href')
        })
    
    #вывод каждого объекта из словаря построчно, а не в одну строку
    for comp in comps:
        print(comp['title'], 'TIME:', comp['time'], '\nhttps://www.krsk.kp.ru' + comp['link'], '\n')
parse()