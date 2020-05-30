import numpy as np


clusters = {0: [[6, 3], [6, 5], [7, 2], [7, 4]],
            1: [[2, 5], [3, 6], [4, 4], [4, 5]],
            2 : [[1, 1], [1, 2], [2, 1], [3, 2], [2, 3]]}

points = np.array([[1, 1], [1, 2], [2, 1], [3, 2], [6, 3], [6, 5], [2, 5],
                   [7, 2], [7, 4], [2, 3], [3, 6], [4, 4], [4, 5]])


def nearest_points(centers, points):
    clusters = {}

    ### YOUR CODE HERE
    point_to_center = {}
    k = len(centers)
    n = len(points)

    # find each point's nearest center
    for i in range(n):
        min_dis = (centers[0][0] - points[i][0]) ** 2 + (centers[0][1] - points[i][1]) ** 2
        min_idx = 0
        for j in range(1, k):
            cur_dis = (centers[j][0] - points[i][0]) ** 2 + (centers[j][1] - points[i][1]) ** 2
            if cur_dis < min_dis:
                min_dis = cur_dis
                min_idx = j
        point_to_center[i] = min_idx

        # init result clusters
    for i in range(k):
        clusters[i] = []

    # re-range point_to_center to result clusters
    for key, value in point_to_center.items():
        clusters[value].append([points[key][0], points[key][1]])

    return clusters

def compute_new_centers(clusters, points):

    new_clusters = {}

    ### YOUR CODE HERE
    k = len(clusters)
    print(k)
    centers = []
    for i in range(k):
        points_in_cluster = clusters.get(i)
        print(points_in_cluster)
        x = 0
        y = 0
        for j in range(len(points_in_cluster)):
            x += points_in_cluster[j][0]
            y += points_in_cluster[j][1]
        centers.append([x / len(points_in_cluster), y / len(points_in_cluster)])

    new_clusters = nearest_points(centers, points)

    return new_clusters

clusters = compute_new_centers(clusters, points)
print(clusters)

print(clusters.get(0))