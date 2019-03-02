from slide import *
from photo import *


def create_dummy_slides(pset):
    """ Dummy slideshow where we first create Monoptychs with
    all horizontal photos and then Diptychs with all vertical
    photos in the same order as they appear in the input file
    """
    photos = pset.photos
    horizontals = [p for p in photos if p.orientation == Orientation.HORIZONTAL]
    verticals = [p for p in photos if p.orientation == Orientation.VERTICAL]
    slides = [Monoptych(p) for p in horizontals]
    diptychs = zip(*[iter(verticals)]*2)
    slides += [Diptych(*d) for d in diptychs]
    return slides
