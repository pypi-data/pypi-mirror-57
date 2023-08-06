import heapq
import collections
# SLOWCOMPLETE
def read_terms_slow(path):

    """ Reads txt file and parse by individual word and corresponding weight

    Parameters
    ----------
    path = the file path of the given txt file

    Results
    ----------
    word_list = list of tuples that contains a word and its associated weight

    """

    word_list = []
    with open(path, "r") as f:
        lines = f.readlines()
        for ii in range(1, len(lines)):
            if lines[ii].strip() == "":
                continue
            ind_weight, ind_word = lines[ii].split('\t')
            ind_weight = int(ind_weight)
            ind_word = ind_word.strip()
            word_list.append((ind_weight, ind_word))
    return word_list

def slowComplete(target_word, list_words, suggest_num):

    """ Search through the word list and return n number of recommended words
    that start with the target word

    Parameter
    ----------
    target_word = the prefix of the word that needs to be matched from the list
    list_words = a list (words and weights) that will be searched
    suggest_num = the number of suggested words that needs to be returned

    Results
    ----------
    recommend_list = a list of top n recommended words and their weights,
    which starts with the target word

    """

    # Pre-conditions to run the slowcomplete
    assert suggest_num > 0 and isinstance(suggest_num, int), "the number of suggested words should be a positive integer"
    assert isinstance(target_word, str), "the target word should be in a string"
    # slowcomplete function
    recommend_list = []
    for ii in range(0, len(list_words)):
        if list_words[ii][1].startswith(target_word) and target_word != list_words[ii][1]:
            recommend_list.append((list_words[ii][0], list_words[ii][1]))
    recommend_list = sorted(recommend_list, key = lambda x: (x[0], x[1]), reverse = True)
    recommend_list = recommend_list[0:suggest_num]
    # message when the list of words do not have enough suggestions
    if len(recommend_list) == 0:
        print("Cannot recommend any words")
        return
    elif len(recommend_list) < suggest_num:
        print("Failed to suggest all", suggest_num, "words, only suggesting", len(recommend_list), "words")
    # return the suggested words
    return recommend_list

# AUTOCOMPLETE - Inserting all attributes of a word into children nodes
class Node:
    def __init__(self, end_weight = -1000, max_weight = -1000, full_word = None):

        """ Initializing the node with default property

        Parameters
        ----------
        end_weight = a word's associated weight,
        updated only after done with inserting attributes of a word into node
        (default = -1000)

        max_weight = a maximum weight of one particular node,
        updated only when the children node's weight is greater than max_weight
        (default = -1000)

        full_word = initialize it as None for each newly created node,
        updated to originally inputted word once done with building nodes

        children = a dictionary, storing information about each word's letter

        """

        # Initialize children, end_weight, max_weight, and word weight
        self.children = {}
        self.end_weight = end_weight
        self.max_weight = max_weight
        self.full_word = full_word

    def insertWord(self, word, weight, full_word=None):

        """ Inserting all attributes (word, weight) into nodes recursively

        Parameters
        ----------
        word = each word from the inputted txt file
        weight = each word's associated weight from the txt file
        full_word = initialize it as None and updated immediately to 'word'
        input from insertWord function. (local version of full_word)

        Results
        ----------
        Builds nodes but does not return any physical result

        """

        # To avoid losing the inputted word from recursion, store the original
        # inputted word as full_word
        if full_word is None:
            full_word = word
        # At the end of the recursion when the word becomes an empty string,
        # update full_word, end_weight, and max_weight (optional)
        if word == "":
            self.full_word = full_word
            self.end_weight = weight
            if self.end_weight > self.max_weight:
                self.max_weight = self.end_weight
            return
        # Initialize the first letter of a word (recursively updated)
        first_letter = word[0]
        # If the weight is greater than the max weight throughout recursion,
        # update the max weight to be the weight of a word
        if weight > self.max_weight:
            self.max_weight = weight
        # If the first letter is not in the children dictionary,
        # Go back to Node() and initialize new node with default property
        if first_letter not in self.children:
            self.children[first_letter] = Node()
        # Go down one more node without first letter and repeat same process
        self.children[first_letter].insertWord(word[1:], weight, full_word)

# AUTOCOMPLETE - reading the txt file
def read_terms(path):

    """ Reading a data file and produce nodes by using insertWord function

    Parameters
    ----------
    path = a path / directory of the data file

    Results
    ----------
    node_result = Building nodes by using insertWord function from Node() class

    """

    node_result = Node()
    with open(path, "r") as f:
        lines = f.readlines()
        for ii in range(1, len(lines)):
            if lines[ii].strip() == "":
                continue
            weight, word = lines[ii].split('\t')
            weight = int(weight)
            node_result.insertWord(word.strip(), weight)
    return node_result

