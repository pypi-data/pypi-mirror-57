import time
import statistics as stat
import autocomplete_me
####### Benchmark 1: slowComplete read_terms vs autoComplete read_terms #######
def benchmark_read_terms(path):
    # slowcomplete read terms
    read_slow_start = time.time()
    autocomplete_me.read_terms_slow(path)
    read_slow_end = time.time() - read_slow_start
    # autocomplete read terms
    read_auto_start = time.time()
    autocomplete_me.read_terms(path)
    read_auto_end = time.time() - read_auto_start
    return read_slow_end, read_auto_end

# read_terms comparison on "test_example.txt" file
test_read_terms_slow, test_read_terms_auto = benchmark_read_terms("Data/test_example.txt")
print("For reading test_example.txt file, it takes", test_read_terms_slow, "seconds for slowComplete, whereas it takes", test_read_terms_auto, "seconds for autoComplete.")
# read_terms comparison on "pokemon.txt" file
pokemon_read_terms_slow, pokemon_read_terms_auto = benchmark_read_terms("Data/pokemon.txt")
print("For reading pokemon.txt file, it takes", pokemon_read_terms_slow, "seconds for slowComplete, whereas it takes", pokemon_read_terms_auto, "seconds for autoComplete.")
# read_terms comparison on "movies.txt" file
movies_read_terms_slow, movies_read_terms_auto = benchmark_read_terms("Data/movies.txt")
print("For reading movies.txt file, it takes", movies_read_terms_slow, "seconds for slowComplete, whereas it takes", movies_read_terms_auto, "seconds for autoComplete.")
# read_terms comparison on "songs.txt" file
songs_read_terms_slow, songs_read_terms_auto = benchmark_read_terms("Data/songs.txt")
print("For reading songs.txt file, it takes", songs_read_terms_slow, "seconds for slowComplete, whereas it takes", songs_read_terms_auto, "seconds for autoComplete.")
###############################################################################

################## Benchmark 2: slowComplete vs autoComplete ##################
slow_test = autocomplete_me.read_terms_slow("Data/test_example.txt")
auto_test = autocomplete_me.read_terms("Data/test_example.txt")
slow_pokemon = autocomplete_me.read_terms_slow("Data/pokemon.txt")
auto_pokemon = autocomplete_me.read_terms("Data/pokemon.txt")
slow_movies = autocomplete_me.read_terms_slow("Data/movies.txt")
auto_movies = autocomplete_me.read_terms("Data/movies.txt")
slow_songs = autocomplete_me.read_terms_slow("Data/songs.txt")
auto_songs = autocomplete_me.read_terms("Data/songs.txt")

# slowComplete Timing
def benchmark_slowComplete(target_word, trie_input, suggest_num):
    slowComplete_record = []
    for s in range(0, 10):
        slowComplete_start = time.time()
        autocomplete_me.slowComplete(target_word, trie_input, suggest_num)
        slowComplete_end = time.time() - slowComplete_start
        slowComplete_record.append(slowComplete_end)
    return slowComplete_record

# autoComplete Timing
def benchmark_autoComplete(target_word, trie_input, suggest_num):
    autoComplete_record = []
    for a in range(0, 10):
        autoComplete_start = time.time()
        autocomplete_me.autoComplete(target_word, trie_input, suggest_num)
        autoComplete_end = time.time() - autoComplete_start
        autoComplete_record.append(autoComplete_end)
    return autoComplete_record

# slowComplete vs autoComplete speed comparison on "test_example.txt" file
test_slowComplete_l_time = benchmark_slowComplete("l", slow_test, 3)
test_autoComplete_l_time = benchmark_autoComplete("l", auto_test, 3)
test_slowComplete_time = benchmark_slowComplete("", slow_test, 3)
test_autoComplete_time = benchmark_autoComplete("", auto_test, 3)
print("Average slowComplete query time to recommend 3 words that start with 'l' in the test_example.txt file is", stat.mean(test_slowComplete_l_time), "seconds with standard deviation of", stat.stdev(test_slowComplete_l_time), "seconds.")
print("Average autoComplete query time to recommend 3 words that start with 'l' in the test_example.txt file is", stat.mean(test_autoComplete_l_time), "seconds with standard deviation of", stat.stdev(test_autoComplete_l_time), "seconds.")
print("Average slowComplete query time to recommend 3 words with highest weights in the test_example.txt file is", stat.mean(test_slowComplete_time), "seconds with standard deviation of", stat.stdev(test_slowComplete_time), "seconds.")
print("Average autoComplete query time to recommend 3 words with highest weights in the test_example.txt file is", stat.mean(test_autoComplete_time), "seconds with standard deviation of", stat.stdev(test_autoComplete_time), "seconds.")

