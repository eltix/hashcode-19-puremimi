import sys
from photo import *

def parse_orientation(o):
    if o == Orientation.HORIZONTAL.value:
        orientation = Orientation.HORIZONTAL
    elif o == Orientation.VERTICAL.value:
        orientation = Orientation.VERTICAL
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
    num_photos = int(lines[0])
    photo_set = PhotoSet(num_photos)
    for i in range(1, len(lines)):
        photo_id = i-1
        items = lines[i].split()
        orientation = parse_orientation(items[0])
        num_tags = int(items[1])
        tags = [items[j] for j in range(2, 2+num_tags)]
        photo_set.add_photo(Photo(photo_id, orientation, num_tags, tags))
    return photo_set
