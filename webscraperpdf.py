from bs4 import BeautifulSoup
import requests

url = requests.get('https://thetrove.is/Books/BattleTech%20%5Bmulti%5D/').text

soup = BeautifulSoup(url, 'lxml')
#print(soup.prettify)

for link in soup.find_all('td', class_='link'):
    link_2 = link.text
    link_3 = link_2.split('=')
    print(link_3)

    try:
        pass
    except Exception as e:
        raise e

    print()