# AUTOCOMPLETE - building class Trie
class Trie:
    def __init__(self, trie_input):

        """ Creating a trie by connecting nodes created from read_terms()

        Parameters
        ----------
        trie_input = an inputted trie built from read_terms

        Results
        ----------
        Connects all the nodes from read_terms called full_trie
        but does not return any physical result (only store full_trie)

        """

        # store original trie as self.full_trie
        self.trie_input = trie_input
        self.full_trie = self.trie_input
        # Initialize updated_trie that will be updated from searchTrie
        self.updated_trie = self.full_trie

    def searchTrie(self, target_word):

        """ Searching target word (prefix that the user inputed to autocomplete)
            from updated_trie and update updated_trie

        Parameters
        ----------
        target_word = a target word that user inputted into autocomplete

        Results
        ----------
        self.updated_trie = a trie after searching for the target wrod

        """

        if target_word == "":
            return self.updated_trie
        for letter in target_word:
            if letter not in self.updated_trie.children:
                return
            else:
                self.updated_trie = self.updated_trie.children[letter]
        return self.updated_trie

def autoComplete(target_word, trie_input, suggest_num):

    """ Suggesting top suggest_num of words with highest weight from txt file

    Parameters
    ----------
    target_word = a target word that user inputted into autocomplete

    trie_input = a trie that was built after the read_terms

    suggest_num = the number of suggested words that needs to be returned

    Results
    ----------
    recommend_word = a list of top n recommended words and their weights,
    which starts with the target word

    """

    start = Trie(trie_input).searchTrie(target_word)
    if start == None:
        print("Cannot recommend any words")
        return
    else:
        start_node = start.children
        recommend_word = []
        pq = []
        for child in start_node.values():
            if child.full_word is not None:
                heapq.heappush(pq, (-child.end_weight, id(child), child, True))
                heapq.heappush(pq, (-child.max_weight, id(child), child, False))
            else:
                heapq.heappush(pq, (-child.max_weight, id(child), child, False))
        while len(pq) > 0 and len(recommend_word) < suggest_num:
            max_weight_node = heapq.heappop(pq)
            if max_weight_node[3] is True:
                recommend_word.append((abs(max_weight_node[0]), max_weight_node[2].full_word))
            else:
                for subchild in max_weight_node[2].children.values():
                    if subchild.full_word is not None:
                        heapq.heappush(pq, (-subchild.end_weight, id(subchild), subchild, True))
                        heapq.heappush(pq, (-subchild.max_weight, id(subchild), subchild, False))
                    else:
                        heapq.heappush(pq, (-subchild.max_weight, id(subchild), subchild, False))
        recommend_word = sorted(recommend_word, key = lambda x: (x[0], x[1]), reverse = True)
        if len(recommend_word) < suggest_num and len(recommend_word) > 0:
            print("Failed to suggest all", suggest_num, "words, only suggesting", len(recommend_word), "words")
        return recommend_word

def add_term(add_word, weight, trie_input):

    """ Adding a term into the trie input

    Parameters
    ----------
    add_word = a word / term we hope to add into the trie

    weight = a weight of the word / term

    trie_input = an input that represents the trie after successfully inserting
    words into the trie by using the combination of read_terms and insertWord

    Results
    ----------
    trie_input = an updated trie node after adding the word / term

    """
    retrieve_node = Trie(trie_input).searchTrie(add_word)
    if retrieve_node is None or retrieve_node.max_weight < weight:
        trie_input.insertWord(add_word, weight)
    return trie_input

