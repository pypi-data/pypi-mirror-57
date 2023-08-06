
import autocomplete_me
import time
import statistics as stat
import numpy
# import os
# os.chdir("C:/Users/dell/Documents/s750/assignments-junyi-zhu/autocomplete-me")


###############################################################################
## 1 LOADING DATA
##   read_terms_slow() vs. read_terms_auto()
###############################################################################

def time_read_terms(path):
    """ 
    Records the time it takes to read files for slow- and auto-complete.
    """
    # slowcomplete
    start_slow = time.time()
    autocomplete_me.read_terms_slow(path)
    time_slow = time.time() - start_slow
    
    # autocomplete
    start_auto = time.time()
    autocomplete_me.read_terms_auto(path)
    time_auto = time.time() - start_auto
    
    return time_slow, time_auto

    # could also make lists, and then take the quantiles as the time may vary a bit
    # but songs.txt takes way too long; each run is 300-400s, so 50 iterations is 5 hours

    # return numpy.quantile(record_slow, 0.75), numpy.quantile(record_auto, 0.75)


# files ranked by size in ascending order
# time_read_terms("Data/pokemon.txt")
# time_read_terms("Data/fortune1000-randomly-ordered.txt")
# time_read_terms("Data/nasdaq.txt")
# time_read_terms("Data/wiktionary.txt")
# time_read_terms("Data/baby-names.txt")
# time_read_terms("Data/mandarin.txt")
# time_read_terms("Data/artists.txt")
# time_read_terms("Data/trademarks.txt")
# time_read_terms("Data/movies.txt")
# time_read_terms("Data/songs.txt")



###############################################################################
## 1 FINDING MATCHES
##   slowcomplete() vs. autocomplete()
###############################################################################

# VERSION 1

def time_bothcomplete(mylist, mytrie, prefix, k):
    """ 
    TLDR: Record the time it takes to find matches for slow- and auto-complete.
    
    With fixed inputs (file, prefix and k), this function runs slowcomplete 
    and autocomplete 1000 iterations, and record the time respectively for 
    each function into a list of length 1000.
    
    Then it calculates the 25th, 50th and 75th quantile of each list to compare
    the speed for the two functions.
    """
    # slowcomplete
    record_slow = []
    for ii in range(1, 1000):
        start = time.time()
        autocomplete_me.slowcomplete(mylist, prefix, k)
        time_slow = time.time() - start
        record_slow.append(time_slow)

    # autocomplete
    record_auto = []
    for ii in range(1, 1000):
        start = time.time()
        autocomplete_me.autocomplete(mytrie, prefix, k)
        time_auto = time.time() - start
        record_auto.append(time_auto)

    return numpy.quantile(record_slow, 0.25), \
           numpy.quantile(record_slow, 0.50), \
           numpy.quantile(record_slow, 0.75), \
           numpy.quantile(record_auto, 0.25), \
           numpy.quantile(record_auto, 0.50), \
           numpy.quantile(record_auto, 0.75)


# read files for testing
# files ranked by size in ascending order
pokemon_list = autocomplete_me.read_terms_slow("Data/pokemon.txt")
pokemon_trie = autocomplete_me.read_terms_auto("Data/pokemon.txt")

babies_list = autocomplete_me.read_terms_slow("Data/baby-names.txt")
babies_trie = autocomplete_me.read_terms_auto("Data/baby-names.txt")

movies_list = autocomplete_me.read_terms_slow("Data/movies.txt")
movies_trie = autocomplete_me.read_terms_auto("Data/movies.txt")

# songs_list = autocomplete_me.read_terms_slow("Data/songs.txt")
# songs_trie = autocomplete_me.read_terms_auto("Data/songs.txt")

# tests


# pokemon: 18 kb
time_bothcomplete(pokemon_list, pokemon_trie, "", 1)
time_bothcomplete(pokemon_list, pokemon_trie, "", 3)
time_bothcomplete(pokemon_list, pokemon_trie, "", 5)
time_bothcomplete(pokemon_list, pokemon_trie, "", 7)
time_bothcomplete(pokemon_list, pokemon_trie, "", 9)

time_bothcomplete(pokemon_list, pokemon_trie, "", 5)
time_bothcomplete(pokemon_list, pokemon_trie, "P", 5)
time_bothcomplete(pokemon_list, pokemon_trie, "Po", 5)
time_bothcomplete(pokemon_list, pokemon_trie, "Por", 5)
time_bothcomplete(pokemon_list, pokemon_trie, "Pory", 5)


# baby-names: 400 kb
time_bothcomplete(babies_list, babies_trie, "", 1)
time_bothcomplete(babies_list, babies_trie, "", 3)
time_bothcomplete(babies_list, babies_trie, "", 5)
time_bothcomplete(babies_list, babies_trie, "", 7)
time_bothcomplete(babies_list, babies_trie, "", 9)

time_bothcomplete(babies_list, babies_trie, "", 5)
time_bothcomplete(babies_list, babies_trie, "S", 5)
time_bothcomplete(babies_list, babies_trie, "Sa", 5)
time_bothcomplete(babies_list, babies_trie, "Sab", 5)
time_bothcomplete(babies_list, babies_trie, "Sabr", 5)


# movies: 10,261 kb
time_bothcomplete(movies_list, movies_trie, "", 1)
time_bothcomplete(movies_list, movies_trie, "", 3)
time_bothcomplete(movies_list, movies_trie, "", 5)
time_bothcomplete(movies_list, movies_trie, "", 7)
time_bothcomplete(movies_list, movies_trie, "", 9)

time_bothcomplete(movies_list, movies_trie, "", 5)
time_bothcomplete(movies_list, movies_trie, "O", 5)
time_bothcomplete(movies_list, movies_trie, "Oc", 5)
time_bothcomplete(movies_list, movies_trie, "Oce", 5)
time_bothcomplete(movies_list, movies_trie, "Ocea", 5)


