class Trie: 
    def __init__(self):
        self.root = Node()

class Node: 
    def __init__(self, data=None):
        self.data = data 
        self.links = [None] * 27