import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, data, pos):
        if self.length() < pos:
            print("INVALID POS")
            return 0
        new_node = Node(data)
        cur_node = self.head
        i = 1
        while i != pos:
            cur_node = cur_node.next
            i += 1
        new_node.next = cur_node.next
        cur_node.next = new_node

    def display(self):
        element = []
        cur_node = self.head
        while cur_node:
            element.append(cur_node.data)
            cur_node = cur_node.next
        print(element)

    def length(self):
        total = 0
        cur_node = self.head
        while cur_node != None:
            cur_node = cur_node.next
            total += 1
        return total

    def delete(self, pos):
        if pos > self.length():
            print("INVALID POSITION")
            return 0
        cur_node = self.head
        i = 1
        if pos == 1:
            x = cur_node.data
            self.head = self.head.next
            print(x)
            return 0
        while i != pos - 1:
            cur_node = cur_node.next
            i += 1
        x = cur_node.next.data
        cur_node.next = cur_node.next.next
        print(x)
        return 0

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def min_max(self):
        curr = self.head
        min = sys.maxsize
        max = 0
        while curr:
            if curr.data > max:
                max = curr.data
            if curr.data < min:
                min = curr.data
            curr = curr.next
        print(min, max)
        return 0

    def middle(self):
        pt1 = pt2 = self.head
        while pt2 and pt2.next:
            pt2 = pt2.next.next
            pt1 = pt1.next
        print(pt1.data)
        return 0

    def create_loop(self, pos):
        cur = self.head
        k = 1
        add = None
        while cur.next:
            if k == pos:
                add = cur
            k += 1
            cur = cur.next
        if add == None:
            cur.next = cur
        else:
            cur.next = add


l = Linked_List()
l.push(200)
l.append(70)
l.append(90)
l.push(99)
l.append(30)
l.push(100)
l.display()
print(l.length())
"""l.delete(3)
l.delete(2)
l.delete(4)
l.display()
l.reverse()
l.display()
l.min_max()"""
l.create_loop(6)
