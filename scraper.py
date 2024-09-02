import requests
from bs4 import BeautifulSoup
import csv

#URL
url = 'http://books.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(response.content,'html.parser')

books = soup.find_all('article', class_='product_pod')

with open('books.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title','Price','Rating'])

    for book in books:
        title = book.h3.a['title']

        price = book.find('p',class_= 'price_color').get_text()
        # Extract the book rating
        rating_class = book.find('p', class_='star-rating')['class']
        rating = rating_class[1]  # The second class name represents the rating

        # Write the extracted data to CSV
        writer.writerow([title, price, rating])

print("Scraping completed and data saved to books.csv")