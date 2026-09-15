class Trie: 
    def __init__(self):
        self.root = Node()

    def insert(self, key, data=None):
        # start from root  
        current = self.root

        # iterate each character in key
        for char in key:
            index = ord(char) - 97 + 1
            print(index, char)

            # if path exist, move to next node
            if not current.links[index] is None:
                current = current.links[index]
            # if path doesnt exist, create a new node and move to the new node
            else:
                current.links[index] = Node()
                current = current.links[index]

        # go through terminal character ($)
        index = 0 
        if not current.links[index] is None:
            current = current.links[index]
        else:
            current.links[index] = Node()
            current = current.links[index]

        # add data 
        current.data = data 


class Node: 
    def __init__(self, data=None, size=27):
        self.data = data 
        self.links = [None] * size


trie_test = Trie()
trie_test.insert("oklo", "sap baby")