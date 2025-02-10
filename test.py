import urllib.request
from bs4 import BeautifulSoup
import sqlite3



num = 807029
no = 86


url = f'https://comic.naver.com/webtoon/detail?titleId={str(num)}&no={str(no)}'
header = {
            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0'
            
}


def re():
    
    request = urllib.request.Request(url=url, headers=header)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response, 'html.parser')
    
    return soup

def create_db():
    
    con = sqlite3.connect(f'{str(num)}.db')
    cursor = con.cursor()

    create_sql = f'''CREATE TABLE IF NOT EXISTS "{no}" (
                        Num INT PRIMARY KEY,
                        Link VARCHAR(100)
                    );'''
                    
    cursor.execute(create_sql)
    
    con.commit()

def link_save(soup):

    con = sqlite3.connect(f'{str(num)}.db')
    cursor = con.cursor()
    
    for tag in soup.find(class_='wt_viewer').find_all('img'):
    
        try:
            
            insert_sql = f'''INSERT INTO "{no}" (Num, Link) VALUES (?, ?);'''

            link_num = tag['src'].split('_')[-1].split('.')[0]
            cursor.execute(insert_sql, (link_num, tag['src']))
        
            con.commit()
            
        except:
            
            pass


create_db()        
soup = re()
link_save(soup)


'''
with open('test.txt', 'w', encoding="utf-8") as File:
    
    File.write(html)
'''