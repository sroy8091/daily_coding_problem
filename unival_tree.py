"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

def is_unival(root):
    if root.left: 
        if root.left.value != root.value:
            return False
        else:
            right_true =  is_unival(root.right)
    if root.right:
        if root.right.value != root.value:
            return False
        else:
            left_true =  is_unival(root.left)
    else:
        return True
    if right_true and left_true:
        return True

    return False

def count_unival(root):
    if root == None:
        return 0
    total_count = count_unival(root.left) + count_unival(root.right)
    if is_unival(root):
        total_count += 1
    return total_count

class Node:
    def __init__(self, val, right=None, left=None):
        self.right = right
        self.left = left
        self.value = val

def main():
    n1 = Node(1)
    n2 = Node(1)
    n3 = Node(1, n1, n2)
    n4 = Node(0)
    n5 = Node(0, n4, n3)
    n6 = Node(1)
    root = Node(0, n5, n6)
    print(count_unival(root))


if __name__=="__main__":
    main()