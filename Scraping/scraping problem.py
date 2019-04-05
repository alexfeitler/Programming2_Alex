# SCRAPING PROBLEM (12pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list
# items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweetslocated on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.

from bs4 import BeautifulSoup
import requests

url = "https://twitter.com/stephenasmith"  # stephen a is the man
page = requests.get(url)
print(page)

bs = BeautifulSoup(page.text, "html.parser")
print(bs.prettify())
print()
tweets = bs.findAll(class_="TweetTextSize")
x = 0

for i in range(5):
    x += 1
    print(x,end=".) ")
    print(tweets[i].text)

    print()
