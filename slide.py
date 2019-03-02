import sys
from enum import Enum

class Slide:

    def __init__(self, num_photos):
        pass

    def serialize(self):
        pass

class Monoptych(Slide):
    """ A slide with only one photo """

    def __init__(self, photo_1):
        self.photo_1 = photo_1

    def tags(self):
        return self.photo_1.tags

    def serialize(self):
        return str(self.photo_1.id)


class Diptych(Slide):
    """ A slide with two photos """

    def __init__(self, photo_1, photo_2):
        self.photo_1 = photo_1
        self.photo_2 = photo_2

    def tags(self):
        return self.photo_1.tags + self.photo_2.tags

    def serialize(self):
        return str(self.photo_1.id) + ' ' + str(self.photo_2.id)

class Submission:

    def __init__(self, data_set_name, slides):
        self.data_set_name = data_set_name
        self.slides  = slides
        self.num_slides = len(slides)

    def serialize(self):
        """ Convert Submission object to a list of strings """
        content = [str(self.num_slides)]
        for s in self.slides:
            content += [s.serialize()]
        return content

    def write_submission(self):
        filename = './data/output/submission_' + self.data_set_name + '.txt'
        with open(filename, 'w') as f:
            for item in self.serialize():
                f.write("%s\n" % item)
        print('Successfully wrote submission file {}'.format(filename))

    def submission_score(self):
        return compute_score(self.slides)

def compute_score(slides):
    slide_pairs = zip(slides, slides[1:])
    score = sum(score_slide_pair(pair) for pair in slide_pairs)
    return score

def score_slide_pair(slide_pair):
    left_slide, right_slide = slide_pair
    left_tags = set(left_slide.tags())
    right_tags = set(right_slide.tags())
    intersec = len(left_tags.intersection(right_tags))
    left_diff = len(left_tags.difference(right_tags))
    right_diff = len(right_tags.difference(left_tags))
    #print(intersec, left_diff, right_diff)
    score = min(intersec, left_diff, right_diff)
    return score
