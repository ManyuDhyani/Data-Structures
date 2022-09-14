class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def deleteNodeAtGivenPosition(self, position):

        if self.head is None:
            return

        curr = self.head
        i = 1
        while curr.next and i < position:
            prev = curr
            curr = curr.next
            i+=1

        if position == 1:
            self.head = self.head.next
        else:
            prev.next = curr.next
        
        



