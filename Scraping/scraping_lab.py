# SCRAPING LAB 
# (20pts)
# Below is a link to a 10-day weather forecast at weather.com
# Use requests and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days by grabbing each of the following:
# Day, date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (10pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:  
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.

# Note: Although it is possible to pull a description of the weather which includes much of this data, that is not the intent.
# However, if you can do it and add the additional info, that works for me.
from bs4 import BeautifulSoup
import requests

url = "https://weather.com/weather/tenday/l/USIL0225:1:US"
page = requests.get(url)
#print(page)

bs = BeautifulSoup(page.text, "html.parser")
#print(bs.prettify())
print()
day = bs.findAll(class_="date-time")
date = bs.findAll(class_="day-detail clearfix")
description = bs.findAll(class_="description")
temperature = bs.findAll(class_="temp")
wind = bs.findAll(class_="wind")
humidity = bs.findAll(class_="humidity")


for i in range(10):
    print(day[i].text, date[i].text, "will be", description[i].text, "with a high/ low temperature of", temperature[i].text, "degrees. There will be a wind speed of", wind[i].text, "and a humidity of", humidity[i].text, sep=", ")

