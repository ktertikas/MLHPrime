from bs4 import BeautifulSoup
import requests

def get_metadata(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text)
    title_text = soup.title.text
    if not soup.title:
        title_text = soup.h1.text

    meta = soup.findAll(attrs={"name":"description"})
    meta_text=""
    for name in meta:
        meta_text = meta_text + name["content"]

    soup1 = BeautifulSoup(r.text)

    sources=soup1.findAll('img',{"src":True})
    image_link = sources[0]["src"]
    return (title_text, meta_text, image_link)
