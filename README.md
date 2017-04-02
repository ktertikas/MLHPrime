# TagYourLinks

## The Idea

Our main idea was to create a web service for the user, so that he is able to store his preferred links, in a fast and well-structured way. In particular, once the user pastes a new link, our algorithm classifies the link to one of the 6 predefined categories (Sports, Technology, Education, Finance, Entertainment, Politics).

## The Approach

Our algorithm has several steps:
- Preprocessing: Web Scraping, Tokenization, Stemming, Stopwords Removal, Filtering of small words and words with very small and very high term frequencies.
- Feature Extraction: Bag of Words implementation. Metric Used: TF-IDF (Term Frequency, Inverse Document Frequency).
- Classification. We trained our model with the sparse feature vectors of approximately 220 different links that were preprocessed as mentioned above, each of these links having a specific label. When our model was trained, we used it to predict in which one of the 6 different predefined categories the newly inserted link belongs to, and assign it accordingly. We tried two algorithms for our model, the first one being the Naive Bayes Classifier, and the next one being a multiclass Linear Support Vector Machines implementation. From our testing we concluded that the Support Vector Machine approach is more suitable for our case.

## Technical

For the Web server part and the data analysis we used python. In particular, we used Beautiful Soup for the web scraping, the NLTK library for the preprocessing of the text obtained from every webpage, and the machine learning library scikit-learn for the feature extraction and the two implemented classification algorithms. For the web application, we used a Linux Virtual Machine from Amazon Web Services (EC2). We created a MongoDB database, and our application is based on the Tornado web framework. For the front end implementation of our app, we used javascript, and libraries such as jquery and d3, and for the design of the webpage we used Bootstrap. 


## Future Improvements 

Bigger Training dataset, more categories, try some different text mining approaches (Matrix Factorisation, Latent Semantic Analysis). For the preprocessing of our text we could try a different implementation, using ngrams or lemmatisation.
