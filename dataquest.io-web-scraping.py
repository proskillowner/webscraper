import requests
from bs4 import BeautifulSoup
import pandas

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')

with open('test.html', 'w') as f:
	f.write(soup.prettify())

seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
# print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
# print(period)
# print(short_desc)
# print(temp)

img = tonight.find("img")
desc = img['title']
# print(desc)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
short_desc_tags = seven_day.select(".tombstone-container .short-desc")
short_descs = [sdt.get_text() for sdt in short_desc_tags]
temp_tags = seven_day.select(".tombstone-container .temp")
temps = [tt.get_text() for tt in temp_tags]
desc_tags = seven_day.select(".tombstone-container img")
descs = [dt["title"] for dt in desc_tags]
# print(periods)
# print(short_descs)
# print(temps)
# print(descs)

weather = pandas.DataFrame({
	"period": periods,
	"short_desc": short_descs,
	"temp": temps,
	"desc": descs,
})

print(weather)
weather.to_csv('weather.csv', index=False, encoding='utf-8')
