# Topic Modeling
* ***Unsupervised learning*** technique to analyze large volumes of text data by **clustering documents into groups** based on similar characteristics. 
* It is used to group large volumes of unlabeled text data.  
* It is one of the most sought after research areas in NLP. 

*Example*: Newspaper articles that belong to the same category or have the same topic can be assigned to the same cluster or group.  

*Consideration*: It is extremely difficult to evaluate the performance of topic modeling since there are no right answers. It depends upon the user to find similar characteristics between the documents of one cluster and assign it an appropriate label or topic.  

# Python Libraries
* pandas
* os
* sklearn

`pip install -r requirements.txt`

## Approaches

## Latent Dirichlet Allocation (LDA)
* Assumptions
    * Documents that have similar words usually have the same topic.
    * Documents that have groups of words frequently occurring together usually have the same topic.
* Mathematically
    * **Documents** are probability distributions over **latent topics**.
    * **Topics** are probability distributions over **words**.

## Non-negative Matrix Factorization (NMF)
* It performs ***clustering*** as well as ***dimensionality reduction***. 
* It can be used in combination with ***TF-IDF*** scheme to perform topic modeling. 

### Create vocabulary and Vectorize document 
* Create vocabulary of all the words in the data using *CountVectorizer* for **LDA** and *TfidfVectorizer* for **NMF**. (2627 terms)
    * Include those words that appear in less than 80% of the document. (max_df)
    * Include those words that appear in atleast 2 documents. (min_df)
    * Remove English stopwords
* Create document term matrix with the vocabulary vector. (60x2627)
    * Each of the 60 news document is represented as a vector of 2627 terms

### Create topic model using LDA and NMF
* Use LDA and NMF on the vectorized documents.
* Divide into 5 topics. (n_components)
* Calculate probability distribution of each word in vocabulary.

### Get Topics and top 10 words
Get each topic with its top 10 highest probability words
* Use *components_* for fetching the topics.
* Use *argsort()* to sort the words based on probability values and fetch their indices.
* Use *get_feature_names()* to retrieve the words from vectorizer (vocabulary) using the indices.

### Predict Topic for news text
* Use *argmax(axis=1)* to get the topic with max probability
