import fresh_tomatoes
import media

#   An empty movie array is initiated to hold the list of movies.
#   This deviates from prescribed code, so that by creating a new
#   instance, the author doesn't forget to add the entity to the list

movies = []

#   Add all new movies here using media.Movie.
#   Each enumerated object is a seperate instance.

starwars7 = media.Movie(
    "Star Wars: Episode VII",
    "The Force Awakens",
    "https://upload.wikimedia.org/wikipedia/en/2/28/Starwarsviitheforceawakens.jpg",
    "https://www.youtube.com/watch?v=ngElkyQ6Rhs")
movies.append(starwars7)

jurassic_world = media.Movie(
    "Jurassic World",
    "The Park Reopens",
    "https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg",
    "https://www.youtube.com/watch?v=RFinNxS5KN4")
movies.append(jurassic_world)

fantastic_four_2015 = media.Movie(
    "Fantastic Four",
    "Good things come in fours",
    "https://upload.wikimedia.org/wikipedia/en/f/f4/Fantastic_Four_2015_poster.jpg",
    "https://www.youtube.com/watch?v=wuV4BCYv-YY")
movies.append(fantastic_four_2015)

terminator_genisys = media.Movie(
    "Terminator: Genisys",
    "He's Back",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Terminator_Genisys.JPG",
    "https://www.youtube.com/watch?v=62E4FJTwSuc")
movies.append(terminator_genisys)

mi_rogue_nation = media.Movie(
    "Mission: Impossible - Rogue Nation",
    "It's time to go Rogue",
    "https://upload.wikimedia.org/wikipedia/en/7/74/Mission_Impossible_–_Rogue_Nation_poster.jpg",
    "https://www.youtube.com/watch?v=gOW_azQbOjw")
movies.append(mi_rogue_nation)

mocking_jay_2 = media.Movie(
    "The Hunger Games: Mocking Jay Part II",
    "No more games",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/Mockingjay_Part_2_Poster.jpg",
    "https://www.youtube.com/watch?v=8e2xY0pMz70")
movies.append(mocking_jay_2)

toy_story = media.Movie(
    "Toy Story",
    "A story about a boy and his toys that come to life.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=vwyZH85NQC4")
movies.append(toy_story)

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
movies.append(avatar)

school_of_rock = media.Movie(
    "School of Rock",
    "I really want to be in a band",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=5afGGGsxvEA")
movies.append(school_of_rock)

ratatouille = media.Movie(
    "Ratatouille",
    "Chefs are awesome",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=ALUmKa_mpik")
movies.append(ratatouille)

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Thanks Woody",
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
    "https://www.youtube.com/watch?v=BYRWfS2s2v4")
movies.append(midnight_in_paris)

hunger_games = media.Movie(
    "The Hunger Games",
    "Wanna play a game?",
    "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
    "https://www.youtube.com/watch?v=4S9a5V9ODuY")
movies.append(hunger_games)
                           
# fresh_tomatoes does all the HTML rendering and front-end formatting
fresh_tomatoes.open_movies_page(movies)
