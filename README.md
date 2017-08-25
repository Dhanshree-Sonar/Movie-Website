## Movie Trailer Website

This web site has list of movies. You can click any movie image and it will play trailer for that movie.
This site will help you to decide whether you want to watch that particular movie or not, by showing its trailer.

## Prerequisites

- Internet connection
- Python
  1. For instruction to install Python on Windows, click [here](https://www.python.org/downloads/windows/)
  2. For instruction to install Python on Mac, click [here](https://www.python.org/downloads/mac-osx/)
  
## File List
1. entertainment_center.py
2. media.py
3. fresh_tomatoes.py
4. README.md
  
## How to run

1. Place fresh_tomatoes.py, media.py and entertainment_center.py at one location
2. Open entertainment_center.py with Python
3. Run entertainment_center.py Module (Run -> Run Module) 
4. It will open the web site

## How to use website

1. Use vertical scrolling to go through all the movies.
2. Click on the image to open a trailer, it will open a pop-up a window, which will play the trailer
3. To close the trailer, click on cross mark (X) at upper right corner. It will take you to main page.
4. To see another trailer just follow the step 2 again.
5. If you are done surfing the movies, you can close the webpage.

## Improvements
 Currently this site stores 6 movies(Toy Story, Avatar, Inception, Interstellar, The Martian, Doctor Strange) data.
 If you want to add more movies to the site then you have insert below code to your entertainment_center.py
 
 1. Add below data
 ```
 <Movie Name> = media.Movie("<Movie Name>",
                     "<Movie Description>",
                     "<Movie poster image link>",
                     "<Movie trailer link from YouTube>")
 ```

2. Edit movies[] variable
  append your movie name to the existing array.
  
  `movies = [<previous array list>, <Movie Name>]`
