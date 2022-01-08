class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data <= cur_node.data:
            if cur_node.left == None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        else:
            if cur_node.right == None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
            print("inorder")
            self.inorder(self.root)
            print("preorder")
            self.preorder(self.root)
            print("postorder")
            self.postorder(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print(cur_node.data)
            self._print_tree(cur_node.right)

    def inorder(self, cur):
        if cur == None:
            return
        self.inorder(cur.left)
        print(cur.data)
        self.inorder(cur.right)

    def preorder(self, cur):
        if cur == None:
            return
        print(cur.data)
        self.preorder(cur.left)
        self.preorder(cur.right)

    def postorder(self, cur):
        if cur == None:
            return
        self.postorder(cur.left)
        self.postorder(cur.right)
        print(cur.data)

    def bfs(self):
        print("bfs")
        q = [self.root]
        if self.root:
            self._bfs(self.root, q)
        else:
            print("NO NODE TO Traverse")

    def _bfs(self, cur, q):
        while len(q) > 0:
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            s = q.pop(0)
            print(s.data)
            if len(q):
                cur = q[0]

    def dfs(self):
        print("DFS")
        stack = []
        if self.root:
            self._dfs(self.root, stack)
        else:
            print("NO NODE TO Traverse")

    def _dfs(self, cur, stack):
        i = - 1
        while 1:
            if cur not in stack:
                print(cur.data)
                if len(stack) == 0 and (cur.left and cur.right) == None:
                    break
                if cur.left or cur.right:
                    stack.append(cur)
                    i += 1
                    if cur.left:
                        cur = cur.left
                else:
                    cur = stack[i]
            else:
                if cur.right:
                    cur = cur.right
                    stack.pop(i)
                    i -= 1
                else:
                    stack.pop(i)
                    i -= 1
                    cur = stack[i]

    def height(self):
        return self._height(self.root)

    def _height(self, cur):
        if cur is None:
            return 0
        lh = self._height(cur.left)
        rh = self._height(cur.right)
        return (max(lh, rh) + 1)

    def spiral(self):
        h = self.height()
        curr = self.root
        for i in range(1, h + 1):
            self.print_level(curr, i, i % 2)

    def print_level(self, curr, l, flag):
        if curr is None:
            return
        if l == 1:
            print(curr.data)
            return
        if flag == 1:
            self.print_level(curr.left, l - 1, flag)
            self.print_level(curr.right, l - 1, flag)
        else:
            self.print_level(curr.right, l - 1, flag)
            self.print_level(curr.left, l - 1, flag)

    def is_bst(self):
        return self._is_bst(self.root)

    def _is_bst(self, cur):
        if cur == None:
            return 1
        if cur.left and cur.data > cur.left.data:
            self._is_bst(cur.left)
            return 1
        if cur.right and cur.data < cur.right.data:
            self._is_bst(cur.right)
            return 1
        if (self._is_bst(cur.left) and self._is_bst(cur.right)) is 1:
            return 1
        return 0

        def reverseLevelOrder(self, root):
            h = self.height(root)

        for i in reversed(range(1, h + 1)):
            self.printGivenLevel(root, i)
            # Print nodes at a given level

    def printGivenLevel(self, root, level):

        if root is None:
            return
        if level == 1:
            print(root.data, end=" ")

        elif level > 1:
            self.printGivenLevel(root.left, level - 1)
            self.printGivenLevel(root.right, level - 1)


t = Tree()
t.insert(40)
t.insert(30)
t.insert(50)
t.insert(46)
t.insert(45)
t.insert(12)
t.insert(32)
t.insert(33)
t.insert(47)
t.insert(90)
t.insert(1)
# t.print_tree()
# t.bfs()
t.dfs()
# print(t.height())
# t.spiral()
# print(t.is_bst())


"""Tree
        40
   30   |    50
 12  32 |  46  90
1     33|45  47      """


