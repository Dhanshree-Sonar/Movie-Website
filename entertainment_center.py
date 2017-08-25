# This module helps to create a web page which all necessary styling
# 
import fresh_tomatoes

import media

# Creating class Movie() instances 
baby_driver = media.Movie("Baby Driver",
                        "After being coerced into working for a crime boss,"
                          "a young getaway driver finds himself taking part"
                          "in a heist doomed to fail.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8e/Baby_Driver_poster.jpg",
                        "https://www.youtube.com/watch?v=z2z857RSfhk")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

inception = media.Movie("Inception",
                        "Plant an idea in someone's mind.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

interstellar = media.Movie("Interstellar",
                           "Humanity trying to save themselves by understanding "
                           "the physics of space and time.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

the_martian = media.Movie("The Martian",
                          "An astronaut becomes stranded on Mars after his team "
                          "assume him dead, and must rely on his ingenuity to "
                          "find a way to signal to Earth that he is alive.",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

doctor_strange = media.Movie("Doctor Strange",
                             "While on a journey of physical and spiritual "
                             "healing, a brilliant neurosurgeon is drawn into "
                             "the world of the mystic arts.",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")

arrival = media.Movie("Arrival",
                      "When twelve mysterious spacecraft appear around the world,"
                      "linguistics professor Louise Banks is tasked with "
                      "interpreting the language of the apparent alien visitors.",
                      "https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

the_revenant = media.Movie("The Revenant",
                      "A frontiersman on a fur trading expedition in the 1820s "
                           "fights for survival after being mauled by a bear and "
                           "left for dead by members of his own hunting team.",
                      "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
                      "https://www.youtube.com/watch?v=LoebZZ8K5N0")




# Creating array of objects
movies = [avatar, inception, interstellar, doctor_strange, the_martian, arrival, the_revenant, baby_driver]

# Calling open_movies_page function of fresh_tomatoes module.
# It takes array of Movie() objects, then it generates and opens a webpage
# This webpage showes list of movies from the array 
fresh_tomatoes.open_movies_page(movies)


