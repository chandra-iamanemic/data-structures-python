#%%
## Can use list but will have problem with memory allocation complexity as lists are dynamic arrays
content_to_watch = []

content_to_watch.insert(0, "Lincoln Lawyer")
content_to_watch.insert(0, "Kadaisi Vyavasayi")
content_to_watch.insert(0, "Demon Slayer")

content_to_watch

# %%
# FIFO pop unlike stack
content_to_watch.pop()

# %%
from collections import deque

q = deque()

dir(q)

# %%
# append left to form a que
q.appendleft("Lincoln Lawyer")
q.appendleft("Kadaisi Vyavasayi")
q.appendleft("Demon Slayer")

#%%

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
#%%

queue = Queue()

queue.enqueue({"name" : "Lincoln Lawyer",
               "type" : "series"})

queue.enqueue({"name" : "Kadaisi Vyavasayi",
               "type" : "movie"})

queue.enqueue({"name" : "Demon Slayer",
               "type" : "anime"})

queue.buffer

# %%
## after finishing the first content in list we can pop it out FIFO

queue.dequeue()
queue.buffer

# %%
