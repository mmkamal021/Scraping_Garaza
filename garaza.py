from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://garza.es/10-iluminacion'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

pagination = soup.find('ul', class_='page-list')

page_numbers = pagination.find_all('li')
for page in page_numbers:
    no = page.find('a', class_="js-search-link").text
    # print(no.strip())
    if no.strip().isdigit():
        products_url = "https://garza.es/10-iluminacion?page="+no.strip()
        products_page = requests.get(products_url)
        products_soup = BeautifulSoup(products_page.content, 'html.parser')
        products = products_soup.find_all('div', class_='js-product-miniature-wrapper')
        # print(len(products))

    
        # header = ['Title', 'Description', 'Features','URL']
        # thewriter.writerow(header)
        for product in products:
            title_link = product.find('h2', class_='h3')
            link = title_link.find('a')
            single_prod_url = link.get('href')
            single_product_page = requests.get(single_prod_url)
            single_product_soup = BeautifulSoup(single_product_page.content, 'html.parser')

            with open('dataList.csv', 'a', encoding='utf8', newline='') as f:
             thewriter = writer(f)
             # header = ['Title', 'Description', 'Features','URL']
             # thewriter.writerow(header)
      
             single_product_title = single_product_soup.find('div', class_='product_header_container').find('h1', class_="page-title").find('span').text
             single_product_price = single_product_soup.find('div', class_='product-prices').find('span', class_="product-price").text.strip()
             


             single_product_description = single_product_soup.find('div', id='productdaas-accordion-description').text if single_product_soup.find('div', id = 'productdaas-accordion-description') else "N/A"
             



             single_product_details = single_product_soup.find('div', id='product-details')
             data_sheet_details = single_product_details.find('section', class_='product-features')
             
             try:
              data_sheet_col_names = data_sheet_details.find_all('dt')
             except:
              data_sheet_col_names="None"



             try:
              data_sheet_col_values = data_sheet_details.find_all('dd')
             except:
              data_sheet_col_names="None"

             try:
              other_product_details = single_product_details.find_all('div')
             except:
              other_product_details="None"

      
             
             # print('Title: ' + single_product_title)
             # print('Product URL: ' + single_prod_url)
             # print('Price ' + single_product_price)
             # print('Description ' + single_product_description)
             # print('Data sheet details:')

             info = [single_product_title,single_product_description,single_prod_url,Feature]
             thewriter.writerow(info)
             
             Feature = []
            try:
             for i in range(0, len(data_sheet_col_names)):
                 # print(data_sheet_col_names[i].text+':'+data_sheet_col_values[i].text)
                 Feature.append(data_sheet_col_names[i].text+':'+data_sheet_col_values[i].text)
            except:
             # other_product_details="None"
             data_sheet_col_names="None"
            # print(Feature)


            # info = [single_product_title,single_product_description,single_prod_url,Feature]
            # thewriter.writerow(info)
            

            # print('Other product details:')
            # for detail in other_product_details:
            #     if detail.find('label'):
            #         other_product_details_labels = detail.find('label').text.strip()
            #         other_product_details_values = detail.find('span').text.strip()
            #         print(other_product_details_labels+' '+other_product_details_values)


print('All done!')