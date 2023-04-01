from bs4 import BeautifulSoup 
import requests 
from csv import writer
import time


def find_reviews():

  url= "https://garza.es/iluminacion-inteligente/401278-Tira_LED_WiFi_para_exteriores-8430624012783.html"

  page = requests.get(url)


  soup = BeautifulSoup(page.content, 'html.parser')

  title_all = soup.find_all('div', class_ = 'product-container js-product-container')
  description_all = soup.find_all('div', class_ = 'iqit-accordion mb-5')
  features_all = soup.find_all('section', class_ = 'product-features')
 

  with open('dataList.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Description', 'Features','URL']
    thewriter.writerow(header)



    for title in title_all:
      Title = title.find('h1', class_ = 'h1 page-title').text.strip().replace('[ \r\n\t]+','')

    for description in description_all:
      Description = description.find('div', class_ = 'rte-content').text

    for features in features_all:
      Features = features.find('dl', class_ = 'data-sheet').text.replace('[ \r\n\t]+','')

    

      info = [Title,Description,Features]
      thewriter.writerow(info)

if __name__ == '__main__':
  # while True:
  find_reviews()
  
  time_wait = 1
  print(f'Waiting {time_wait} seconds... ')
  time.sleep(time_wait *6)