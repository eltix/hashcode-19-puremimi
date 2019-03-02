import sys
from enum import Enum

class PhotoSet:

    def __init__(self, num_photos):
        self.num_photos = num_photos
        self.photos = []

    def add_photo(self, photo):
        self.photos.append(photo)

class Photo:

    def __init__(self, id, orientation, num_tags, tags):
        self.id = id
        self.orientation = orientation
        self.num_tags = num_tags
        self.tags = tags

class Orientation(Enum):
    HORIZONTAL = 'H'
    VERTICAL = 'V'

def parse_orientation(o):
    if o == Orientation.HORIZONTAL.value:
        orientation = Orientation.HORIZONTAL
    elif o == Orientation.VERTICAL.value:
        orientation = Orientation.HORIZONTAL
    else:
        print('Wrong orientation value {}'.format(o))
        sys.exit()
    return orientation

def parse_input(data_set_name):
    fname = './data/input/'+data_set_name+'.txt'
    # read the file content as a list of strings
    # also strip out end-line characters '\n'
    with open(fname) as file:
        lines = [line.rstrip('\n') for line in file]
    print(lines)
    num_photos = int(lines[0])
    input_set = PhotoSet(num_photos)
    for i in range(1, len(lines)):
        photo_id = i-1
        items = lines[i].split()
        orientation = parse_orientation(items[0])
        num_tags = int(items[1])
        tags = [items[j] for j in range(2, 2+num_tags)]
        print(photo_id, orientation, tags)
        input_set.add_photo(Photo(photo_id, orientation, num_tags, tags))
