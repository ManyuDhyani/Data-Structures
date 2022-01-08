#check weather two trees are identical or not

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root1 = Node(20)
root1.left = Node(10)
root1.right = Node(30)
root1.right.right = Node(40)


"""
            20        
           10 30
            20
           10 40
"""



root2 = Node(20)
root2.left = Node(10)
root2.right = Node(30)
root2.right.left = Node(40)


def check_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 and root2:
        return ((root1.val == root2.val) and check_identical(root1.left, root2.left) and check_identical(root1.right, root2.right))
    return False

print(check_identical(root1, root2))