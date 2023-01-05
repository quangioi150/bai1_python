import json
import psycopg2
import requests
from bs4 import BeautifulSoup
import time

class CrawArticle(object):
    def __init__(self, url: str):
        pass

    def get_title(self) -> str:
        pass

    def get_description(self) -> str:
        pass

    def get_comments(self) -> list:
        pass

    def craw(self):
        title = self.get_title()
        description = self.get_description()
        comments = self.get_comments()
        print(title, description, comments)

        list_article = []
        for i in range(1, 30):
            print(f"Trang {i}")
            index = 0
            if i == 1:
                url = "https://vnexpress.net/giao-duc/tin-tuc"
            else:
                url = f"https://vnexpress.net/giao-duc/tin-tuc-p{i}"
            req = requests.get(url, 'html.parser')
            soup = BeautifulSoup(req.content, 'html.parser')
            contents = soup.findAll("article", {"class": "item-news"})

            for content in contents:
                    index += 1
                    content_div = content.find("h2", {"class": "title-news"})
                    if content_div:
                        content_a = content_div.find("a", href=True)
                        detail_req = requests.get(content_a.get("href"), 'html.parser')
                        detail_soup = BeautifulSoup(detail_req.content, 'html.parser')
                        h1_title = detail_soup.find("h1", {"class": "title-detail"})
                        description = detail_soup.find("article", {"class": "fck_detail"})
                        if h1_title and description:
                            h1_title = h1_title.text
                            description = description.text
                            print(f"Title{index}: ", h1_title)
                            article = {"title": h1_title, "description": description}
                            list_article.append(article)
        print(list_article)
if __name__ == '__main__':
    data = CrawArticle(object)
    start_time = time.time()
    data.craw()
    print("--- %s seconds ---" % (time.time() - start_time))


