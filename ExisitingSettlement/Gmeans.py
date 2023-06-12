import seaborn as sns
from pyclustering.cluster import gmeans
import numpy as np
import itertools
import matplotlib.pyplot as plt
from . import neighboring_centers_detector as ncd
maxnum = -1



def neighboring_detect(c1, c2):
    for one in c2:
        x = one[0]
        z = one[1]
        if np.any(np.all(c1 == [x+1, z], axis=1)) or np.any(np.all(c1 == [x-1, z], axis=1)) or np.any(
                np.all(c1 == [x, z+1], axis=1)) or np.any(np.all(c1 == [x, z-1], axis=1)):
            return True
    return False


def fit(X, pltshow=1):
    if len(X) == 0:
        print('no clusters')
        return [], [], [], []
    gmeans_instance = gmeans.gmeans(data=X, k_max=maxnum).process()

    clusters = gmeans_instance.get_clusters()
    centers = gmeans_instance.get_centers()
    count_clusters = len(clusters)
    print('old_centers', count_clusters)
    for i in range(count_clusters-1):
        if len(clusters[i]) == 0:
            continue
        for j in range(i+1, count_clusters):
            if neighboring_detect(X[clusters[i]], X[clusters[j]]):
                clusters[i].extend(clusters[j])
                clusters[j] = []
                centers[i] = [(centers[i][0] + centers[j][0])/2, (centers[i][1] + centers[j][1])/2]
                centers[j] = []

    new_clusters = []
    new_clusters_2 = []
    new_centers = []
    for i in range(count_clusters):
        if len(clusters[i]) != 0:
            new_clusters.append(clusters[i])
            new_clusters_2.append(X[clusters[i]])
            new_centers.append(centers[i])
    print('new_centers', len(new_centers))

    new_clusters_ncd, new_centers_ncd = ncd.detect(new_clusters.copy(), new_centers.copy())
    print('new_centers ncd.detect: ', len(new_centers_ncd))

    new_clusters_ncd_2 = []
    for i in range(len(new_clusters_ncd)):
        new_clusters_ncd_2.append(X[new_clusters_ncd[i]])

    if pltshow:
        labels_size = len(
            list(itertools.chain.from_iterable(new_clusters))
        )
        labels = np.zeros((1, labels_size))
        for n, n_th_cluster in np.ndenumerate(np.array(new_clusters)):
            for img_num in n_th_cluster:
                labels[0][img_num] = n[0]
        labels = labels.ravel()

        ax = sns.scatterplot(
            X[:, 0], X[:, 1], hue=labels, legend="full"
        )
        new_centers = np.array(new_centers)
        plt.scatter(new_centers[:, 0], new_centers[:, 1], s=200, marker='.', c='red')
        plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
        plt.setp(ax.get_legend().get_texts(), fontsize='8')
        plt.show()
    return new_clusters_2, new_centers, new_clusters_ncd_2, new_centers_ncd
