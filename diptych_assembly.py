import numpy as np
from utils import *
from slide import Diptych

def maximum_union(photos):
    verticals = extract_verticals(photos)
    tag_mat = tag_matrix(verticals)
    n = len(verticals)
    tag_union = np.zeros((n, n), dtype=int)
    for i in range(n):
        tag_union[i, :] = np.sum(np.minimum(np.ones(tag_mat.shape), tag_mat + tag_mat[i, :]), axis=1)
    tag_union = tag_union - np.diag(np.diag(tag_union))
    available_ids = range(n)
    i0, j0 = np.unravel_index(np.argmax(tag_union), (n, n))
    vertical_pairs = [(i0, j0)]
    available_ids.remove(i0); available_ids.remove(j0)
    for j in range(n/2-1):
        # print('j {}'.format(j))
        k = len(available_ids)
        loc_mat = tag_union[np.ix_(available_ids, available_ids)]
        # print(loc_mat)
        iloc, jloc = np.unravel_index(np.argmax(loc_mat), (k, k))
        # print('max union {}'.format(np.amax(loc_mat )))
        i0, j0 = available_ids[iloc], available_ids[jloc]
        # print('i0, j0 {},{}'.format(i0, j0))
        available_ids.remove(i0); available_ids.remove(j0)
        vertical_pairs.append((i0, j0))
    return [Diptych(verticals[p1], verticals[p2]) for (p1, p2) in vertical_pairs]

def big_with_small(photos):
    verticals = extract_verticals(photos)
    xs = sorted(verticals, key = lambda x: len(set(x.tags)))
    n = len(xs)
    vertical_pairs = [(xs[i], xs[-i-1]) for i in range(n//2)]
    return [Diptych(p1, p2) for (p1, p2) in vertical_pairs]
