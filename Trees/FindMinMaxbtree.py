class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def findMax(root):
 
    # Base case
    if (root == None):
        return float('-inf')
 
    # Return maximum of 3 values:
    # 1) Root's data 
    # 2) Max in Left Subtree
    # 3) Max in right subtree
    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)
    if (lres > res):
        res = lres
    if (rres > res):
        res = rres
    return res

def find_min_in_BT(root):
    if root is None:
        return float('inf')
    res = root.data
    lres = find_min_in_BT(root.leftChild)
    rres = find_min_in_BT(root.rightChild)
    if lres < res:
        res = lres
    if rres < res:
        res = rres
    return res