#example webscrape code
import pandas as pd
import requests
from bs4 import BeautifulSoup

#I chose this site because they have interesting products and don't change their naming conventions like larger stores often do
url='https://beadleandgrimms.com/collections/frontpage'

page_object=requests.get(url)

parsed_object=BeautifulSoup(page_object.content,'html.parser')

toy_boxes=parsed_object.find_all('li',class_='grid__item')

toy_df=pd.DataFrame(columns=['Name','Price'])

for toy in toy_boxes:
    name=toy.find('a', class_='full-unstyled-link').text
    price=toy.find('span', class_='price-item price-item--regular').text
    miniToy=pd.DataFrame(columns=list(toy_df.columns), data=[[name,price]])
    toy_df=pd.concat([toy_df,miniToy])
    print(name)
    print(price)