#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
get_first_movie.py

Usage: get_first_movie "movie title"

Search for the given title and print the best matching result.
"""


import sys

# Import the Cinemagoer package.
try:
    import imdb
except ImportError:
    print('You need to install the Cinemagoer package!')
    sys.exit(1)


if len(sys.argv) != 2:
    print('Only one argument is required:')
    print(f'  {sys.argv[0]} "movie title"')
    sys.exit(2)

title = sys.argv[1]


i = imdb.IMDb()

try:
    # Do the search, and get the results (a list of Movie objects).
    results = i.search_movie(title)
except imdb.IMDbError as e:
    print("Probably you're not connected to Internet.  Complete error report:")
    print(e)
    sys.exit(3)

if not results:
    print(f'No matches for "{title}", sorry.')
    sys.exit(0)

# Print only the first result.
print(f'    Best match for "{title}"')

# This is a Movie instance.
movie = results[0]

# So far the Movie object only contains basic information like the
# title and the year; retrieve main information:
i.update(movie)

print(movie.summary())
