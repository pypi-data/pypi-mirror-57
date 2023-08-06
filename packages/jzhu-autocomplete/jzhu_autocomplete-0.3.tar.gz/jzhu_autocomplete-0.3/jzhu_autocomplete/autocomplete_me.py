
import heapq
#import os
#os.chdir('C:/Users/dell/Documents/s750/assignments-junyi-zhu/autocomplete-me')



##############################################################################
################################ SLOWCOMPLETE ################################
##############################################################################

def read_terms_slow(path):
    """
    Parses the input file and store the corresponding word and weight  
    Params: 
            path: the path to the input file
    Return: 
            mylist: a list that looks like [(weight1, word1), ...]
    """
    mylist = []
    with open(path, "r", encoding="utf8") as fp:
        line = fp.readlines()
        for i in range(1, len(line)):
            if line[i].strip() == "":
                continue
            weight, word = line[i].split('\t')
            weight = int(weight)
            word = word.strip()
            mylist.append((weight, word))
    return mylist

def slowcomplete(mylist, prefix, k):
    """
    Given a prefix, suggest the top k words with the highest weight  
    Params:  
            prefix: the prefix to search in the list
            mylist: a list with stored words and corresponding weights
            k: the number of top recommendations ordered by weight  
    Return: 
            reclist: list of top k recommendations matching the prefix
    """
    assert isinstance(mylist, list), "The search space should be a list."
    assert isinstance(prefix, str), "The prefix should be a string"
    assert isinstance(k, int), "The number of suggestions should be a positive integer"
    assert k > 0, "The number of suggestions should be a positive integer"

    reclist = []
    for i in range(len(mylist)):
        # note: mylist contains [(weight1, word1), (weight2, word2), ...]
        if prefix != mylist[i][1] and mylist[i][1].startswith(prefix):
            reclist.append(mylist[i])
    reclist = sorted(reclist, key=lambda x: x[0], reverse=True)
    if len(reclist) == 0:
        return 'No words match with the given prefix.'
    return reclist[0:k]
    # return [x[1] for x in reclist[0:k]]



##############################################################################
################################ AUTOCOMPLETE ################################
##############################################################################

class Node:
    """ build the nodes and define the children of nodes """

    def __init__(self):
        """
        Attributes:  
            children: node object, a node's children, stores letter and weight  
            weight: numeric, weight of each node  
            maxweight: numeric, the maximum weight of a node's children  
            fullword: stores the word at the node when it is the end of the word
        """
        self.children = {}
        self.weight = -1
        self.maxweight = -1
        self.fullword = None

    def insertWord(self, weight, word, fullword=None):
        """
        Store each letter from a word into nodes (one letter per node)  
        Params:
                word: words/phrases to be inserted into the trie
                weight: the corresponding weights for each word/phrase
        Return:
                nothing; this function simply builds a trie
        """
        assert isinstance(weight, int)

        if fullword is None:
            fullword = word

        if word == "":
            self.weight = weight
            self.fullword = fullword
            if self.weight > self.maxweight:
                self.maxweight = self.weight
            return

        if weight > self.maxweight:
            self.maxweight = weight

        first_letter = word[0]
        if word[0] not in self.children:
            self.children[first_letter] = Node()

        self.children[first_letter].insertWord(weight, word[1:], fullword)

def read_terms_auto(path):
    """
    Parses the input file and store the words and weights into a trie  
    Params:
            path: the path to the input file
    Return:
            mytrie: a trie with stored words and corresponding weights
    """
    mytrie = Node()
    with open(path, "r", encoding="utf8") as fp:
        line = fp.readlines()
        for i in range(1, len(line)):
            if line[i].strip() == "":
                continue
            weight, word = line[i].split('\t')
            weight = int(weight)
            word = word.strip()
            mytrie.insertWord(weight, word)
    return mytrie


class Trie:
    """ Build the trie using the attributes from class Node """
    def __init__(self, mytrie):
        """
        Attributes:  
            mytrie: a trie object, taking attributes from the Node class
        """
        self.mytrie = mytrie

    def searchTrie(self, prefix: str):
        """
        Searches the prefix in the trie with words and weights  
        Params:
                prefix: the prefix to search in the trie
        Return:
                if predix not in trie: return False
                if predix in trie: return mytrie, the node to start search from
        """
        mytrie = self.mytrie
        for letter in list(prefix):
            letter_not_found = True
            for child in mytrie.children:
                if child == letter:
                    letter_not_found = False
                    mytrie = mytrie.children[letter]
                    break
            if letter_not_found:
                return False
        return mytrie


def autocomplete(mytrie, prefix, k):
    """
    Given a prefix, suggest the top k words with the highest weight  
    Params:  
            prefix: the prefix to search in the list
            mytrie: a trie with stored words and corresponding weights
            k: the number of top recommendations ordered by weight  
    Return: reclist: list of top k recommendations matching the prefix
    """
    assert isinstance(prefix, str), "The prefix should be a string"
    assert isinstance(k, int), "The number of suggestions should be a positive integer"
    assert k > 0, "The number of suggestions should be a positive integer"

    start = Trie(mytrie).searchTrie(prefix)
    if start is False:
        return "No words match with the given prefix."
    
    reclist = []
    pq = []
    
    for child in start.children.values():
        heapq.heappush(pq, (-child.maxweight, id(child), child, False))
        if child.fullword is not None:
            heapq.heappush(pq, (-child.weight, id(child), child, True))
    
    while len(pq) > 0 and len(reclist) < k:
        # mwc: the child with max weight popped out from the priority queue
        mwc = heapq.heappop(pq)
        # if the weight and the maxweight matches
        if mwc[3] == True:
            reclist.append((mwc[2].weight, mwc[2].fullword))
        else:
            for child in mwc[2].children.values():
                heapq.heappush(pq, (-child.maxweight, id(child), child, False))
                if child.fullword is not None:
                    heapq.heappush(pq, (-child.weight, id(child), child, True))
    # return reclist
    return [(x[0],x[1]) for x in reclist]


##############################################################################
#################### ADD_TERM, DELETE_TERM, CHANGE_WEIGHT ####################
##############################################################################

def add_term(mytrie, word, weight):
    """
    Add a term with the weight into an existing trie  
    Params:  
            mytrie: the trie to add the word into
            word: the word to add into the trie
            weight: the weight of the word to be inserted
    Return: 
            mytrie: an updated trie with word inserted into it
    """
    assert isinstance(word, str), "The word to be added should be a string."
    assert isinstance(weight, int), "The weight of the word should be an integer"
    mytrie.insertWord(weight, word)


def insert_or_update(mytrie, word, newweight):
    """
    Word not in trie -> insert word into trie with the designated newweight  
    Word in trie     -> increase the weight of the term by 1, and update the
    maxweight if the newly updated weight > maxweight
    Params: 
            word: the word to add into the trie or update the weight
            weight: the weight of the word to be inserted
    Returns:
            a trie with either an updated dictionary or an updated weight
    """
    assert isinstance(word, str), "The word to be added should be a string."
    assert isinstance(newweight, int), "The weight of the word should be an integer"

    node = Trie(mytrie).searchTrie(word)

    if node is not False:
        weightplusone = node.weight + 1
        mytrie.insertWord(weightplusone, word)
        return
    else:
        mytrie.insertWord(newweight, word)


def delete_term(mytrie, word, end1=True, end2=True):
    """
    Delete a word from an existing trie  
    Params:  
            mytrie: the trie to delete the word from
            word: the word to delete from the trie
    Return: 
            mytrie: an updated trie with the input word deleted
    """
    assert isinstance(word, str), "The word to be deleted should be a string." 

    # Base case: at the toot node, word[:-1] doesn't exist
    if word == "":
        root = Trie(mytrie).searchTrie("")
        rootweightlist = []
        for rootchild in Trie(mytrie).searchTrie("").children.values():
            rootweightlist.append(rootchild.maxweight)
        root.maxweight=max(rootweightlist)
        return mytrie
    
    else:
        node = Trie(mytrie).searchTrie(word)
        parentnode = Trie(mytrie).searchTrie(word[:-1])

        # Case 1: node has children
        if len(node.children) != 0:
            weightlist = []
            for child in node.children.values():
                weightlist.append(child.maxweight)
            node.maxweight = max(weightlist)
            # I still don't get why this works...
            if end1 is True:
                node.fullword = None
                node.weight = -1
            delete_term(mytrie, word[:-1], False, False)

        # Case 2: node does not have children
        else: 
            if end2 is True:
                # Case 2.1: parentnode is not a full word - just delete
                if parentnode.fullword is None:
                    del parentnode.children[word[-1:]]
                    delete_term(mytrie, word[:-1], False, True)

                # Case 2.2: parentnode is a full word (e.g. in and inn)
                else:
                    parentnode.maxweight = parentnode.weight
                    del parentnode.children[word[-1:]]
                    delete_term(mytrie, word[:-1], False, False)
            else:
                delete_term(mytrie, word[:-1], False, False)


def change_weight(mytrie, word, updatefunc):
    """
    Change the weight of a term already in the trie. 
    
    To account for the possible change in the maxweight, we will change weight 
    by first deleting the term and using the insertWord() function to add the 
    word back into the trie with the new weight. 

    Params:
            mytrie: the trie that we operate on
            word: the word to change weight
            updatefunc: the function that takes the current weight as an 
                        argument and return the desired new weight
                        (examples of update functions are defined and called 
                        in the test file directly)
    Return:
            mytrie: an updated trie where the input word has an updated weight
    """
    assert isinstance(word, str), "The word to change weight should be a string."

    node = Trie(mytrie).searchTrie(word)
    # if word doesn't exist in trie or it is not a full word in trie
    if node is None or node.weight == -1:
        return mytrie
    else:
        oldweight = node.weight
        newweight = updatefunc(oldweight)
        delete_term(mytrie, word)
        mytrie.insertWord(newweight, word)
    return mytrie


def prune_trie(mytrie, threshold):
    """
    Traverse the input trie and delete all words with weights smaller than threshold.  
    Params:
            mytrie: the trie to prune
            threshold: an integer as the weight threshold; words with weights 
                       lower than threshold will be deleted
    Return:
            mytrie: an updated tree such that the words with weights under the 
            threshold are deleted
    """
    assert isinstance(threshold, int)
    fulltrie = autocomplete(mytrie, "", 2147483647)
    lst = []
    for i in range(0, len(fulltrie)):
        if fulltrie[i][0] <= threshold:
            lst.append(fulltrie[i][1])
    for word in lst:
        delete_term(mytrie, word)
    return mytrie


def rescale_weight(mytrie, updatefunc):
    """
    Scale all weights in a trie by a function
    Params:
            mytrie: the trie to scale the weights
            updatefunc: a monotone function that takes the current weight as an 
                        argument and return the desired new weight
    Return:
            mytrie: an updated trie with its weights rescaled
    """
    fulltrie = autocomplete(mytrie, "", 2^31-1)
    lst = []
    for i in range(0, len(fulltrie)):
        lst.append(fulltrie[i][1])
    for word in lst:
        change_weight(mytrie, word, updatefunc)
    return mytrie


