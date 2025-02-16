import requests
import time


ss = requests.Session()

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