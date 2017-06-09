from sklearn import feature_extraction

data = [{"weight": 60., "sex": 'female', "student": True},
        {"weight": 80.1, "sex": 'male', "student": False},
        {"weight": 65.3, "sex": 'male', "student": True},
        {"weight": 58.5, "sex": 'female', "student": False}]

vectorizer = feature_extraction.DictVectorizer(sparse=False)

vectors = vectorizer.fit_transform(data)
print vectors
print vectorizer.get_feature_names()