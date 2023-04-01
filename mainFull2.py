from bs4 import BeautifulSoup
import requests

# url= "https://garza.es/10-iluminacion?page=1"
url= requests.get("https://garza.es/10-iluminacion").text

# page = requests.get(url)
# print(url)
soup = BeautifulSoup(url, 'lxml')

# lists = soup.find_all('div', class_="js-product-miniature-wrapper col-12")
# lists = soup.find_all('article', class_="product-miniature product-miniature-default product-miniature-list js-product-miniature")
lists = soup.find_all('div', class_="col col-description")
print(lists)
# lists = soup.find_all('div', class_="disabled js-search-link")










# for list in lists:
#  title = lists.find('div', class_="col col-description").h2.a['href']
#  info=[title]
#  print(info)