# slowComplete vs autoComplete speed comparison on "pokemon.txt" file
pokemon_slowComplete_Po_time = benchmark_slowComplete("Po", slow_pokemon, 5)
pokemon_autoComplete_Po_time = benchmark_autoComplete("Po", auto_pokemon, 5)
pokemon_slowComplete_time = benchmark_slowComplete("", slow_pokemon, 5)
pokemon_autoComplete_time = benchmark_autoComplete("", auto_pokemon, 5)
print("Average slowComplete query time to recommend 5 words that start with 'Po' in the pokemon.txt file is", stat.mean(pokemon_slowComplete_Po_time), "seconds with standard deviation of", stat.stdev(pokemon_slowComplete_Po_time), "seconds.")
print("Average autoComplete query time to recommend 5 words that start with 'Po' in the pokemon.txt file is", stat.mean(pokemon_autoComplete_Po_time), "seconds with standard deviation of", stat.stdev(pokemon_autoComplete_Po_time), "seconds.")
print("Average slowComplete query time to recommend 5 words with highest weights in the pokemon.txt file is", stat.mean(pokemon_slowComplete_time), "seconds with standard deviation of", stat.stdev(pokemon_slowComplete_time), "seconds.")
print("Average autoComplete query time to recommend 5 words with highest weights in the pokemon.txt file is", stat.mean(pokemon_autoComplete_time), "seconds with standard deviation of", stat.stdev(pokemon_autoComplete_time), "seconds.")

# slowComplete vs autoComplete speed comparison on "movies.txt" file
movies_slowComplete_Ocean_time = benchmark_slowComplete("Ocean", slow_movies, 5)
movies_autoComplete_Ocean_time = benchmark_autoComplete("Ocean", auto_movies, 5)
movies_slowComplete_Ocean2_time = benchmark_slowComplete("Ocean's", slow_movies, 5)
movies_autoComplete_Ocean2_time = benchmark_autoComplete("Ocean's", auto_movies, 5)
print("Average slowComplete query time to recommend 5 words that start with 'Ocean' in the movies.txt file is", stat.mean(movies_slowComplete_Ocean_time), "seconds with standard deviation of", stat.stdev(movies_slowComplete_Ocean_time), "seconds.")
print("Average autoComplete query time to recommend 5 words that start with 'Ocean' in the movies.txt file is", stat.mean(movies_autoComplete_Ocean_time), "seconds with standard deviation of", stat.stdev(movies_autoComplete_Ocean_time), "seconds.")
print("Average slowComplete query time to recommend 5 words that start with 'Ocean's' in the movies.txt file is", stat.mean(movies_slowComplete_Ocean2_time), "seconds with standard deviation of", stat.stdev(movies_slowComplete_Ocean2_time), "seconds.")
print("Average autoComplete query time to recommend 5 words that start with 'Ocean's' in the movies.txt file is", stat.mean(movies_autoComplete_Ocean2_time), "seconds with standard deviation of", stat.stdev(movies_autoComplete_Ocean2_time), "seconds.")

# slowComplete vs autoComplete speed comparison on "songs.txt" file
songs_slowComplete_A_time = benchmark_slowComplete("A", slow_songs, 5)
songs_autoComplete_A_time = benchmark_autoComplete("A", auto_songs, 5)
songs_slowComplete_AllI_time = benchmark_slowComplete("All I", slow_songs, 5)
songs_autoComplete_AllI_time = benchmark_autoComplete("All I", auto_songs, 5)
songs_slowComplete_AllIWant_time = benchmark_slowComplete("All I Want", slow_songs, 5)
songs_autoComplete_AllIWant_time = benchmark_autoComplete("All I Want", auto_songs, 5)
songs_slowComplete_AllIWant_all_time = benchmark_slowComplete("All I Want", slow_songs, 182)
songs_autoComplete_AllIWant_all_time = benchmark_autoComplete("All I Want", auto_songs, 182)
print("Average slowComplete query time to recommend 5 words that start with 'A' in the songs.txt file is", stat.mean(songs_slowComplete_A_time), "seconds with standard deviation of", stat.stdev(songs_slowComplete_A_time), "seconds.")
print("Average autoComplete query time to recommend 5 words that start with 'A' in the songs.txt file is", stat.mean(songs_autoComplete_A_time), "seconds with standard deviation of", stat.stdev(songs_autoComplete_A_time), "seconds.")
print("Average slowComplete query time to recommend 5 words that start with 'All I' in the songs.txt file is", stat.mean(songs_slowComplete_AllI_time), "seconds with standard deviation of", stat.stdev(songs_slowComplete_AllI_time), "seconds.")
print("Average autoComplete query time to recommend 5 words that start with 'All I' in the songs.txt file is", stat.mean(songs_autoComplete_AllI_time), "seconds with standard deviation of", stat.stdev(songs_autoComplete_AllI_time), "seconds.")
print("Average slowComplete query time to recommend 5 words that start with 'All I Want' in the songs.txt file is", stat.mean(songs_slowComplete_AllIWant_time), "seconds with standard deviation of", stat.stdev(songs_slowComplete_AllIWant_time), "seconds.")
print("Average autoComplete query time to recommend 5 words that start with 'All I Want' in the songs.txt file is", stat.mean(songs_autoComplete_AllIWant_time), "seconds with standard deviation of", stat.stdev(songs_autoComplete_AllIWant_time), "seconds.")
print("Average slowComplete query time to recommend all words that start with 'All I Want' in the songs.txt file is", stat.mean(songs_slowComplete_AllIWant_all_time), "seconds with standard deviation of", stat.stdev(songs_slowComplete_AllIWant_all_time), "seconds.")
print("Average autoComplete query time to recommend all words that start with 'All I Want' in the songs.txt file is", stat.mean(songs_autoComplete_AllIWant_all_time), "seconds with standard deviation of", stat.stdev(songs_autoComplete_AllIWant_all_time), "seconds.")