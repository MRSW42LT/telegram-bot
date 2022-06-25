import requests
from bs4 import BeautifulSoup

def cotar_dolar():

    page = requests.get('https://dolarhoje.com/')

    soup = BeautifulSoup(page.text, 'html.parser')

    dolar_price = soup.find(class_='cotMoeda nacional')
    dolar_price = dolar_price.find('input').get('value')

    return str(dolar_price)

print(cotar_dolar())