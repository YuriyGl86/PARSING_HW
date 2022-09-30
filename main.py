import bs4
import requests
from fake_headers import Headers

KEYWORDS = ['Incident Manager', 'MicroSD', 'ГЕЙМДЕВ']
URL = "https://habr.com/ru"


def get_articles_with_keywords(KEYWORDS):
    headers = Headers(os="win", headers=True).generate()
    response = requests.get(URL, headers=headers)

    soup = bs4.BeautifulSoup(response.text, features='html.parser')
    articles = soup.find_all('article')

    for article in articles:
        href = article.find(class_="tm-article-snippet__title-link").attrs['href']
        article_url = f'{URL}{href[3:]}'
        article_headers = Headers(browser="chrome", os="win", headers=True).generate()
        article_page = requests.get(article_url, headers=article_headers).text
        article_soup = bs4.BeautifulSoup(article_page, features='html.parser')
        article_all_text = article_soup.find('article').get_text()

        if any([word in article_all_text for word in KEYWORDS]):
            title = article_soup.find("h1").find('span').text
            date = article_soup.find('span', class_="tm-article-snippet__datetime-published").find('time').get('title')
            print(f'{date} - {title} - {article_url}')


if __name__ == '__main__':
    get_articles_with_keywords(KEYWORDS)
