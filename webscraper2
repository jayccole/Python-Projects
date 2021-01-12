from bs4 import BeautifulSoup
import requests

url = requests.get('https://thetrove.is/Books/BattleTech%20%5Bmulti%5D/').text

soup = BeautifulSoup(url, 'lxml')
#print(soup.prettify)

for link in soup.find_all('a'):
    print(link.get('href'))