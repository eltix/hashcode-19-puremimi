from enum import Enum

class PhotoSet:

    def __init__(self, num_photos):
        self.num_photos = num_photos
        self.photos = []

    def add_photo(self, photo):
        self.photos.append(photo)

    def tags(self):
        tags_ = [p.tags for p in self.photos]
        tags = [item for sublist in tags_ for item in sublist]
        return tags

class Photo:

    def __init__(self, id, orientation, num_tags, tags):
        self.id = id
        self.orientation = orientation
        self.num_tags = num_tags
        self.tags = tags

class Orientation(Enum):
    HORIZONTAL = 'H'
    VERTICAL = 'V'
