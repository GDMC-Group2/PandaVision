import seaborn as sns
import numpy as np
import itertools
import matplotlib.pyplot as plt


def neighboring_centers_detect(c1, c2, neighbor_dis=50):
    neighbor_dis = neighbor_dis ** 2
    if (c2[0] - c1[0])**2 + (c2[1] - c1[1])**2 <= neighbor_dis:
            return True
    return False

def detect(clusters, centers):
    count_centers = len(centers)
    for i in range(count_centers):
        if len(centers[i]) == 0:
            continue
        for j in range(count_centers):
            if len(centers[j]) == 0 or i == j:
                continue
            if neighboring_centers_detect(centers[i], centers[j]):
                clusters[i].extend(clusters[j])
                clusters[j] = []
                centers[i] = [(centers[i][0] + centers[j][0]) / 2, (centers[i][1] + centers[j][1]) / 2]
                centers[j] = []

    new_clusters = []
    new_centers = []
    for i in range(count_centers):
        if len(clusters[i]) != 0:
            new_clusters.append(clusters[i])
            new_centers.append(centers[i])

    return new_clusters, new_centers