#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
get_first_company.py

Usage: get_first_company "company name"

Search for the given name and print the best matching result.
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
    print(f'  {sys.argv[0]} "company name"')
    sys.exit(2)

name = sys.argv[1]


i = imdb.IMDb()

try:
    # Do the search, and get the results (a list of company objects).
    results = i.search_company(name)
except imdb.IMDbError as e:
    print("Probably you're not connected to Internet.  Complete error report:")
    print(e)
    sys.exit(3)

if not results:
    print(f'No matches for "{name}", sorry.')
    sys.exit(0)

# Print only the first result.
print(f'    Best match for "{name}"')

# This is a company instance.
company = results[0]

# So far the company object only contains basic information like the
# name; retrieve main information:
i.update(company)

print(company.summary())
