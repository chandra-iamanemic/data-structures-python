#%%
from collections import deque

s = deque()


# %%
dir(s)

# %%
s.append("1.com")
s.append("2.com")
s.append("3.com")

# %%

class Stack:

    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        self.container.pop()

    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
# %%

stack = Stack()

stack.push("luffy")
stack.push("naruto")
stack.push("tanjiro")

# %%
stack.peek()

# %%
stack.pop()

# %%
stack.peek()

#%%