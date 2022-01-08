class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        print(self.head.data)
        self.head=self.head.next


    def print_ll(self):
        cur=self.head
        while cur:
            print(cur.data,end="->")
            cur=cur.next

l=Linked_List()
l.push(40)
l.push(70)
l.push(89)
l.pop()
l.print_ll()
