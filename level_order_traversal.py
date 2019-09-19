"""
   0
  / \
 1   2
    / \
   3   4
  / \
 5   6
"""



def level_order_traversal(root):
    queue = [root]
    temp = root
    while queue:
        print(queue[0].value, end=",")
        temp = queue.pop(0) 
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)


def dfs_r(root):
    "recursive"
    if root.left:
        dfs_r(root.left)
    print(root.value)
    if root.right:
        dfs_r(root.right)
    

def dfs(root):
    "iterative"
    stack = []
    current = root
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.value)
            current = current.right
        else:
            break
    




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
    # level_order_traversal(root)
    # dfs_r(root)
    # dfs(root)

if __name__=="__main__":
    main()