# songs: 48,029 kb

# !!!!!!!!!! LAPTOP CRASHES FOR RUNNING THESE LINES !!!!!!!!!!

# time_bothcomplete(songs_list, songs_trie, "", 1)
# time_bothcomplete(songs_list, songs_trie, "", 3)
# time_bothcomplete(songs_list, songs_trie, "", 5)
# time_bothcomplete(songs_list, songs_trie, "", 7)
# time_bothcomplete(songs_list, songs_trie, "", 9)

# time_bothcomplete(songs_list, songs_trie, "", 5)
# time_bothcomplete(songs_list, songs_trie, "L", 5)
# time_bothcomplete(songs_list, songs_trie, "Lo", 5)
# time_bothcomplete(songs_list, songs_trie, "Lov", 5)
# time_bothcomplete(songs_list, songs_trie, "Love", 5)


# Nick:
# 
# run it 100 times, and then divide the total time by 100.
#     then collect 100 times (in total 10,000 times) for small files
#     use just means and standard deviations
# 
# for songs, do it once. 
# 
# we do not need graphs for benchmark, just txt files 
# (but do graphs over the weekend)


# VERSION 2 (based on Nick's suggestions)

def time_bothcomplete_new(mylist, mytrie, prefix, k):
    """ 
    TLDR: Record the time it takes to find matches for slow- and auto-complete.
    
    With fixed input (file, prefix and k), this function runs slowcomplete and 
    autocomplete 100 times in 100 iterations (in total 10,000 runs) and records 
    the time to run each function 100 times into a list of length 100.
    
    Then it calculates the mean and standard deviation of the two lists.
    """
    # slowcomplete
    record_slow = []

    start = time.time()
    for aa in range(1, 10):
        start = time.time()
        for bb in range(1, 1000):
            autocomplete_me.slowcomplete(mylist, prefix, k)
        time_slow = time.time() - start
        record_slow.append(time_slow)


    # autocomplete
    record_auto = []
    for cc in range(1, 10):
        start = time.time()
        for dd in range(1, 1000):
            autocomplete_me.autocomplete(mytrie, prefix, k)
        time_auto = time.time() - start
        record_auto.append(time_auto)

    return stat.mean(record_slow), stat.stdev(record_slow), \
           stat.mean(record_auto), stat.stdev(record_auto)

######################################################################
# pokemon: 18 kb
time_bothcomplete_new(pokemon_list, pokemon_trie, "", 1)
time_bothcomplete_new(pokemon_list, pokemon_trie, "", 3)
time_bothcomplete_new(pokemon_list, pokemon_trie, "", 5)
time_bothcomplete_new(pokemon_list, pokemon_trie, "", 7)
time_bothcomplete_new(pokemon_list, pokemon_trie, "", 9)

time_bothcomplete_new(pokemon_list, pokemon_trie, "", 5)
time_bothcomplete_new(pokemon_list, pokemon_trie, "P", 5)
time_bothcomplete_new(pokemon_list, pokemon_trie, "Po", 5)
time_bothcomplete_new(pokemon_list, pokemon_trie, "Por", 5)
time_bothcomplete_new(pokemon_list, pokemon_trie, "Pory", 5)


######################################################################
# baby-names: 400 kb
time_bothcomplete_new(babies_list, babies_trie, "", 1)
time_bothcomplete_new(babies_list, babies_trie, "", 3)
time_bothcomplete_new(babies_list, babies_trie, "", 5)
time_bothcomplete_new(babies_list, babies_trie, "", 7)
time_bothcomplete_new(babies_list, babies_trie, "", 9)

time_bothcomplete_new(babies_list, babies_trie, "", 5)
time_bothcomplete_new(babies_list, babies_trie, "S", 5)
time_bothcomplete_new(babies_list, babies_trie, "Sa", 5)
time_bothcomplete_new(babies_list, babies_trie, "Sab", 5)
time_bothcomplete_new(babies_list, babies_trie, "Sabr", 5)


######################################################################
# movies: 10,261 kb
time_bothcomplete_new(movies_list, movies_trie, "", 1)
time_bothcomplete_new(movies_list, movies_trie, "", 3)
time_bothcomplete_new(movies_list, movies_trie, "", 5)
time_bothcomplete_new(movies_list, movies_trie, "", 7)
time_bothcomplete_new(movies_list, movies_trie, "", 9)

time_bothcomplete_new(movies_list, movies_trie, "", 5)
time_bothcomplete_new(movies_list, movies_trie, "O", 5)
time_bothcomplete_new(movies_list, movies_trie, "Oc", 5)
time_bothcomplete_new(movies_list, movies_trie, "Oce", 5)
time_bothcomplete_new(movies_list, movies_trie, "Ocea", 5)


######################################################################
# songs: 48,029 kb

# !!!!!!!!!! LAPTOP CRASHES FOR RUNNING THESE LINES !!!!!!!!!!

# time_bothcomplete_new(songs_list, songs_trie, "", 1)
# time_bothcomplete_new(songs_list, songs_trie, "", 3)
# time_bothcomplete_new(songs_list, songs_trie, "", 5)
# time_bothcomplete_new(songs_list, songs_trie, "", 7)
# time_bothcomplete_new(songs_list, songs_trie, "", 9)

# time_bothcomplete_new(songs_list, songs_trie, "", 5)
# time_bothcomplete_new(songs_list, songs_trie, "L", 5)
# time_bothcomplete_new(songs_list, songs_trie, "Lo", 5)
# time_bothcomplete_new(songs_list, songs_trie, "Lov", 5)
# time_bothcomplete_new(songs_list, songs_trie, "Love", 5)

