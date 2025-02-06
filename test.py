import urllib.request, requests
from bs4 import BeautifulSoup
import chardet


url1 = "https://linkareer.com/list/intern?filterBy_activityTypeID=5&filterBy_categoryIDs=111&filterBy_jobTypes=INTERN&filterBy_regionIDs=2&filterBy_regionIDs=9&filterBy_regionIDs=5&filterBy_status=OPEN&orderBy_direction=DESC&orderBy_field=RECENT&page=1"
header = {
    
                'sec-ch-ua' :'"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
                'sec-ch-ua-mobile' : '?0',
                'sec-ch-ua-platform' : '"Windows"',
                'upgrade-insecure-requests': '1',
                'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0'
}


request = urllib.request.Request(url=url1, headers=header)
response = urllib.request.urlopen(request)
html = response.read()

detected_encoding = chardet.detect(html)['encoding']
print(detected_encoding)
html = html.decode(detected_encoding)


with open('test.txt', 'w', encoding="utf-8") as File:
    
    File.write(html)