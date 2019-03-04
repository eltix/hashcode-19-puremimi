from slide import *
from photo import *
from utils import *
from diptych_assembly import *
import numpy as np

def create_dummy_slides(pset):
    """ Dummy slideshow where we first create Monoptychs with
    all horizontal photos and then Diptychs with all vertical
    photos in the same order as they appear in the input file
    """
    monoptychs, diptychs = split_tychs_in_order(pset)
    slides = monoptychs + diptychs
    return slides

def random_diptychs_greedy(pset):
    """ Dummy slideshow where we first create Monoptychs with
    all horizontal photos and then Diptychs with all vertical
    photos in the same order as they appear in the input file
    """
    monoptychs, diptychs = split_tychs_in_order(pset)
    all_slides = monoptychs + diptychs
    n = len(all_slides)
    slide_dict = dict((s.id, s) for s in all_slides)
    available_slides = slide_dict.keys()
    id0, slide0 = slide_dict.popitem()
    slides = [slide0]
    available_slides.remove(id0)
    for i in range(n-1):
        print(i)
        scores = np.array([score_slide_pair((slides[-1], slide_dict[id])) for id in available_slides])
        imax = np.argmax(scores)
        slides.append(slide_dict[available_slides[imax]])
        available_slides.remove(available_slides[imax])
    return slides

def split_tychs_in_order(pset):
    photos = pset.photos
    horizontals = [p for p in photos if p.orientation == Orientation.HORIZONTAL]
    verticals = [p for p in photos if p.orientation == Orientation.VERTICAL]
    monoptychs = [Monoptych(p) for p in horizontals]
    diptychs = [Diptych(*d) for d in zip(*[iter(verticals)]*2)]
    return (monoptychs, diptychs)

def maximize_score_greedy(slides):
    n = len(slides)
    tag_mat = tag_matrix(slides)
    intersec = np.dot(tag_mat, tag_mat.T)
    diag = np.diag(intersec)
    diff_right = diag - intersec
    diff_left = diff_right.T
    score_mat = np.minimum(intersec, np.minimum(diff_right, diff_left))
    available_slides = range(n)
    i0, j0 = np.unravel_index(np.argmax(score_mat), (n, n))
    score = np.amax(score_mat)
    print('max score {}'.format(score))
    slideshow = [slides[i0], slides[j0]]
    print('add to slideshow: {}'.format(i0, j0))
    available_slides.remove(i0)
    for j in range(n-2):
        jloc = available_slides.index(j0)
        loc_mat = score_mat[np.ix_(available_slides, available_slides)]
        s = np.amax(loc_mat[:, jloc])
        if (s <= 0):
            # print('only zero-score transitions. stop the slideshow')
            break
        score += s
        print(' score {}'.format(score))
        iloc = np.argmax(loc_mat[:, jloc])
        i0 = available_slides[iloc]
        print('add to slideshow: {}'.format(i0))
        slideshow.append(slides[i0])
        available_slides.remove(j0)
        j0 = i0
    return slideshow


def naive_greedy(pset):
    # diptychs = maximum_union(pset.photos)
    diptychs = big_with_small(pset.photos)
    hors = extract_horizontals(pset.photos)
    monoptychs = [Monoptych(h) for h in hors]
    slides = maximize_score_greedy(monoptychs+diptychs)
    return slides

# def all_photos_scores(photos):
#     tags_ = [p.tags for p in photos]
#     tags = [item for sublist in tags_ for item in sublist]
#     all_tags = list(set(tags))
#     p = len(all_tags)
#     n = len(photos)
#     A = np.zeros((n, p), dtype=int)
#
#
#
#     intersec = np.dot(A, A.T)
#     diag = np.diag(intersec)
#     diff_right = diag - intersec
#     diff_left = diff_right.T
#     S = np.minimum(intersec, np.minimum(diff_right, diff_left))
#     return S
#
# def diptychs_indices(photos):
#     indices = [i for (i, p) in enumerate(photos) if p.orientation == Orientation.VERTICAL]
#     return indices
#
# def score_matrix(pset):
#     S = all_photos_scores(pset.photos)
#     D = diptychs_scores(pset.photos)
#
#     # Best pair of photos
#     i0, j0 = np.unravel_index(np.argmax(S), (n, n))
#     print(photos[i0].tags)
#     print(photos[j0].tags)
#     return None
