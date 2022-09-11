class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #Time Complexity: O(1)
    #Auxiliary Space: O(1)


    # Function to insert a new node after gievn point

    def insertAfter(self, prev_node, new_data):
        new_node = Node(new_data)
        
        if prev_node == None:
            return

        new_node.next = prev_node.next
        prev_node.next = new_node

        #Time Complexity: O(1)
        #Auxiliary Space: O(1)
        

    # Function to append a new node in the end

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next
        
        last.next = new_node

        #Time complexity: O(N)
        #Auxiliary Space: O(1)


