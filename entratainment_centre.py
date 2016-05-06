import media
import fresh_tomatoes

#movies I liked with relative data and links to trailer and poster image
toy_story = media.Video("Toy Story", "8.3 out of 10")

toy_story = media.Movie("A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc")

la_haine = media.Video("La Haine", "8.1 out of 10")

la_haine = media.Movie("One day in the banlieue of Paris",
                       "https://upload.wikimedia.org/wikipedia/en/3/30/Haine.jpg",
                       "https://youtu.be/yk77VrkxL88")

no_country_for_old_men = media.Video("No Country for Old Men", "8.1 out of 10")

no_country_for_old_men = media.Movie("While hunting in the desert, Llewelyn Moss comes across the aftermath of a drug deal gone awry.",
                                     "https://upload.wikimedia.org/wikipedia/en/8/8b/No_Country_for_Old_Men_poster.jpg",
                                     "https://youtu.be/38A__WT3-o0")

there_will_be_blood = media.Video("There Will Be Blood", "8.1 out of 10")

there_will_be_blood = media.Movie("In 1898, Daniel Plainview, a prospector in New Mexico, mines a potentially precious ore vein from a pit mine hole.",
                                  "https://upload.wikimedia.org/wikipedia/en/d/da/There_Will_Be_Blood_Poster.jpg",
                                  "https://youtu.be/FeSLPELpMeM")
fargo = media.Video("Fargo", "1h 38min", "8.2 out of 10")

fargo = media.Movie("A homespun murder story",
                    "https://upload.wikimedia.org/wikipedia/en/a/ac/Fargo.jpg",
                    "https://youtu.be/h2tY82z3xXU")

the_blues_brothers = media.Video("The Blues Brothers", "7.9 out of 10")

the_blues_brothers = media.Movie("Two men with a mission",
                                 "https://upload.wikimedia.org/wikipedia/en/f/f5/BluesBrothers.jpg",
                                 "https://youtu.be/A-xtJYIwfYo")

#list of movies for html document
movies = [toy_story, la_haine, no_country_for_old_men, there_will_be_blood, fargo, the_blues_brothers]
fresh_tomatoes.open_movies_page(movies)

#tv shows I liked with relative data and links to image
breaking_bed = media.Video("Breadking, Bad", "9.5 out ot 10")

breaking_bed = media.Tv_show("https://upload.wikimedia.org/wikipedia/en/6/61/Breaking_Bad_title_card.png",
                              "Five seasons"
                              "AMC")

house_of_cards = media.Video("House of Cards", "9.0 out of 10")

house_of_cards = media.Tv_show("https://upload.wikimedia.org/wikipedia/en/3/3f/House_of_Cards_title_card.png",
                               "Four seasons aired. Fifth season announced for 2017"
                               "Netflix")

#list of tv shows for html document
tv_shows = [breaking_bed, house_of_cards])
fresh_tomatoes.open_movies_page(tv_shows)

