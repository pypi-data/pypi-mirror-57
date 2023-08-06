import pytest
import autocomplete_me
############################## SLOWCOMPLETE ###################################
# Testing read_terms_slow
def test_read_terms_slow():
    assert autocomplete_me.read_terms_slow("Data/test_example.txt") == [(222, 'life'),(222,'love'),(222,'lab'),(500,'help'),(11,'me'),(489,'survive')]

# Testing slowComplete
slow_test = autocomplete_me.read_terms_slow("Data/test_example.txt")
slow_pokemon = autocomplete_me.read_terms_slow("Data/pokemon.txt")
slow_movies = autocomplete_me.read_terms_slow("Data/movies.txt")
slow_mandarin = autocomplete_me.read_terms_slow("Data/mandarin.txt")
def test_slowComplete():
    assert autocomplete_me.slowComplete("h", slow_test, 3) == [(500,'help')]
    assert autocomplete_me.slowComplete("l", slow_test, 5) == [(222, 'love'), (222, 'life'), (222, 'lab')]
    assert autocomplete_me.slowComplete("Po", slow_pokemon, 1) == [(1846470, 'Politoed')]
    assert autocomplete_me.slowComplete("", slow_pokemon, 3) == [(2194440, 'Scizor'), (1968270, 'Ferrothorn'), (1846470, 'Politoed')]
    assert autocomplete_me.slowComplete("Ocean's Eleven", slow_movies, 3) == [(183405771, "Ocean's Eleven (2001)"), (12317000, "Ocean's Eleven (1960)")]
    assert autocomplete_me.slowComplete("Ocean", slow_movies, 5) == [(183405771, "Ocean's Eleven (2001)"), (125531634, "Ocean's Twelve (2004)"), (117154724, "Ocean's Thirteen (2007)"), (12317000, "Ocean's Eleven (1960)"), (47732, 'Ocean of Pearls (2008)')]
    assert autocomplete_me.slowComplete("是", slow_mandarin, 3) == [(8291, '是的'), (2158, '是不是'), (899, '是否')]
    assert autocomplete_me.slowComplete("안녕하세요", slow_mandarin, 5) == None

###############################################################################

############################## AUTOCOMPLETE ###################################

# Testing read_terms for autoComplete
def test_read_terms():
    assert type(autocomplete_me.read_terms("Data/test_example.txt").children) == dict
    assert type(autocomplete_me.read_terms("Data/pokemon.txt").children) == dict
    assert type(autocomplete_me.read_terms("Data/movies.txt").children) == dict
    assert type(autocomplete_me.read_terms("Data/mandarin.txt").children) == dict

# Testing Trie class' searchTrie function
auto_test = autocomplete_me.read_terms("Data/test_example.txt")
auto_pokemon = autocomplete_me.read_terms("Data/pokemon.txt")
auto_movies = autocomplete_me.read_terms("Data/movies.txt")
auto_mandarin = autocomplete_me.read_terms("Data/mandarin.txt")
def test_Trie_searchTrie():
    assert autocomplete_me.Trie(auto_test).searchTrie("l").full_word == None
    assert autocomplete_me.Trie(auto_test).searchTrie("l").end_weight == -1000
    assert autocomplete_me.Trie(auto_pokemon).searchTrie("Pikachu").full_word == "Pikachu"
    assert autocomplete_me.Trie(auto_pokemon).searchTrie("Pikachu").end_weight != -1000
    assert autocomplete_me.Trie(auto_movies).searchTrie("Ocean").full_word == None
    assert autocomplete_me.Trie(auto_movies).searchTrie("Ocean").end_weight < autocomplete_me.Trie(auto_movies).searchTrie("Ocean").max_weight
    assert autocomplete_me.Trie(auto_mandarin).searchTrie("是").full_word == "是"
    assert autocomplete_me.Trie(auto_mandarin).searchTrie("是").end_weight == autocomplete_me.Trie(auto_mandarin).searchTrie("是").max_weight

