#%%
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        



class LinkedList:

    # At the start initialize the head as None
    def __init__(self):
        self.head = None

    # Inserting a new node at the beginning of the linked list
    # We add a new node and take the current head node as its next node
    # We assign the new node as the current head node as its added to beginning
    def insert_at_beginning(self, data):
        # create a new node for new data
        # take current head node and add as the next node
        node = Node(data, self.head)

        #now assign the newly created node as the list's head node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
        
        current_node = self.head
        while True:
            if(current_node.next is None):
                current_node.next = Node(data, None)
                break
            else:
                current_node = current_node.next
            
        
    # function to insert values at the end of existing List
    def insert_values_at_end(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    # function to insert values at the beginning of existing List
    def insert_values_at_beginning(self, data_list):
        for data in data_list:
            self.insert_at_beginning(data)


    # function to clear existing list and insert values
    def insert_values_clear(self, data_list):
        self.head = None
        
        for data in data_list:
            self.insert_at_end(data)


    def remove_at_index(self, index):
        if index<0 or index>= self.get_length():
            raise Exception("invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        current_node = self.head

        while current_node:
            if count == index - 1:
                current_node.next = current_node.next.next
                break
            count += 1
            current_node = current_node.next
    

    def insert_at_index(self, index, data):
        if index<0 or index>= self.get_length():
            raise Exception("invalid index")

        if index == 0:
            self.insert_at_beginning(data)

        if index == self.get_length():
            self.inser_at_end(data)
        
        current_node = self.head
        
        count = 0
        while current_node:
            if count == index - 1:
                temp_next_node = current_node.next
                current_node.next = Node(data, temp_next_node)
                break
            count+=1
            current_node = current_node.next
        

    def get_head(self):
        return self.head.data


    def get_length(self):
        count = 0
        current_node = self.head

        while current_node:
            count += 1
            current_node = current_node.next
        
        return count


    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        current_node = self.head
        linked_list = []
        linked_list_str = ''
        while current_node:
            linked_list.append(current_node.data)
            linked_list_str = linked_list_str + str(current_node.data) + '-->'
            current_node = current_node.next
        print(linked_list)
        print(linked_list_str)





#%%
linked_list = LinkedList()
linked_list.insert_at_beginning(1)
linked_list.insert_at_beginning(2)

linked_list.insert_at_end(3)

# %%
linked_list.print()

# %%
data_list = [4,5,6]

linked_list.insert_values_at_end(data_list)
linked_list.print()

# %%
data_list = [7,8,9]

linked_list.insert_values_at_beginning(data_list)
linked_list.print()

#%%

print("Current Head : ", linked_list.get_head())

linked_list.remove_at_index(3)
linked_list.print()

# %%
linked_list.insert_at_index(3, 2)

linked_list.print()
# %%
