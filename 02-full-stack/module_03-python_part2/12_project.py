import requests         # pip install requests
import inflection       # pip install inflection
import bs4              # pip install beautifulsoup4

html_doc = requests.get("https://www.dailysmarty.com/topics/python")
# print(html_doc.text)

def urls_to_title(urls):
    titles = []
    for url in urls:
        # remove the url part we don't want
        url = str(url).replace("/posts/", "")

        # transform this-kind-of-string to this_kind_of_string
        url = inflection.underscore(url)

        # This Kind Of String
        titles.append(inflection.titleize(url))
    
    return titles


soup = bs4.BeautifulSoup(html_doc.text, "html.parser")

html_links = soup.find_all("a")
links_list = []
for link in html_links:
    # print(link.get("href"))
    str_link = str(link.get("href"))
    if str_link.startswith("/posts/"):
        links_list.append(str_link)
    
titles_list = urls_to_title(links_list)

for title in titles_list:
    print(title)