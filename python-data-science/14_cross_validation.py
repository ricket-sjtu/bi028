from sklearn import svm, cross_validation, datasets

iris = datasets.load_iris()
X, y = iris.data, iris.target

model = svm.SVC()
print cross_validation.cross_val_score(model, X, y, scoring='precision')
print cross_validation.cross_val_score(model, X, y, scoring='mean_squared_error')