# Testing autoComplete
def test_autoComplete():
    assert autocomplete_me.slowComplete("h", slow_test, 3) == autocomplete_me.autoComplete("h", auto_test, 3)
    assert autocomplete_me.slowComplete("l", slow_test, 5) == autocomplete_me.autoComplete("l", auto_test, 5)
    assert autocomplete_me.slowComplete("Po", slow_pokemon, 1) == autocomplete_me.autoComplete("Po", auto_pokemon, 1)
    assert autocomplete_me.slowComplete("", slow_pokemon, 3) == autocomplete_me.autoComplete("", auto_pokemon, 3)
    assert autocomplete_me.slowComplete("Ocean's Eleven", slow_movies, 3) == autocomplete_me.autoComplete("Ocean's Eleven", auto_movies, 3)
    assert autocomplete_me.slowComplete("Ocean", slow_movies, 5) == autocomplete_me.autoComplete("Ocean", auto_movies, 5)
    assert autocomplete_me.slowComplete("是", slow_mandarin, 3) == autocomplete_me.autoComplete("是", auto_mandarin, 3)
    assert autocomplete_me.slowComplete("안녕하세요", slow_mandarin, 5) == autocomplete_me.autoComplete("안녕하세요", auto_mandarin, 5)

###############################################################################

############ ADD TERM, DELETE TERM, CHANGE WEIGHT, INSERT OR UPDATE ############

# Testing add_term
def test_add_term():
    auto_test_add = autocomplete_me.add_term("life", 1000, auto_test)
    auto_pokemon_add = autocomplete_me.add_term("Pikachus", 10000000, auto_pokemon)
    auto_movies_add = autocomplete_me.add_term("Parasite (2019)", 3000, auto_movies)
    auto_mandarin_add = autocomplete_me.add_term("안녕하세요", 1500, auto_mandarin)
    assert autocomplete_me.autoComplete("l", auto_test_add, 3) == [(1000, 'life'), (222, 'love'), (222, 'lab')]
    assert autocomplete_me.autoComplete("Pikachu", auto_pokemon_add, 1) == [(10000000, 'Pikachus')]
    assert autocomplete_me.autoComplete("Parasite", auto_movies_add, 5) == [(7000000, 'Parasite (1982)'), (3000, 'Parasite (2019)'), (0, 'Parasite (2010)'), (0, 'Parasite (2009)'), (0, 'Parasite (2006)')]
    assert autocomplete_me.autoComplete("안녕", auto_mandarin_add, 1) == [(1500, '안녕하세요')]

# Testing delete_term
def test_delete_term():
    autocomplete_me.delete_term("life", auto_test)
    autocomplete_me.delete_term("Porygon2", auto_pokemon)
    autocomplete_me.delete_term("Parasite", auto_movies) # case when the term does not exist in the Trie
    autocomplete_me.delete_term("是不是", auto_mandarin)
    assert autocomplete_me.autoComplete("l", auto_test, 5) == [(222, 'love'), (222, 'lab')]
    assert autocomplete_me.autoComplete("Porygo", auto_pokemon, 2) == [(83878, 'Porygon-Z'), (533, "Porygon")]
    assert autocomplete_me.Trie(auto_pokemon).searchTrie("Pory").max_weight == autocomplete_me.Trie(auto_pokemon).searchTrie("Porygon-Z").max_weight
    assert autocomplete_me.autoComplete("Parasite", auto_movies, 5) == [(7000000, 'Parasite (1982)'), (3000, 'Parasite (2019)'), (0, 'Parasite (2010)'), (0, 'Parasite (2009)'), (0, 'Parasite (2006)')]
    assert autocomplete_me.autoComplete("是不", auto_mandarin, 2) == []

