from sklearn import decomposition
from sklearn import manifold
import umap


class DimensionalityReduction():

    def __init__(self, input_matrix):
        self.input_matrix = input_matrix

    def pca(self):
        pca = decomposition.PCA(n_components=2)
        pos = pca.fit(self.input_matrix).transform(self.input_matrix)
        return pos

    def tsne(self):
        tsne = manifold.TSNE(n_components=2)
        pos = tsne.fit_transform(self.input_matrix)
        return pos

    def u_map(self):
        reducer = umap.UMAP()
        pos = reducer.fit_transform(self.input_matrix)
        return pos