def delete_term(delete_word, trie_input, terminal = True, terminal2 = True):

    """ Deleting a term from a trie

    Parameters
    ----------
    delete_word = an input that represents which trie to delete

    trie_input = an input that represents the trie after successfully inserting
    words into the trie by using the combination of read_terms and insertWord

    terminal = a boolean (T/F) value that represents when to reassign full_word
    and end_weight (True for reassign, False for not reassign)

    terminal2 = a boolean (T/F) value that represents when to delete the node
    True when there are no children after the deletion
    False when there is a children after the deletion

    Results
    ----------
    trie_input = an updated trie node after deleting the inputted word / term

    """
    if delete_word == "":
        top_node = Trie(trie_input).searchTrie(delete_word)
        for top_node_child in top_node.children.values():
            weight_list = []
            weight_list.append(top_node_child.max_weight)
            weight_list = sorted(weight_list, reverse = True)
        top_node.max_weight = weight_list[0]
        return trie_input
    retrieve_node = Trie(trie_input).searchTrie(delete_word)
    last_letter = delete_word[-1:]
    retrieve_node_prior = Trie(trie_input).searchTrie(delete_word[:-1])
    if len(retrieve_node.children) != 0:
        weight_list = []
        for child in retrieve_node.children.values():
            weight_list.append(child.max_weight)
            weight_list = sorted(weight_list, reverse = True)
        retrieve_node.max_weight = weight_list[0]
        if terminal is True:
            retrieve_node.full_word = None
            retrieve_node.end_weight = -1000
        delete_term(delete_word[:-1], trie_input, False, False)        
    else:
        if terminal2 is True:
            if retrieve_node_prior.full_word is None:
                # case when you are deleting the node and the corresponding
                # parent node is not a full word --> can delete the parent node
                del retrieve_node_prior.children[last_letter]
                delete_term(delete_word[:-1], trie_input, False, True)
            else:
                # case when you are deleting the node but the corresponding
                # parent node is also a full word --> can't delete parent node
                retrieve_node_prior.max_weight = retrieve_node_prior.end_weight
                del retrieve_node_prior.children[last_letter]
                delete_term(delete_word[:-1], trie_input, False, False)
        else:
            delete_term(delete_word[:-1], trie_input, False, False)

def change_weight(trie_input, change_word, weight_fx):

    """ Changing the weight of a term already in the trie

    Parameters
    ----------
    trie_input = an input that represents the trie after successfully inserting
    words into the trie by using the combination of read_terms and insertWord

    change_word = a word / term we hope to change the weight

    weight_fx = another function that can change the weight of the word

    Results
    ----------
    trie_input = an updated trie node after changing the weight of a word

    """
    retrieve_node = Trie(trie_input).searchTrie(change_word)
    if retrieve_node == None:
        print ("Cannot change the weight of the inputed word, because the word does not exist in the Trie.")
        return trie_input
    if retrieve_node.end_weight == -1000:
        print ("Cannot change the weight of the inputed word, because it is not a full word.")
        return trie_input
    else:
        new_end_weight = weight_fx(retrieve_node.end_weight)
        delete_term(change_word, trie_input)
        trie_input.insertWord(change_word, new_end_weight)
    return trie_input

def insert_or_update(change_word, weight, trie_input):

    """ Given word, insert the term into the trie if it is not there already, or
    increase the weight of the term by 1 if it is - weights are increased every
    time a word is used, meaning that popular terms get higher weights

    Parameters
    ----------
    change_word = a word / term we hope to insert or update

    weight = a weight of the word input

    trie_input = initial trie to start with that represents the trie after
    successfully inserting words into the trie by using the combination of
    read_terms and insertWord

    Results
    ----------
    trie_input = an updated trie after the user runs the autoComplete function

    """
    retrieve_node = Trie(trie_input).searchTrie(change_word)
    if retrieve_node == None or retrieve_node.end_weight == -1000:
        add_term(change_word, weight, trie_input)
        return trie_input
    else:
        new_end_weight = retrieve_node.end_weight + 1
        add_term(change_word, new_end_weight, trie_input)
        return trie_input

def prune_trie(trie_input, threshold):

    """ Deleting all terms with weights under a threshold from the trie_input

    Parameters
    ----------

    trie_input = initial trie to start with that represents the trie after
    successfully inserting words into the trie by using the combination of
    read_terms and insertWord

    threshold = a weight threshold set by the user to delete a word from a trie

    Results
    ----------
    trie_input = an updated trie after running prune_trie function

    """
    full_trie_result = autoComplete("", trie_input, 2147483647)
    under_threshold_word = []
    for i in range(0, len(full_trie_result)):
        if full_trie_result[i][0] < threshold:
            under_threshold_word.append(full_trie_result[i][1])
    for word in under_threshold_word:
        delete_term(word, trie_input)
    return trie_input

def rescale_weights(trie_input, weight_fx):

    """ Rescaling all weights in a trie

    Parameters
    ----------
    trie_input = an input that represents the trie after successfully inserting
    words into the trie by using the combination of read_terms and insertWord

    weight_fx = another function that changes the weight (for whole trie)

    Results
    ----------
    updated_trie = an updated trie node after changing the weight of a word

    """
    start = Trie(trie_input).searchTrie("")
    all_children = collections.deque(list(start.children.values()))
    while all_children:
        child = all_children.popleft()
        if child.full_word is not None:
            child.end_weight = weight_fx(child.end_weight)
            child.max_weight = weight_fx(child.max_weight)
        else:
            child.end_weight = weight_fx(child.end_weight)
        all_children.extendleft(list(child.children.values()))
    return trie_input