import bs4
import requests
from fake_headers import Headers

URL ="https://habr.com/ru/all/"
headers = Headers(os="win", headers=True).generate()

resp = requests.get(URL, headers=headers)

soup = bs4.BeautifulSoup(resp.text, features='html.parser')

articles = soup.find_all('article')

for article in articles:
    txt = article.get_text()
    print(txt)
    print('*' * 50)
    # hubs = [hub.text for hub in hubs]
    # print(hubs)