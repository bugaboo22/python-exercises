from bs4 import BeautifulSoup
import ssl
import re
import urllib.request, urllib.parse, urllib.error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = 'http://python-data.dr-chuck.net/known_by_Conar.html'
url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
href = soup('a')
#print href

for i in range(count):
    link = href[position].get('href', None)
    print(href[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')