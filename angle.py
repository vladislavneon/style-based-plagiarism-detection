import numpy as np


def unit_vector(vector):
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def dist_between(v1, v2):
    vec1 = np.array(v1)
    vec2 = np.array(v2)
    return np.linalg.norm(vec1 - vec2)


def main():
    v1 = [1, 2, 0]
    v2 = [2, -1, 0]
    print(angle_between(v1, v2))
    print(np.pi / 2)
