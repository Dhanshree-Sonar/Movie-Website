# Importing module which allow use to open web browser
import webbrowser

# Creating class to store all movie related parameters in one object
class Movie():
    # Constructor for the class 
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # Initializing the variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Function to show movie trailer 
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        

        
        
    
