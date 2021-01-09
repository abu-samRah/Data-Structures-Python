class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
       if self.data == data:
           return
       
       else:
           if data < self.data:
               if self.left:
                   self.left.add_child(data)
               else:
                    self.left = BinarySearchTreeNode(data)
           else:
                if self.right:
                   self.right.add_child(data)
                else:
                    self.right = BinarySearchTreeNode(data)    
                
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
            
    def in_order_traversal(self):
        res = []
        if self :
           
            if self.left:
              res =  self.left.in_order_traversal() 
            res.append(self.data)
            if self.right:
               res = res + self.right.in_order_traversal()
            
        return res

    def findMin(self):

        if self.left :
            return self.left.findMin()
        else:
            return self.data
        
    def findMax(self):

        if self.right :
            return self.right.findMax()
        else:
            return self.data   
    
    
    def deleteNode(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.deleteNode(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.deleteNode(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.left.findMax()
            self.data = max_val
            self.left = self.left.deleteNode(max_val)

        return self
    
    
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    countries = [17,4,1,20,9,23,18,34,8,4]
    country_tree = build_tree(countries)
    print(country_tree.in_order_traversal())
    country_tree.deleteNode(20)
    print(country_tree.in_order_traversal())
