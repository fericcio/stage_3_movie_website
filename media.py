import webbrowser

class Video():
	"""docstring for video: this class contains information about the title, duration of the movie and its votes"""

	def __init__(self, movie_title, youtube_trailer):
		"""Common data shared by both the Movie and TV_show class"""
		self.title = movie_title
		self.youtube_trailer_url = youtube_trailer
#		self.votes = votes
	
	def show_trailer(self):
		webbrowser.open(self.youtube_trailer_url)
		
class Movie(Video):
    """This class provide a way to store movie related information"""
    def __init__(self, movie_title, youtube_trailer, movie_storyline, poster_image):
        Video.__init__(self, movie_title, youtube_trailer)
        self.storyline_text = movie_storyline
        self.poster_image_url = poster_image


class Tv_show(Video):
	"""This class provides a way to store tv shows related information"""
	def __init__(self, movie_title, youtube_trailer, tv_show_image):
		Video.__init__(self, movie_title, youtube_trailer)
		self.tv_show_image_url = tv_show_image
#		self.nr_of_seasons = nr_of_seasons
#		self.tv_station = tv_station
