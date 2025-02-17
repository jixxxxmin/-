import requests
import time



def session_sets():
    
    s = requests.Session()
    set_url = "https://naver.com"
    get_url = "https://naver.com"

    s.get(set_url, params={"userName": "John99"})
    s.get(set_url, params={"location": "NewYork"})

    response = s.get(get_url)
    print(response.text)


ss_s = time.time()
for _ in range(20):
    
    response = ss.get("https://naver.com")
ss_e = time.time()

print(ss_e - ss_s)

s = time.time()
for _ in range(20):
    
    response = requests.get("https://naver.com")
e = time.time()


print(e - s)