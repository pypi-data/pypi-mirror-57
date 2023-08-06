# autocomplete by Gunho Jung
gunhojung_autocomplete is a Python library for predicting the complete query 
that the user intends to type.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) install gunhojung_autocomplete

```bash
pip install gunhojung_autocomplete
```

## Usage

```python
import gunhojung_autocomplete as autocomplete_me
 # reads the txt file
pokemon = autocomplete_me.read_terms("autocomplete/Data/pokemon.txt")
# conducts an autocomplete 
autocomplete_me.autoComplete("Pika", pokemon, 1) # returns [(32501, 'Pikachu')]
```

## Explanation
Within autocomplete_me, there are eight functions that the user can call. The 
functions are 'read_terms, autoComplete, add_term, delete_term, change_weight, 
insert_or_update, prune_trie, rescale_weights'. These functions utilize 
the functionality of the Node() and Trie() Class. 

Node() Class has one function called insertWord, which inserts all attributes
(the weight and word) into the nodes (stored as a dictionary).

Trie() Class has one function called searchTrie, which quickly searches for the
node information of the the user's input word.

These two Class functions are automatically called when the user tries to call
the following eight functions.

(1) read_terms

```python
def read_terms(path):
    
    """ Searching target word (prefix that the user inputed to autocomplete)
            from updated_trie and update updated_trie
        
        Parameters
        ----------
        target_word = a target word that user inputted into autocomplete

        Results
        ----------
        self.updated_trie = a trie after searching for the target wrod

        """
```

(2) autoComplete

```python
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
```

(3) add_term

```python
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
```

(4) delete_term

```python
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
```

(5) change_weight

```python
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
```

(6) insert_or_update

```python
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
```

(7) prune_trie

```python
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
```

(8) rescale_weights

```python
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
```

## Contributing

Pull requests are always welcome. If you detect any bugs, please open an issue
first to discuss what you detected and how you would like it to be changed.

Or, you can send a direct email to gjung@andrew.cmu.edu.

## License
[MIT](https://choosealicense.com/licenses/mit/)