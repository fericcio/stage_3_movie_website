import webbrowser

class Video():
	"""docstring for video: this class contains information about the title, duration of the movie and its votes"""

	def __init__(self, movie_title, votes):
		self.title = movie_title
		self.votes = votes
		
class Movie(Video):
    """This class provide a way to store movie related information"""
    
    def __init__(fede, movie_storyline, poster_image, trailer_youtube):
            Video.__init__(self, movie_title,votes)
            fede.storyline = movie_storyline
            fede.poster_image_url = poster_image
            fede.trailer_youtube_url = trailer_youtube

    def show_trailer(fede):
            webbrowser.open(fede.trailer_youtube_url)

class TV_show(Video):
	"""This class provides a way to store tv shows related information"""
	def __init___(self, tv_show_image, nr_of_seasons, tv_station):
		Video.__init__(self, movie_title, votes):
		self.tv_show_image = tv_show_image
		self.nr_of_seasons = nr_of_seasons
		self.tv_station = tv_station

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url) 

