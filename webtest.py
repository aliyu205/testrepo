import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

counts = 7
count = int(counts)

index = 17
pos = int(index)

while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    lst = list()
    tags = soup('a')
    for tag in tags:
        href = tag.get('href', None)
        lst.append(href)
    url = lst[pos]
    print('Retrieving:', url)
    count = count - 1


    
   

   
    
