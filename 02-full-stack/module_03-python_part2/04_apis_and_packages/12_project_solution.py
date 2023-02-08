# Jordans's solution

import requests
import bs4
from inflection import titleize

def titles_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in str(url):
            url = url.split("/")[-1]
            url = url.replace("-", " ")
            url = titleize(url)
            titles.append(url)


    for link in links:
        # print(link.get("href"))
        post_formatter(link.get('href'))

    return titles


r = requests.get("https://www.dailysmarty.com/topics/python")
# print(r.text) # shows the full html document

soup = bs4.BeautifulSoup(r.text, "html.parser")
# print(soup)

links = soup.find_all("a")  # to get all the links from the page

titles = titles_generator(links)
for title in titles:
    print(title)