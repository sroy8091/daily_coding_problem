"""
   0
  / \
 1   2
    / \
   3   4
  / \
 5   6
"""

height_sum = 0

def height_util(root):
    global height_sum
    if not root:
        return -1
    lh = height_util(root.left)
    rh = height_util(root.right)
    height_sum += max(lh, rh) + 1
    return max(lh, rh) + 1

def get_height(root):
    height_util(root)
    print(height_sum)


class Node:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.value = val

def main():
    n1 = Node(5)
    n2 = Node(6)
    n3 = Node(3, n1, n2)
    n4 = Node(4)
    n5 = Node(2, n3, n4)
    n6 = Node(1)
    root = Node(0, n6, n5)
    get_height(root)


if __name__=="__main__":
    main()