class Movie():
    """Movie __init__ takes in a Title, Poster Image URL,
    a youtube trailer and assigns attributes for each of them"""
    def __init__(self, movieTitle, posterImage, trailerYoutube):
        self.title = movieTitle
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailerYoutube
