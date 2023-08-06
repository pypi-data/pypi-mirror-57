import time
import statistics as stat
import autocomplete_me
import profile

# Profiling slowComplete's read_terms vs autoComplete's read_terms
profile_slow_songs = profile.run("autocomplete_me.read_terms_slow('Data/songs.txt')")
profile_auto_songs = profile.run("autocomplete_me.read_terms('Data/songs.txt')")

# Profiling slowComplete vs autoComplete
slow_songs = autocomplete_me.read_terms_slow("Data/songs.txt")
auto_songs = autocomplete_me.read_terms("Data/songs.txt")
profile_slowComplete = profile.run("autocomplete_me.slowComplete('A', slow_songs, 100)")
profie_autoComplete = profile.run("autocomplete_me.autoComplete('A', auto_songs, 100)")