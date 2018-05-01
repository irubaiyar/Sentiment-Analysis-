

import bs4
import requests

URL = "http://www.cbc.ca/cmlink/rss-topstories"

response = requests.get(URL)
with open('feed.xml', 'wb') as file:
    file.write(response.content)

xml=open('feed.xml', 'r')
#pass xml to beautiful soup parser
soup = bs4.BeautifulSoup(xml, "xml")
#get all the instances of the "item" class
headlines= soup.find_all("item")
#iterate through each item class and extract the string portion of the "title" tag
headlineList=[]
for headline in headlines:
    print(headline.find("title").string) # print to standard output
    headlineList.append(headline.find("title").string)


