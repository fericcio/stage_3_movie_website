import media
import fresh_tomatoes

#movies I liked with relative data and links to trailer and poster image

toy_story = media.Movie("Toy Story", 
                        "https://youtu.be/KYz2wyBy3kc",
#                        "8.3 out of 10",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg")

la_haine = media.Movie("La Haine",
                       "https://youtu.be/yk77VrkxL88",
#                       "8.1 out of 10",
                       "One day in the banlieue of Paris",
                       "https://upload.wikimedia.org/wikipedia/en/3/30/Haine.jpg")

no_country_for_old_men = media.Movie("No Country for Old Men",
                                     "https://youtu.be/38A__WT3-o0",
#                                     "8.1 out of 10",
                                     "While hunting in the desert, Llewelyn Moss comes across the aftermath of a drug deal gone awry.",
                                     "https://upload.wikimedia.org/wikipedia/en/8/8b/No_Country_for_Old_Men_poster.jpg")

there_will_be_blood = media.Movie("There Will Be Blood",
                                  "https://youtu.be/FeSLPELpMeM",
#                                  "8.1 out of 10",
                                  "In 1898, Daniel Plainview, a prospector in New Mexico, mines a potentially precious ore vein from a pit mine hole.",
                                  "https://upload.wikimedia.org/wikipedia/en/d/da/There_Will_Be_Blood_Poster.jpg")

fargo = media.Movie("Fargo",
                    "https://youtu.be/h2tY82z3xXU",
#                    "8.2 out of 10",
                    "A homespun murder story",
                    "https://upload.wikimedia.org/wikipedia/en/a/ac/Fargo.jpg")

the_blues_brothers = media.Movie("The Blues Brothers",
                                 "https://youtu.be/A-xtJYIwfYo",
#                                 "7.9 out of 10",
                                 "Two men with a mission",
                                 "https://upload.wikimedia.org/wikipedia/en/f/f5/BluesBrothers.jpg")

#list of movies for html document

movies = [toy_story, la_haine, no_country_for_old_men, there_will_be_blood, fargo, the_blues_brothers]

#tv shows I liked with relative data and links to image

breaking_bed = media.Tv_show("Breadking Bad",
                             "https://youtu.be/8h-iAZBtNrs",
#                             "9.5 out ot 10",
                             "https://upload.wikimedia.org/wikipedia/en/6/61/Breaking_Bad_title_card.png")
#                             "Five seasons",
#                             "AMC")

house_of_cards = media.Tv_show("House of Cards",
                               "https://youtu.be/ULwUzF1q5w4",
#                               "9.0 out of 10",
                               "https://upload.wikimedia.org/wikipedia/en/3/3f/House_of_Cards_title_card.png")
#                               "Four seasons aired. Fifth season announced for 2017",
#                               "Netflix")

#list of tv shows for html document
tv_shows = [breaking_bed, house_of_cards]

fresh_tomatoes.open_movies_page(movies, tv_shows)
