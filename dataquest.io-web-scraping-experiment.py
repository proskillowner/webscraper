import requests
from bs4 import BeautifulSoup

page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")

# print(page.status_code)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

doc = list(soup.children)
# print(doc)

html = list(soup.children)[2]
# print(html)

body = list(html.children)[3]
# print(body)

p = list(body.children)[1]
# print(p)
# print(p.get_text())

allp = soup.find_all('p')
print(allp)
