import requests
from bs4 import BeautifulSoup

url = "https://tr.azrhymes.com/?"
t = "tekerlemeler"

kelime = input("Kelime giriniz: ")

search_url = url + t + "=" + kelime
content = requests.get(search_url).content
soup = BeautifulSoup(content, "html.parser")


# Çekilen HTML içeriğini yazdır
print(soup.prettify())


def get_rhyme(soup):
    r = soup.find_all("span", {"class": "result"})
    return r


kafiyeler = get_rhyme(soup)

ilk_12 = kafiyeler[:12]

for i in ilk_12:
    print(i.text.replace(",",""))
