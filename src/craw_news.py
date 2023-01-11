import time

import requests
from bs4 import BeautifulSoup


class CrawArticle(object):
    def get_title(self) -> str:
        list_article = []
        for i in range(1, 30):
            print(f"Trang {i}")
            index = 0
            if i == 1:
                url = "https://vnexpress.net/giao-duc"
            else:
                url = f"https://vnexpress.net/giao-duc-p{i}"
            req = requests.get(url, 'html.parser')
            soup = BeautifulSoup(req.content, 'html.parser')
            contents = soup.findAll("article", {"class": "item-news"})
            for content in contents:
                index += 1
                content_div = content.find("h3", {"class": "title-news"})
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
                        print(f"Description{index}: ", description)
                        article = {"title": h1_title, "description": description}
                        list_article.append(article)
            print(list_article)

    def get_description(self, description):
        if description:
            description = description.text
        return description

    def get_comments(self, article_id):
        req = requests.get(
            url=f"https://usi-saas.vnexpress.net/index/get?objectid={article_id}&objecttype=1&siteid=1000000&usertype=4")
        res = req.json()
        comments = res['data'].get("items")
        return comments

    def craw(self):
        title = self.get_title()
        description = self.get_description()
        comments = self.get_comments()
        print(title, description, comments)


if __name__ == '__main__':
    data = CrawArticle()
    start_time = time.time()
    data.craw()
    print("--- %s seconds ---" % (time.time() - start_time))
