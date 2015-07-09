import webbrowser


class Movie():

    '''The class Movie is designed to create movie type objects'''

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    #   Establish the instance variables necessary for a Movie object.
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #   Define a function that plays a Movie objects
    #   associated movie trailer on YouTube via webbrowser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
