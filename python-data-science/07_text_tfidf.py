from sklearn import feature_extraction

corpus = ['Cats really are great.',
          'I like cats but I still prefer dogs.',
          'Dogs are the best.',
          'I like trains',
          ]

tfidf = feature_extraction.text.TfidfVectorizer()

print tfidf.fit_transform(corpus)
print tfidf.get_feature_names()