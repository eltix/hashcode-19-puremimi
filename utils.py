import numpy as np
from photo import Orientation

def tag_matrix(photos):
    tags_ = [p.tags for p in photos]
    tags = [item for sublist in tags_ for item in sublist]
    all_tags = list(set(tags))
    p = len(all_tags)
    n = len(photos)
    A = np.zeros((n, p), dtype=int)
    for i in range(n):
        A[i, :] = [t in photos[i].tags for t in all_tags]
    return A

def extract_verticals(photos):
    verticals = [p for p in photos if p.orientation == Orientation.VERTICAL]
    return verticals

def extract_horizontals(photos):
    horizontals = [p for p in photos if p.orientation == Orientation.HORIZONTAL]
    return horizontals
