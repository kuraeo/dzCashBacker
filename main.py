import requests
from bs4 import BeautifulSoup
import lxml

user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
header = {"User-Agent": user}
session = requests.Session()
# count = 2

for j in range(1, 7):
    print(f"Page = {j}")
    url = f"https://cash-backer.club/shops?page={j}"
    response = session.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_cashbacks = soup.find_all('div', class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")

        for product in all_cashbacks:
            cashback = product.find("div", class_="shop-rate")
            title = product.find("div", class_="shop-title")
            print(title.text, cashback.text)
            with open("Name_and_Cashback.txt", "a", encoding = "utf-8") as file:
                    file.write(f"{cashback.text} {title.text}\n")


