# Need to information title, description, variant option with price, price, category (All products) 

from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://www.etsy.com/shop/BellaBerryDesigns'
page = requests.get(url)
# print(page)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

# pagination = soup.find('ul', class_='wt-action-group wt-list-inline wt-flex-no-wrap  wt-flex-no-wrap wt-pt-xl-2 wt-pb-xl-4')

pagination = soup.find_all("div", class_="wt-show-xl")
# print(pagi)
for page in pagination:
    if page.find("nav", attrs={"aria-label":"Pagination of listings"}):
        nav_attrs = page.find("nav", attrs={"aria-label":"Pagination of listings"})
        # print(nav_attrs)
        spans = nav_attrs.find_all('span')
        for i in range(3, len(spans)-1, 2):
            # print(spans[i].text.strip())
            no=(spans[i].text.strip())
            # print(no)
            if no.strip().isdigit():
                # products_url = "https://garza.es/10-iluminacion?page="+no.strip()
                products_url = "https://www.etsy.com/shop/BellaBerryDesigns?page="+no.strip()+"#items"
                products_page = requests.get(products_url)
                # print(products_page)
                products_soup = BeautifulSoup(products_page.content, 'html.parser')
                # print(products_soup)
                # products = products_soup.find_all('div', class_='js-merch-stash-check-listing')
                # products = products_soup.find_all('div', class_='v2-listing-card')
                # products = products_soup.find_all('div', class_='wt-position-relative')
                # products = products_soup.find_all('div', class_='wt-grid__item-xs-6')
                # products = products_soup.find_all('div', class_='wt-flex-shrink-xs-1')

                products = products_soup.find_all('div', class_='wt-grid__item-xl-3')
                # products = products_soup.find_all('div', class_='wt-grid__item-lg-4')
                # products = products_soup.find_all('div', class_='wt-grid__item-md-4')
                # print(products)
                # print(len(products))
                for product in products:
                    try:
                        Title = product.find('h3', class_='wt-text-caption').text.strip()
                    except:
                        print('Title : '+Title[product])
                    # print(title_link)
                    try:
                        product_price = product.find('span', class_='currency-value').text
                    except:
                        print('Price : '+product_price[product])
                    # print(product_price)

                    link = product.find('a')
                    single_prod_url = link.get('href')
                    print(single_prod_url)
                    single_product_page = requests.get(single_prod_url)
                    single_product_soup = BeautifulSoup(single_product_page.content, 'html.parser')

                    with open('dataListESTY.csv', 'a', encoding='utf8', newline='') as f:
                        thewriter = writer(f)

                        # header = ['Title', 'Description', 'Price','Variant option with price']
                        # thewriter.writerow(header)
                        

                        # single_product_title = single_product_soup.find('h1', class_='wt-text-body-01').text.strip()
                        # print(single_product_title)

                        # product_price = single_product_soup.find('p', class_='wt-text-title-03').text
                        # print(product_price)
                        
                        try:
                            Description = single_product_soup.find('p', class_='wt-break-word').text
                        except:
                            print('V_product_price : '+Description[product])
                        # print(product_price)

                        single_product_details = single_product_soup.find('div', class_='wt-select')
                        # print(single_product_details)
                        try:
                            variant_option_with_price = single_product_details.find('select', id='variation-selector-0').text.replace('Select an option','') if single_product_details.find('select', id='variation-selector-0') else "N/A"
                        except:
                            print('data_sheet_details : ')
                        # print(data_sheet_details)
                        # data_sheet_col_names = data_sheet_details.find('option').text
                        # print(data_sheet_col_names)

                        info = [Title,variant_option_with_price,product_price,Description]
                        thewriter.writerow(info)

print('All done!')
















# for page in page_numbers:
#     no = page.find('a', class_="wt-action-group__item").find('span', class_="wt-screen-reader-only")
#     print(no)
    # print(no.strip())
    # if no.strip().isdigit():
    #     products_url = "https://www.etsy.com/shop/BellaBerryDesigns?page="+no.strip()+#items