class Node():
    def __init__(self, value):
        self.val = value
        self.nxt = None
        self.prv = None
        
class LRU_Cache():

    def __init__(self, capacity):
        self.cap = capacity
        self.curr_size = 0
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.set_head(node)
            return node.val
        else:
            return -1

    def set(self, key, value):
        if self.curr_size == self.cap:
            self.removeLRU()
        new_node = Node(value)
        self.cache[key] = new_node
        self.set_head(new_node)
        self.curr_size += 1
    
    def set_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.nxt = node
            node.prv = self.head
            if self.head.prv == None:
                self.tail = self.head
            self.head = node
        
    def remove_node(self, node):
        if self.curr_size == 1:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.prv
            self.head.nxt = None
        elif node == self.tail:
            self.tail.nxt.prv = None
            self.tail = self.tail.nxt
        else:
            node.prv.nxt = node.nxt
            node.nxt.prv = node.prv
        
    def removeLRU(self):
        node = self.tail
        del self.cache[node.val]
        self.remove_node(node)
        self.curr_size -= 1
       
# Test Cases

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9)) # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
