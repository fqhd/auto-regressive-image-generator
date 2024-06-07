import numpy as np
import random
import math

def dist(p1, p2):
    dim = len(p1)
    distance_squared = 0
    for i in range(dim):
        distance_squared += math.pow(p2[i] - p1[i], 2.0)
    return math.sqrt(distance_squared)
    
def find_closest(clusters, point):
    d = float('inf')
    best_index = 0
    for i, c in enumerate(clusters):
        distance = dist(c[0], point)
        if distance < d:
            best_index = i
            d = distance
    return best_index

def partition(clusters, points):
    for i, p in enumerate(points):
        closest_cluster_idx = find_closest(clusters, p)
        clusters[closest_cluster_idx][1].append(i)

def mean(cluster, points):
    sum = np.zeros(points[0].shape)
    for p_idx in cluster[1]:
        sum += points[p_idx]
    if len(cluster[1]) == 0:
        return sum
    return sum / len(cluster[1])


def recompute_centroids(clusters, points, learning_rate):
    convergence = 0
    for c in clusters:
        centroid = mean(c, points)
        convergence += np.linalg.norm(centroid - c[0])
        direction = (centroid - c[0]) * learning_rate
        new_centroid = c[0] + direction
        np.copyto(c[0], new_centroid)
        c[1].clear()
    return convergence / len(clusters)
    
def init_clusters(points, k):
    clusters = []
    cluster_indices = np.linspace(0, len(points)-1, len(points)).astype('int32')
    random.shuffle(cluster_indices)
    for i in range(k):
        clusters.append((points[cluster_indices[i]].copy(), []))
    return clusters
    
def kmeans_step(clusters, points, learning_rate):
    partition(clusters, points)
    convergence = recompute_centroids(clusters, points, learning_rate)
    return convergence
    
def kmeans(points, k, learning_rate, iters):
    clusters = init_clusters(points, k)
    for _ in range(iters):
        convergence = kmeans_step(clusters, points, learning_rate)
        print(convergence)
    partition(clusters, points)
    return clusters