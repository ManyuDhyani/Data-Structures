class Node:
    def __init__(self,data):
        self.data = data
        self.pre = None
        self.next = None

class Doubly_Linked_List:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur=cur.next
            cur.next=new_node
            cur.next.pre=cur
    def print_db(self):
        cur=self.head
        print()
        while cur:
            print("<-", cur.data, "->", end="")
            cur = cur.next
    def print_reverse_db(self):
        cur=self.head
        while cur.next:
            cur=cur.next
        print()
        while cur:
            print("<-", cur.data, "->", end="")
            cur = cur.pre
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head.pre=new_node
        self.head=new_node
    def insert(self, pos, data):
        if pos>self.length() or pos==0:
            print()
            print("INVALID POS")
            return
        new_node = Node(data)
        i = 1
        cur = self.head
        while i != pos:
            cur = cur.next
            i+=1
        new_node.next = cur.next
        if cur.next:
            cur.next.pre=new_node
        else:
            pass
        cur.next = new_node
        new_node.pre = cur
    def length(self):
        cur = self.head
        total = 0
        while cur:
            cur=cur.next
            total+=1
        return total
    def delete(self,pos):
        if pos==1:
            x = self.head.data
            self.head = self.head.next
            self.head.pre = None
            return x
        else:
            i= 1
            cur = self.head
            while i!=pos-1:
                cur = cur.next
                i+=1
            x = cur.next.data
            cur.next=cur.next.next
            if cur.next:
                cur.next.pre = cur
            else:
                pass
            return x



d=Doubly_Linked_List()
d.append(90)
d.append(80)
d.append(40)
d.push(100)
d.insert(1, 200)
d.print_db()
print(d.length())
"""d.insert(4, 89)
d.push(98)
d.print_db()
print(d.length())
d.print_reverse_db()
print(d.length())
d.insert(0,23)
d.insert(7,89)
d.print_db()
d.insert(8,88)
d.print_db()
print(d.length())
d.print_reverse_db()
d.insert(10,2)"""
print(d.delete(2))
d.print_db()
