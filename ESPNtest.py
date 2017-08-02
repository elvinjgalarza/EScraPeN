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

#------------------------------------------------------------------------------------------
#First news-feed-item... ESPN seems to have different types of items
#Specification: story-package, video-standalone, shorstop
#They are all distinguished by an <article> tag, and are classified with "news-feed-item" followed by specification
#Seems as though some articles uses ESPN.com news services... this makes it a bit harder because then no specific author is put

articles = child6.find_all("article")
i=0
print("I have found %d New York Knicks related articles:\n" % (len(articles)))
tag=articles[i]
if(tag["news-feed-item news-feed-story-package"] = True):
    content = articles[i]
    content = content.find(class_="text-container no-headlines")
    content = content.find(class_="item-info-wrap")

    timestamp = content.find(class_="news-feed_item-meta")
    timestamp = timestamp.find(class_="timestamp").get_text()
    print(u"\U0001F3C0" + " " + timestamp)
    headline = content.find("h1").get_text()
    print("- " + headline.strip() + " -")
    para = content.find("p").get_text()
    print(para.strip())
    #author = content.find(class_="news-feed_item-meta")
    #author = author.find(class_="author").get_text()
    #print("Author: " + author.strip())
    i=i+1

