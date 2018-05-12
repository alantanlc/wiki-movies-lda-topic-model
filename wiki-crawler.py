import pycorpora

# Extract list of popular movies
movies = pycorpora.film_tv.popular_movies['popular-movies']

# Split entries into title and year
movies = [m[:-1].split(' (') for m in movies]

print('Program completed!')