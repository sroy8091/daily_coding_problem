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
    res = [[root.value]]
    while queue:
        level = len(queue)
        while level:
            temp = queue.pop(0) 
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            level -= 1
        if queue:
            res.append([x.value for x in queue])
    return res

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
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

def main():
    n1 = Node(5)
    n2 = Node(6)
    n3 = Node(3, n1, n2)
    n4 = Node(4)
    n5 = Node(2, n3, n4)
    n6 = Node(1)
    root = Node(0, n6, n5)
    print(level_order_traversal(root))
    # dfs_r(root)
    # dfs(root)

if __name__=="__main__":
    main()