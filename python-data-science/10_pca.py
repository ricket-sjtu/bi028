from sklearn import decomposition

data = [[0.3, 0.2, 0.4,  0.32],
        [0.3, 0.5, 1.0, 0.19],
        [0.3, -0.4, -0.8, 0.22]]

pca = decomposition.PCA()
print pca.fit_transform(data)
print pca.explained_variance_ratio_