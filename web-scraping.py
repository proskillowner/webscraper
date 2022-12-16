from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas

# driver = webdriver.Chrome("E:\\chromedrvier.exe")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

products = []
prices = []
ratings = []

driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class':'_31qSD5'}):
	name = a.find('div', attrs={'class':'_3wU53n'})
	price = a.find('div', attrs={'class':'_1vc40E _2rQ-NK'})
	rating = a.find('div', attrs={'class':'hGSR34 _2beYZw'})
	products.append(name.text)
	prices.append(price.text)
	ratings.append(rating.text)

df = pandas.DataFrame({'Product Name':products, 'Price':prices, 'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')