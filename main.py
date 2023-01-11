import requests
from bs4 import BeautifulSoup


url = "https://vnexpress.net/giao-duc"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('a', class_="btn-page")
list_next = soup.find_all('a', class_="btn-page next-page")

for list in lists:
    list_article = []
    while True:
        print(f"Trang {i}")
        index = 0
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
                    print(f"Title: ", h1_title)
                    # print(f"Description: ", description)
        #             article = {"title": h1_title, "description": description}
        #             list_article.append(article)
        # print(list_article)

    else:
        break

