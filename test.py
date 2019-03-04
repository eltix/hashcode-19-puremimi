from input import parse_input
from slide import *
from slideshow import *
import numpy as np
from utils import *

a = 'a_example'
b = 'b_lovely_landscapes'
c = 'c_memorable_moments'
d = 'd_pet_pictures'
e = 'e_shiny_selfies'


#data_sets = [a, b, c, d, e]

#for data_set in data_sets:
#    pset = parse_input(data_set)
#    tags = pset.tags()
#    tagset = set(tags)
#    print(len(tagset))



data_set = d
pset = parse_input(data_set)

diptychs = big_with_small(pset.photos)
hors = extract_horizontals(pset.photos)
monoptychs = [Monoptych(h) for h in hors]

slides = maximize_score_greedy(monoptychs+diptychs)
submission = Submission(data_set, slides)
score = submission.submission_score()
print(score)
