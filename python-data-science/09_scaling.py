from sklearn import preprocessing

data = [[10., 2345., 0., 2.],
        [3., -3490., 0.1, 1.99],
        [13., 3903., -0.2, 2.11]]

print preprocessing.normalize(data)