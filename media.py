import webbrowser

class Video():
	"""docstring for video: this class contains information about the title, duration of the movie and its votes"""

	def __init__(self, movie_title):
		"""Common data shared by both the Movie and TV_show class"""
		self.title = movie_title
#		self.votes = votes
		
class Movie(Video):
    """This class provide a way to store movie related information"""
    
    def __init__(self, movie_title, votes, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, movie_title)
        self.storyline_text = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
            webbrowser.open(fede.trailer_youtube_url)

class Tv_show(Video):
	"""This class provides a way to store tv shows related information"""
	def __init__(self, movie_title, tv_show_image, trailer_youtube):
		Video.__init__(self, movie_title)
		self.tv_show_image_url = tv_show_image
		self.trailer_youtube_url = trailer_youtube
#		self.nr_of_seasons = nr_of_seasons
#		self.tv_station = tv_station

#	def show_trailer(self):
#		webbrowser.open(self.trailer_youtube_url) 
