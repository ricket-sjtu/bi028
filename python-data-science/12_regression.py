import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

def f(x):
    return x + np.random.random() * 3.

X = np.arange(0, 5, 0.5)
X = X.reshape((len(X), 1))
y = map(f, X)

clf = linear_model.LinearRegression()
clf.fit(X, y)

new_X = np.arange(0.2, 5.2, 0.3)
new_X = new_X.reshape((len(new_X), 1))
new_y = clf.predict(new_X)

plt.scatter(X, y, color='g', label='Training data')

plt.plot(new_X, new_y, '.-', label='Predicted')



plt.legend()
plt.show()