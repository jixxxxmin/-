import urllib.request
import json
import sqlite3



class stack():
    
    def __init__(self):
        
        self.stack = []
        
    def __str__(self):
        
        return str(self.stack)
    
    def push(self, value):
        
        self.stack.append(value)
        
    def pop(self):
        
        if self.isEmpty():  return IndexError("Stack Empty")
        else:   self.stack.pop()

    def isEmpty(self):
        
        return len(self.stack) == 0



def head(page_num):
    
    url = f"https://api.linkareer.com/graphql?operationName=RecruitList&variables=%7B%22filterBy%22%3A%7B%22status%22%3A%22OPEN%22%2C%22activityTypeID%22%3A%225%22%2C%22categoryIDs%22%3A%5B%22111%22%5D%2C%22regionIDs%22%3A%5B%222%22%2C%229%22%2C%225%22%5D%2C%22jobTypes%22%3A%5B%22INTERN%22%5D%7D%2C%22activityOrder%22%3A%7B%22field%22%3A%22RECENT%22%2C%22direction%22%3A%22DESC%22%7D%2C%22page%22%3A{page_num}%2C%22pageSize%22%3A20%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%221de6571120f5792968cfc5b56c6ee631a59d588ab75051708d13907844dd87b2%22%7D%7D"
    header = {
                "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    
    return url, header

def re(page_num, id_num):
    
    url, header = head(page_num)
    
    request = urllib.request.Request(url=url, headers=header)
    response = urllib.request.urlopen(request)
    response = json.loads(response.read())

   
    nodes = response.get('data', {}).get('activities', {}).get('nodes', [])

    if nodes:
    
        for node in nodes:
            
            id = node.get('id', {})
            
            id_num.push(id)
            
    else:   return 1

def each_id():

    id_num = stack()
    page_num = 0
    while True:
        
        page_num+=1
        check = re(page_num, id_num)
        
        if check:  break
        
    return id_num


id_num = each_id()
print(id_num)