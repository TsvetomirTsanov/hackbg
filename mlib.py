class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length


    def __eq__(self, other):
        return self.title = other.title and self.artist = other.title /
               and self.album = other.album and self.length = other.length

    def __hash__(self):
        return hash(str(self.name))

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def __length__(self, seconds = False):
        if seconds = False:
            return str(length)
        else:
            return ord(self.length[0])*60 + ord(self.length[1:]))
