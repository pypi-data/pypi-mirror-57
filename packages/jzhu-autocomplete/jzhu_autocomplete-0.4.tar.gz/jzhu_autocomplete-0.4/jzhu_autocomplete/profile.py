
import os
os.chdir('C:/Users/dell/Documents/s750/assignments-junyi-zhu/autocomplete-me')

import time
import statistics as stat
import autocomplete_me


import cProfile

# read_terms_slow vs. read_terms_auto
profile_movies_slow = cProfile.run("autocomplete_me.read_terms_slow('Data/movies.txt')")
profile_movies_auto = cProfile.run("autocomplete_me.read_terms_auto('Data/movies.txt')")

movies_slow = autocomplete_me.read_terms_slow("Data/movies.txt")
movies_auto = autocomplete_me.read_terms_auto("Data/movies.txt")

# slowcomplete vs. autocomplete
profile_slow = cProfile.run("autocomplete_me.slowcomplete(movies_slow, '', 10)")
profie_auto = cProfile.run("autocomplete_me.autocomplete(movies_auto, '', 10)")



