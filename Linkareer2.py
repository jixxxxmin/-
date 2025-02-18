import requests
import json
import time



page_num = 0
url = f"https://api.linkareer.com/graphql?operationName=RecruitList&variables=%7B%22filterBy%22%3A%7B%22status%22%3A%22OPEN%22%2C%22activityTypeID%22%3A%225%22%2C%22categoryIDs%22%3A%5B%22111%22%5D%2C%22regionIDs%22%3A%5B%222%22%2C%229%22%2C%225%22%5D%2C%22jobTypes%22%3A%5B%22INTERN%22%5D%7D%2C%22activityOrder%22%3A%7B%22field%22%3A%22RECENT%22%2C%22direction%22%3A%22DESC%22%7D%2C%22page%22%3A{page_num}%2C%22pageSize%22%3A20%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%221de6571120f5792968cfc5b56c6ee631a59d588ab75051708d13907844dd87b2%22%7D%7D"
    

def session_sets(page_num):
    
    s = requests.Session()
    set_url = url
    get_url = url

    s.get(set_url, params={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"})
    
    response = s.get(get_url)
    response = json.loads(response.text)

    
    nodes = response.get('data', {}).get('activities', {}).get('nodes', [])
    
    
    if nodes:
    
        for node in nodes:
            
            id = node.get('id', {})
            
            print(id)
            
    else:   return 1


while True:
        
        page_num+=1
        check = session_sets(page_num)
        
        if check:  break