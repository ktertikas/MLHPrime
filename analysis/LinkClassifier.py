import requests
from bs4 import BeautifulSoup

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
from sklearn.naive_bayes import MultinomialNB

from sklearn.svm import SVC, LinearSVC
from sklearn.preprocessing import LabelEncoder

class LinkClassifier():

    category_links = {"sports": "http://feeds.bbci.co.uk/sport/football/rss.xml?edition=int",
                    "politics":"http://feeds.bbci.co.uk/news/politics/rss.xml",
                     "technology":"https://www.technologyreview.com/topnews.rss",
                     "finance":"http://feeds.bbci.co.uk/news/business/rss.xml",
                     "education":"http://feeds.bbci.co.uk/news/education/rss.xml?edition=uk",
                     "entertainment":"http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml?edition=uk"}

    word_pattern = re.compile("^[^\d\W]+$")
    stop_words = set(stopwords.words('english'))
    word_length = 2
    ps = SnowballStemmer("english")

    def __init__(self):
        print 'Training model...'
        self.train_model()
        print 'Model trained'

    def preprocessing(self,document):
        tokens = WordPunctTokenizer().tokenize(document)
        tokens = list(map(lambda x: x.lower(), tokens))
        tokens = [i for i in tokens if re.match(self.word_pattern, i) and i not in self.stop_words and len(i)>self.word_length]
        tokens = [self.ps.stem(i) for i in tokens]
        tokens_text = ' '.join(tokens)
        return tokens_text

    # Create featurevector
    def create_featurevector(self,document):
        tfidf_vectorizer = TfidfVectorizer(max_df=0.8, min_df=0.1)
        tfidf_matrix = tfidf_vectorizer.fit_transform(document)
        return tfidf_matrix, tfidf_vectorizer

    def train_model(self):
        documents = []
        documents_titles = []
        self.documents_labels = []
        for category, cat_link in self.category_links.items():
            result = requests.get(cat_link)
            soup = BeautifulSoup(result.text, "lxml-xml")
            links_list = soup.findAll("item")
            for item in links_list:
                link = item.link.text
                soup2 = BeautifulSoup(requests.get(link).content, "lxml")
                ignore_list = ["script", "style"]
                for ignore in soup2(ignore_list):
                    ignore.extract()
                processed_text = self.preprocessing(soup2.body.get_text())
                documents.append(processed_text)
                documents_titles.append(soup2.title.text)
                self.documents_labels.append(category)

        self.feature_vector, self.vectorizer = self.create_featurevector(documents)

        self.train_model_lsvm()


    def train_model_bayes(self):
        # Naive Bayes Multinomial Classifier
        self.clf = MultinomialNB().fit(self.feature_vector, self.documents_labels)

    def train_model_lsvm(self):
        # We convert Date, Trap, Species to numerical (both train and test datasets)
        self.lbl = LabelEncoder()
        # Species
        self.lbl.fit(self.documents_labels)
        label_data = self.lbl.transform(self.documents_labels)

        self.clf_lsvm = LinearSVC()
        self.clf_lsvm.fit(self.feature_vector, label_data)

    def link_to_doc(self,link):
        soup = BeautifulSoup(requests.get(link).content, "lxml")
        ignore_list = ["script", "style"]
        for ignore in soup(ignore_list):
            ignore.extract()
        return soup.body.get_text()

    def classify_doc(self,document):
        processed_text = self.preprocessing(document)
        new_feature_vector = self.vectorizer.transform([processed_text])
        predicted = self.clf.predict(new_feature_vector)
        return predicted

    def classify_link(self,link):
        doc = self.link_to_doc(link)
        return self.classify_doc(doc)[0]

    def classify_link_lsvm(self,link):
        doc = self.link_to_doc(link)
        return self.lbl.classes_[self.classify_doc_lsvm(doc)][0]

    def classify_doc_lsvm(self,document):
        processed_text = self.preprocessing(document)
        new_feature_vector = self.vectorizer.transform([processed_text])
        predicted = self.clf_lsvm.predict(new_feature_vector)
        return predicted
