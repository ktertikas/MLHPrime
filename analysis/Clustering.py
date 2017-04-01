
# coding: utf-8

# # RSS Links 

# In[36]:

import requests
from bs4 import BeautifulSoup

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import os
import nltk
import re
import numpy as np
import pandas as pd
from nltk import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.cluster.vq import kmeans, kmeans2


# In[37]:

# Cleaning, tokenization, stemming of text:
word_pattern = re.compile("^[^\d\W]+$")
stop_words = set(stopwords.words('english'))
word_length = 2
ps = SnowballStemmer("english")
def preprocessing(document):
    tokens = WordPunctTokenizer().tokenize(document)
    tokens = list(map(lambda x: x.lower(), tokens))
    tokens = [i for i in tokens if re.match(word_pattern, i) and i not in stop_words and len(i)>word_length]
    tokens = [ps.stem(i) for i in tokens]
    tokens_text = ' '.join(tokens)
    return tokens_text
# new_folder = folder_stemmed + i + ".txt"


# In[38]:

# Create featurevector 
def create_featurevector(document):
    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, min_df=0.1)
    tfidf_matrix = tfidf_vectorizer.fit_transform(document)
    return tfidf_matrix, tfidf_vectorizer


# In[54]:

category_links = {"sports": "http://feeds.bbci.co.uk/sport/football/rss.xml?edition=int", 
                "politics":"http://feeds.bbci.co.uk/news/politics/rss.xml",
                 "technology":"https://www.technologyreview.com/topnews.rss",
                 "finance":"http://feeds.bbci.co.uk/news/business/rss.xml",
                 "education":"http://feeds.bbci.co.uk/news/education/rss.xml?edition=uk",
                 "entertainment":"http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml?edition=uk"}


# In[55]:

print category_links.items()


# In[56]:

documents = []
documents_titles = []
documents_labels = []
for category, cat_link in category_links.items():
#     documents[category] = []
#     documents_titles[category] = []
    print category, cat_link
    result = requests.get(cat_link)
    soup = BeautifulSoup(result.text, "lxml-xml")
    links_list = soup.findAll("item")
#     print links_list
    for item in links_list:
        link = item.link.text
        soup2 = BeautifulSoup(requests.get(link).content, "lxml")
#         documents_titles[category].append(soup2.title.text)
        ignore_list = ["script", "style"]
        for ignore in soup2(ignore_list):
            ignore.extract()
        processed_text = preprocessing(soup2.body.get_text())
#         documents[category].append(processed_text)   
        documents.append(processed_text)
        documents_titles.append(soup2.title.text)
        documents_labels.append(category)
        if category=="finance":
            print repr(link)

# print(feature_vector.shape)
# soup2.body.get_text()


# In[ ]:




# In[57]:

# len(documents_titles["sports"])
# print len(documents_labels)
feature_vector, vectorizer = create_featurevector(documents)
feature_vector.shape


# In[53]:

# one = requests.get("http://rss.cnn.com/~r/rss/money_news_economy/~3/1JYcV4hy51Y/index.html").text
# one = link_to_doc("http://rss.cnn.com/~r/rss/money_news_economy/~3/1JYcV4hy51Y/index.html")
soup = BeautifulSoup(requests.get("http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml?edition=uk").text, "lxml-xml")
# print soup.prettify()
links_list = soup.findAll("item")
# print links_list
for item in links_list:
    print item.link.text


# In[58]:

# Naive Bayes Multinomial Classifier
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(feature_vector, documents_labels)


# In[59]:

def link_to_doc(link):
    soup = BeautifulSoup(requests.get(link).content, "lxml")
    ignore_list = ["script", "style"]
    for ignore in soup(ignore_list):
        ignore.extract()
    return soup.body.get_text()

def classify_doc(document):
    processed_text = preprocessing(document)
    new_feature_vector = vectorizer.transform([processed_text])
    predicted = clf.predict(new_feature_vector)
    return predicted


# In[65]:

prediction_link = "http://www.nltk.org"
doc = link_to_doc(prediction_link)
# print(doc)
classify_doc(doc)


# In[132]:

# Kmeans Clustering 
cluster_num = 2
test = kmeans2(feature_vector.toarray(), cluster_num)
test[1].shape
# results_kmeans = list(zip([documents_titles[x] for x in documents],test[1]))
# results_kmeans.sort(key = lambda x: x[1])
# print(test[1])
# plot_cluster_labels(test[1])


# In[ ]:



