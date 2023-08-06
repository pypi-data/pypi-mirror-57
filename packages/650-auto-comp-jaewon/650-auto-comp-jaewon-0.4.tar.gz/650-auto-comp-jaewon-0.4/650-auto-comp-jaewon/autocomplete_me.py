import heapq as hq


def read_terms(textfile):
    """
    Parameters
    ----------
    textfile: textfile containing weights and words

    Returns
    ----------
    list of words containing weights and words
    """
    list_of_words = []
    file = open(textfile, "r")
    text = file.readlines()
    for i in range(1,len(text)):
        if text[i] == '':
            continue
        weight, word = text[i].split('\t')
        word = word.strip()
        weight = weight.strip()
        weight = int(weight)
        list_of_words.append((weight, word))
        
    return list_of_words


def slowComplete(string, list_of_words, n):
    """
    Parameters
    ----------
    string: a string
    list_of_words: list of weights and words
    n: number of observations

    Returns
    ----------
    Return n numbers of possible string completions from list in order of descending weight
    """
    matches = []
    for weight, word in list_of_words:
        if word.lower().startswith(string):
            matches.append((weight, word))

    sorted_matches = sorted(matches, key=lambda x: x[0], reverse=True)
    return sorted_matches[0:n]



class Node:
    def __init__(self, letter = None, full_word = None, max_weight = None, weight = None):
        """
        Parameters
        ----------
        children: children of each node
        letter: each letter of a word to be inserted into the tree
        full_word: full word
        max_weight: maximum weight of the word
        weight: weight of each word (to distinguish if part of word can also be full word)
        """
        self.children = {}
        self.letter = letter
        self.full_word = full_word
        self.max_weight = max_weight
        self.weight = weight

    def __lt__(self, other):
        return True


class QueueNode:
    def __init__(self, target, parent):
        """
        Parameters
        ----------
        This class is used for pruning the trie.
        Later on, QueueNode is used as a target and parent Node that acts as queue.

        target: target node
        parent: parent node
        """
        self.target = target
        self.parent = parent


class Trie:
    def __init__(self):
        """
        Parameters
        ----------
        Root of the trie is the node
        """
        self.root = Node(letter = None, full_word = None, max_weight = None, weight = None)
     
        
    def insert(self, word, weight):
        """
        Parameters
        ----------
        This function inserts each letter of a word onto each node.
        The max weight is stored at each node.
        The full completed word is stored at the end of the node after all letters have been inserted.
        The weight of the word is also stored at the end of the node.
        """
        node = self.root 
        for letter in word.lower():
            if letter not in node.children:
                node.children[letter] = Node(letter = letter, max_weight = -1*weight) # each node contains letter and weight of word; letter becomes key, node becomes value of the dictionary
            else:
                node.children[letter].max_weight = min(node.children[letter].max_weight, -1*weight) # update the max weight if weight of inserted word is higher
            node = node.children[letter] # re-initialize node
        
        node.full_word = word # store full word at the end
        node.weight = -1*weight # store weight at the end


    def search_autocomplete(self, word_prefix, n):
        """
        Parameters
        ----------
        word_prefix: word prefix to be searched in the trie
        n: number of suggestions

        Returns
        ----------
        n number of suggestions ordered by highest weight that starts with the word_prefix.
        """

        node = self.root
        results = []
        for letter in word_prefix.lower(): # For every letter in word
            if letter not in node.children.keys(): # if letter not in children keys
                return []
            else:
                node = node.children[letter] # follow the nodes down

        queue = []
        hq.heapify(queue) # heapify the queue
        hq.heappush(queue, (node.max_weight, False, node)) # push max weight and node
        word_count = 0

        while word_count < n and len(queue) > 0:
            _, is_word, node = hq.heappop(queue)

            if is_word:
                results.append(node.full_word)
                word_count += 1
            else:
                for child in node.children.values():
                    hq.heappush(queue, (child.max_weight, False, child))

                    if child.full_word != None:
                        hq.heappush(queue, (child.weight, True, child))
                        
        return results


    def delete(self, word):
        """
        This function deletes the input word in the trie.

        Parameters
        ----------
        word: word to be deleted in the trie.
        
        """
        node = self.root
        
        nodes = []
        for letter in word.lower(): 
            if letter in node.children.keys():
                node = node.children[letter]

                nodes.append(node)

        nodes[-1].full_word = None
        nodes[-1].weight = None

        for i in range(len(nodes) - 1, 0, -1):
            node = nodes[i]
            parent_node = nodes[i - 1]

            if len(node.children) == 0:
                parent_node.children.pop(node.letter)

            if len(parent_node.children) > 0:
                parent_node.max_weight = max(
                    child.max_weight 
                    for child in parent_node.children.values()
                )


    def change_weight(self, word, func):
        """
        Change weights on a term inside the trie according to 'func.'
        """
        
        node = self.root

        nodes = []

        for letter in word.lower(): 
            if letter in node.children.keys():
                node = node.children[letter]

                nodes.append(node)

        nodes[-1].max_weight = func(nodes[-1].max_weight)
        nodes[-1].weight = func(nodes[-1].weight)

        for i in range(len(nodes)-1,0,-1):
            node = nodes[i]
            parent_node = nodes[i-1]

            if len(node.children) == 0:
                parent_node.max_weight = func(parent_node.max_weight)

            if len(parent_node.children) > 0:
                parent_node.max_weight = max(child.max_weight for child in parent_node.children.values())
        

    def insert_or_update(self, word):
        """
        Insert word, if not there already, 
        or increase weights inside the trie by 1, if there already.
        """

        if Trie.search_autocomplete(self, word, 1) == []:
            Trie.insert(self, word, -1)
        else:
            Trie.change_weight(self, word, lambda x: x + 1)

    
    def prune_trie(self, threshold):
        """
        This function deletes all terms inside trie with weights under the threshold.
        """

        node = QueueNode(self.root, None)
        threshold = -1 * threshold

        queue = []
        queue.append(node)

        while (len(queue) > 0):
            node = queue.pop(0)
            if node.target.weight != None and node.target.weight > threshold:
                node.parent.children.pop(node.target.letter)
            else:
                for child in node.target.children.values():
                    queue.append(QueueNode(child, node.target))


    def rescale_weights(self, func):
        """
        This function scales all weights in a trie by a function.
        """
        node = self.root

        for child_node in list(node.children.values()):
            child_node.max_weight = func(child_node.max_weight)
            if child_node.full_word != None:
                node.weight = func(node.weight)
        