# Testing change_weight
def test_change_weight():
    def weight_function1(weight):
        return weight + 1
    def weight_function2(weight):
        return weight + 100
    def weight_function3(weight):
        return weight * 0
    def weight_function4(weight):
        return weight * weight
    autocomplete_me.change_weight(auto_test, "love", weight_function1)
    autocomplete_me.change_weight(auto_pokemon, "Pikachu", weight_function2)
    autocomplete_me.change_weight(auto_movies, 'Parasite (1982)', weight_function3)
    autocomplete_me.change_weight(auto_mandarin, "是的", weight_function4)
    assert autocomplete_me.autoComplete("l", auto_test, 2) == [(223, 'love'), (222, 'lab')]
    assert autocomplete_me.autoComplete("Pikach", auto_pokemon, 2) == [(10000000, 'Pikachus'), (32601, 'Pikachu')]
    assert autocomplete_me.autoComplete("Parasite (1982", auto_movies, 1) == [(0, 'Parasite (1982)')]
    assert autocomplete_me.autoComplete("是", auto_mandarin, 1) == [(68740681, '是的')]

# Testing insert_or_update
def test_insert_or_update():
    autocomplete_me.insert_or_update("lab", 1000, auto_test)
    autocomplete_me.insert_or_update("Pikachuss", 1000, auto_pokemon)
    autocomplete_me.insert_or_update("Parasite (2019)", 1000000, auto_movies)
    autocomplete_me.insert_or_update("是是是", 10000000000, auto_mandarin)
    assert autocomplete_me.autoComplete("l", auto_test, 2) == [(223, 'love'), (223, 'lab')]
    assert autocomplete_me.autoComplete("Pikach", auto_pokemon, 3) == [(10000000, 'Pikachus'), (32601, 'Pikachu'), (1000, "Pikachuss")]
    assert autocomplete_me.autoComplete("Parasite (201", auto_movies, 2)  == [(3001, "Parasite (2019)"), (0, "Parasite (2010)")]
    assert autocomplete_me.autoComplete("是是", auto_mandarin, 1) == [(10000000000, "是是是")]

###############################################################################

######################### PRUNE TRIE, RESCALE WEIGHTS #########################

# Redefining the Trie
auto_test2 = autocomplete_me.read_terms("Data/test_example.txt")
auto_pokemon2 = autocomplete_me.read_terms("Data/pokemon.txt")
auto_movies2 = autocomplete_me.read_terms("Data/movies.txt")
auto_mandarin2 = autocomplete_me.read_terms("Data/mandarin.txt")

# Rescale update input function
def rescale_function1(weight):
    return weight + 100
def rescale_function2(weight):
    return weight * 0
def rescale_function3(weight):
    return weight // 1000000
def rescale_function4(weight):
    return weight - 500

# Testing prune trie
def test_prune_trie_rescale_weights():
    # pruning the trie
    autocomplete_me.prune_trie(auto_test2, 223)
    autocomplete_me.prune_trie(auto_pokemon2, 1556150)
    autocomplete_me.prune_trie(auto_movies2, 1)
    autocomplete_me.prune_trie(auto_mandarin2, 292828)
    # rescaling the weights after pruning
    autocomplete_me.rescale_weights(auto_test2, rescale_function1)
    autocomplete_me.rescale_weights(auto_pokemon2, rescale_function2)
    autocomplete_me.rescale_weights(auto_movies2, rescale_function3)
    autocomplete_me.rescale_weights(auto_mandarin2, rescale_function4)
    # Testing after pruning & rescaling the weights
    assert autocomplete_me.autoComplete("", auto_test2, 6) == [(600, "help"), (589, "survive")]
    assert autocomplete_me.autoComplete("", auto_pokemon2, 100) == [(0, 'Scizor'), (0, 'Politoed'), (0, 'Latios'), (0, 'Ferrothorn'), (0, 'Dragonite')]
    assert autocomplete_me.autoComplete("Parasite", auto_movies2, 5) == [(7, 'Parasite (1982)')]
    assert autocomplete_me.autoComplete("", auto_mandarin2, 100) == [(292328, '我')]