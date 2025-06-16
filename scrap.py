from bs4 import BeautifulSoup
import json
import requests
import csv


url = "https://books.toscrape.com/"

def book_details(url):
    response = requests.get(url)

    
    response.encoding = 'utf-8'

    if response.status_code != 200:
        print("Sorry, request failed.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    print("\n", soup.title.string, "\n")

    all_books = []


    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price_text = book.find("p", class_="price_color").text  # e.g. '£51.77'
        currency = price_text[0]  # '£'

        # lean price and handle encoding issues
        price = float(price_text.replace('£', '').replace('Â', '').strip())

        book_info = {
            "title": title,
            "currency": currency,
            "price": price
        }

        all_books.append(book_info)
        print(title, currency, price)


    with open("bookdetail.json", "w", encoding="utf-8") as f:
        json.dump(all_books, f,  ensure_ascii=False)

    print(f"\nSaved {len(all_books)} books to 'bookdetail.json'.")

# calling the function here with argument 


book_details(url)
 