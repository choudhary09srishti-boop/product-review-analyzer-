import requests
from bs4 import BeautifulSoup
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def scrape_books(url, max_pages=5):
    reviews = []
    page = 1

    while page <= max_pages:
        print(f"Scraping page {page}...")
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            print(f"Failed to fetch page {page}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.select("article.product_pod")

        if not books:
            break

        for book in books:
            title = book.select_one("h3 a")["title"]
            rating = book.select_one("p.star-rating")["class"][1]
            price = book.select_one("p.price_color").text.strip()

            reviews.append({
                "title": title,
                "rating": rating,
                "price": price,
                "review": f"This book is rated {rating} stars and priced at {price}."
            })

        next_btn = soup.select_one("li.next a")
        if next_btn:
            base = url.rsplit("/", 1)[0]
            url = base + "/" + next_btn["href"]
            page += 1
            time.sleep(1)
        else:
            break

    return reviews


if __name__ == "__main__":
    data = scrape_books("https://books.toscrape.com/catalogue/page-1.html")
    for d in data[:3]:
        print(d)
        