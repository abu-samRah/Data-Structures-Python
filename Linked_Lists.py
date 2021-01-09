class Node:
    def __init__(self, data = None, nextNode= None):
        self.data = data
        self.nextNode = nextNode

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        
       outputString = ''
       if self.head is None:
           outputString ="empty linked list"
           
       else:
           iter = self.head
           
           while iter:
               outputString += str(iter.data) + '-->' if iter.nextNode else str(iter.data)
               iter = iter.nextNode
               
       print(outputString)
        
    def get_length(self):
       if self.head is None:
           print("empty linked list")
           return
       
       else:
           iter = self.head
           counter = 0
           while iter:
               counter+=1
               iter = iter.nextNode
           return counter

    def insert_at_begining(self, data):
       node = Node(data,self.head)
       self.head = node

    def insert_at_end(self, data):
        if self.head is None:
           self.head = Node(data,None)
           return
        else:
           iter =self.head
           while iter.nextNode:
             iter = iter.nextNode
             
           node = Node(data)
           iter.nextNode = node
            

    def insert_at(self, index, data):
       if self.head is None:
           self.head = Node(data)
           return
       elif index == 0:
           self.insert_at_begining(data)
       else:
           iter =self.head
           count = 1
           while iter.nextNode and count <= index -1:
             iter = iter.nextNode
             count +=1
           node = Node(data , iter.nextNode)
           iter.nextNode = node

    def remove_at(self, index):
       if self.head is None:
           print("empty linked list")
           return
       elif index == 0:
           self.head = self.head.nextNode
       else:
           iter =self.head
           count = 1
           while iter.nextNode and count <= index -1:
             iter = iter.nextNode
             count +=1
           iter.nextNode = iter.nextNode.nextNode

    def insert_values(self, data_list):
        self.head = None
        for x in data_list:
            self.insert_at_end(x)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(0,"blueberry")
    ll.print()
    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()

    
