"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and 
a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], 
return [deer, deal].
"""

class TrieNode:
    def __init__(self, char):
        self.children = []
        self.is_end_of_word = False
        self.counter = 1
        self.char = char


def insert(root, word):
    node = root
    for i in word:
        found_in_child = False
        for j in node.children:
            if j.char == i:
                found_in_child = True
                j.counter += 1
                node = j
                break
        if not found_in_child:
            new_node = TrieNode(i)
            node.children.append(new_node)
            node = new_node
    
    node.is_end_of_word = True


def print_all_words(root, prefix, res):
    if root.is_end_of_word:
        res.append(prefix)
    for i in root.children:
        print_all_words(i, prefix+i.char, res)


def autocomplete(root, prefix):
    node = root
    res = []
    for i in prefix:
        found = False
        for child in node.children:
            if child.char == i:
                found = True
                break
        if not found:
            print("Prefix not found in any words of given array")
            return
        else:
            node = child
    print_all_words(node, prefix, res)
    return res
        


def main():
    root = TrieNode('*')
    arr = ["dog", "deer", "deal"]
    prefix = "de"
    for i in arr:
        insert(root, i)
    print(autocomplete(root, prefix))


if __name__=="__main__":
    main()