"""Solution for Distance Matrix"""
import numpy as np


def pairwise_euclidean_distance(points: np.ndarray) -> np.ndarray:
    # Using broadcasting: (n,1,d) - (1,n,d) = (n,n,d), then sum and sqrt
    diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    return np.sqrt(np.sum(diff ** 2, axis=2))
