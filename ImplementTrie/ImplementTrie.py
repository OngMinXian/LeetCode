class Node:

    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = Node()
            curr_node = curr_node.children[char]
        curr_node.end = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for char in word:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        return curr_node.end

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))   # return True
print(obj.search("app"))   # return False
print(obj.startsWith("app"))   # return True
obj.insert("app")
print(obj.search("app"))   # return True
print()

obj = Trie()
obj.insert("app")
obj.insert("apple")
obj.insert("beer")
obj.insert("add")
obj.insert("jam")
obj.insert("rental")
print(obj.search("apps"))   # return False
print(obj.search("app"))   # return True
