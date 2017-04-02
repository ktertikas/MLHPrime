
# coding: utf-8

# In[47]:

from bs4 import BeautifulSoup
import requests

link = "http://www.economist.com/news/business/21719841-scott-gottlieb-close-pharma-industry-knows-its-tactics-nominee-run-americas?fsrc=rss"
r = requests.get(link)
soup = BeautifulSoup(r.text)
title_text = soup.title.text
if not soup.title:
    title_text = soup.h1.text
print title_text

# meta_text = soup.find_all('meta')
# for link in meta_text:
 
meta = soup.findAll(attrs={"name":"description"})
meta_text=""
for name in meta:
    meta_text = meta_text + name["content"]
    
print meta_text

soup1 = BeautifulSoup(r.text)

sources=soup1.findAll('img',{"src":True})
image_link = sources[0]["src"]
print image_link


# In[ ]:



