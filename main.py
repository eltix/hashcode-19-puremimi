from input import parse_input
from slide import *
from slideshow import *


a = 'a_example'
b = 'b_lovely_landscapes'
c = 'c_memorable_moments'
d = 'd_pet_pictures'
e = 'e_shiny_selfies'

data_sets = [a, b, c, d, e]


for data_set in data_sets:
    photo_set = parse_input(data_set)
    slides = create_dummy_slides(photo_set)
    # dummy submission
    # slides = [Monoptych(0), Diptych(1, 2), Monoptych(3)]
    submission = Submission(data_set, slides)
    print('Submission score {}'.format(submission.submission_score()))
    submission.write_submission()
