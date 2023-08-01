#%%
## Binary Search Tree is a node-based binary tree data structure that has the following properties: 

  

# The left subtree of a node contains only nodes with keys lesser than the node’s key. 

# The right subtree of a node contains only nodes with keys greater than the node’s key. 

# The left and right subtree each must also be a binary search tree. 


class BinarySearchTreeNode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        # add to left sub tree   
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
            
    
    def in_order_traversal(self):
        elements = []

        # traverse left tree recursively
        if self.left:
            elements += self.left.in_order_traversal()
        
        # get the data in current node or base node
        elements.append(self.data)

        # traverse the right tree recursively
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def search(self, val):
        if self.data == val:
            return True
                
        if val<self.data:
            if self.left: 
                return self.left.search(val)
            else:
                return False
            
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    # recursively go right and the last right leaf will be the max in binary search tree
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # recursively go left and the last left leaf will be the min in binary search tree
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val<self.data:
            if self.left:
                self.left = self.left.delete(val)
            
        elif val>self.data:
            if self.right:
                self.right = self.right.delete(val)
                
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            # Find the min val from right sub tree and replace current val
            # we could also find max from left sub tree alternatively
            min_val = self.right.find_min()
            self.data = min_val
            print(min_val)
            self.right = self.right.delete(min_val)

        return self
    
#%%

num_list = [19,4,1,22,9,26,18,34,88,102,109]

root = BinarySearchTreeNode(num_list[0])

for i in range(1, len(num_list)):
    root.add_child(num_list[i])

# %%
print(root.in_order_traversal())

# %%
print(root.search(20))

# %%
root.delete(22)
root.in_order_traversal()

# %%
