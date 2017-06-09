from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()

X = iris.data[:, :2]
y = iris.target

# Training the model
clf = svm.SVC(kernel='rbf')
clf.fit(X, y)

# Doing predictions
new_data = [[4.85, 3.1], [5.61, 3.02]]
print clf.predict(new_data)