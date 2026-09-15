class Trie: 
    def __init__(self):
        self.root = Node(level=0)

    def insert(self, key, data=None):
        # level 
        count_level = 1

        # start from root  
        current = self.root

        # iterate each character in key
        for char in key:
            index = ord(char) - 97 + 1
            print(char, ' insert index ', index, ' level ', current.level)

            # if path exist, move to next node
            if not current.links[index] is None:
                current = current.links[index]
            # if path doesnt exist, create a new node and move to the new node
            else:
                current.links[index] = Node(level=count_level)
                current = current.links[index]
            count_level += 1

        # go through terminal character ($)
        index = 0 
        if not current.links[index] is None:
            current = current.links[index]
        else:
            current.links[index] = Node(level=count_level)
            current = current.links[index]

        # add data 
        current.data = data

    def search(self, key):
        # begin from root 
        current = self.root 

        # iterate each char in string 
        for char in key:
            print('searching level: ', current.level)
            index = ord(char) - 97 + 1
            # if path exist
            if not current.links[index] is None:
                current = current.links[index]
            # if path doesnt exist, key doesnt exist
            else:
                raise Exception(str(key) + " key doesnt exist")

        # go through terminal character ($)
        index = 0
        print('searching level: ', current.level) 

        # if terminal character found, data exist at the next leaf
        if not current.links[index] is None:
            current = current.links[index] 
        # if terminal character not found, data doesnt exist
        else:
            raise Exception("Key doesnt exist")
        print('searching level: ', current.level) 
        return current.data



class Node: 
    def __init__(self, data=None, size=27, level=0):
        self.data = data 
        self.links = [None] * size
        self.level = level


trie_test = Trie()
trie_test.insert("lol", "i am lol")
trie_test.insert("loa", "i am loa")
trie_test.insert("uwu", None)

try:
    print(trie_test.search("lol"))
    print(trie_test.search("loa"))
    print(trie_test.search("uwu"))
except Exception as e:
    print(e)

try:
    print(trie_test.search("wtf"))
except Exception as e:
    print(e)