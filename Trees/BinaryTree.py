from dataclasses import dataclass


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# create root
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

'''4 becomes left child of 2
           1
       /       \
      2          3
    /   \       /  \
   4    None  None  None
  /  \
None None'''

# Tree Traversal
def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.key)
        Inorder(root.right)

def Preorder(root):
    if root:
        print(root.key)
        Preorder(root.left)
        Preorder(root.right)

def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.key)

Inorder(root)
Preorder(root)
Postorder(root)