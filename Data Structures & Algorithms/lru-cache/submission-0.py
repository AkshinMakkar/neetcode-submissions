class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, new):
        last = self.tail.prev

        last.next = new
        new.prev = last

        new.next = self.tail
        self.tail.prev = new

    def remove(self, node):
        left = node.prev
        right = node.next

        left.next = right
        right.prev = left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        
        node = self.cache[key]
        
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        # condition: if the key exists, then update it 
        if key in self.cache: 
            node = self.cache[key]
            node.value = value

            self.remove(node)
            self.insert(node)
        else:
            new = Node(key, value)
            self.insert(new)

            self.cache[key] = new
        
        # we get lru to because the node right after the head is the least recently used 
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

        
