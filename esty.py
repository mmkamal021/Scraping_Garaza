# Need to information title, description, variant option with price, price, category (All products) 

from bs4 import BeautifulSoup
import requests

url = 'https://www.etsy.com/shop/BellaBerryDesigns'
page = requests.get(url)
# print(page)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

# pagination = soup.find('ul', class_='wt-action-group wt-list-inline wt-flex-no-wrap  wt-flex-no-wrap wt-pt-xl-2 wt-pb-xl-4')

pagi = soup.find_all("div", class_="wt-show-xl")
# print(pagi)
nav_attrs = pagi.find_all("nav", attrs={'aria-label':'Pagination of listings'})
print(nav_attrs)

# pagination = soup.find('nav', attrs={'aria-label':'Pagination of listings'})
# print(pagination)

# page_num = pagination.find_all('li')
# page_numbers = page_num.find_all('span')
# for i in range(0, len(page_numbers)):
#  if page_numbers[i].isDigit():
#   print(page_numbers[i])















# for page in page_numbers:
#     no = page.find('a', class_="wt-action-group__item").find('span', class_="wt-screen-reader-only")
#     print(no)
    # print(no.strip())
    # if no.strip().isdigit():
    #     products_url = "https://www.etsy.com/shop/BellaBerryDesigns?page="+no.strip()+#items