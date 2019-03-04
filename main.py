from input import parse_input
from slide import *
from slideshow import *

a = 'a_example'
b = 'b_lovely_landscapes'
c = 'c_memorable_moments'
d = 'd_pet_pictures'
e = 'e_shiny_selfies'

data_sets = [a, b, c, d, e]

total_score=0
for data_set in data_sets:
    photo_set = parse_input(data_set)
    slides = create_dummy_slides(photo_set)
    # slides = random_diptychs_greedy(photo_set)
    # slides = naive_greedy(photo_set)
    submission = Submission(data_set, slides)
    score = submission.submission_score()
    total_score += score
    print('Slideshow for {} has score {}'.format(data_set, score))
    submission.write_submission()

print('Submission score {}'.format(total_score))
