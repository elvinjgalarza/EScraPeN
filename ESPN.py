print("\n"*500)
print("""
 :::      :::===== :::====  == :::===       :::=====  :::====       :::  === :::= === ::: :::===== :::  === :::=== 
 :::      :::      :::==== ==  :::          :::       :::  ===      ::: ===  :::===== ::: :::      ::: ===  :::    
 ===      ======     ===        =====       === ===== ===  ===      ======   ======== === ===      ======    ===== 
 ===      ===        ===           ===      ===   === ===  ===      === ===  === ==== === ===      === ===      ===
 ======== ========   ===       ======        =======   ======       ===  === ===  === ===  ======= ===  === ====== 
                                                                                                                   
""")
import requests

page = requests.get("http://www.espn.com/nba/team/_/name/ny/new-york-knicks")
#print(page.status_code)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, "html5lib")

parent = soup.find(id="global-viewport")

child0 = parent.find(id="pane-main")
child1 = child0.find(id="main-container")
child2 = child1.find(class_="main-content layout-abc")
child3 = child2.find(id="news-feed")
child4 = child3.find(id="news-feed-content")
child5 = child4.find(class_="container-wrapper")
child6 = child5.find(class_="container")
child7 = child6.find(class_="news-feed-item news-feed-story-package")
child8 = child7.find(class_="text-container no-headlines")
child9 = child8.find(class_="item-info-wrap")

#after becoming a decamom, I am finally where I want to be
#There must be a more efficient way tbh...
print(u"\U0001F3C0")
timestamp = child9.find(class_="news-feed_item-meta")
timestamp = timestamp.find(class_="timestamp").get_text()
print(timestamp)
headline = child9.find("h1").get_text()
print("- " + headline.strip() + " -")
para = child9.find("p").get_text()
print(para.strip())
author = child9.find(class_="news-feed_item-meta")
author = author.find(class_="author").get_text()
print("Author: " + author.strip())

#---------------------------------
#for everything past item-info-wrap (main headline)
print(u"\U0001F3C0")
after_main = child5.find(class_="news-feed-item news-now news-feed-shortstop")
content = after_main.find(class_="now-content bloom-content")

timestamp = after_main.find(class_="now-feed_item-meta display-share")
print(timestamp.select_one("span[class*=timestamp]").text)

para = content.find("p").get_text()
print(para)
author = content.find("h1").get_text()
print("Author: " + author)