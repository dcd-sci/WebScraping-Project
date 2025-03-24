# This script gathers all products from the url on base_url
# and stores it on a file called 'products.txt'

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.pakatatu.com/categoria-produto/loja/'
n = 2

products_dict = {}

while True:
    print(f'\nScraping {base_url}')

    req = requests.get(base_url)
    print(f'Status code: {req.status_code}')

    if req.status_code != 200:
        print('Something went wrong: status code not 200')
        break

    soup = BeautifulSoup(req.content, 'html.parser')
    products = soup.find_all('li', class_='minimal')

    for product in products:
        product_name = product.find('h2', class_='woocommerce-loop-product__title').get_text()
        product_price = product.find('bdi').get_text()
        products_dict[product_name] = product_price

    print(products_dict)

    if n == 14:
        print("Scraping complete.") # this number is hard codes which is not ideal but it'll do for the moment
        break

    base_url = f'https://www.pakatatu.com/categoria-produto/loja/page/{n}/'
    n += 1


with open('products.txt', 'w', encoding='utf-8') as file:
    for product_name, product_price in products_dict.items():
        file.write(f'{product_name} - {product_price}\n')
print('Content saved in "products.txt" file.')
