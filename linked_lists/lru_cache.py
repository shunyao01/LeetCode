class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    Create a LRUCache which get and put in O(1) and ditch the least recently used 

    Args:
        capacity: integer > 1, max number of key value pairs LRUCache can hold
        key: integer value >= 0
        value: integer value >= 0

    Time Complexity: 
        O(1)

    Trick:
        Doubly linked list
        Used for O(1) insertion and deletion at both ends or in the middle with a reference
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # store key(key) value(referecne to node) pair
        self.head = Node(0, 0) # dummy mru
        self.tail = Node(0, 0) # dummy lru
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node: Node) -> None:
        """Add node to the front of double linked list"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def remove(self, node: Node) -> None:
        """Remove node from the doubly linked list"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        """Return the value of the key and update to MRU"""
        if key in self.cache:
            node = self.cache[key]

            # remove node and add node to update MRU
            self.remove(node)
            self.add(node)
            return node.value

        return -1 # not found

    def put(self, key: int, value: int) -> None:
        """Add node to list head or Update node to head"""

        # found key, update
        if key in self.cache: # or len(self.cache) < self.capacity: 
            old_node = self.cache[key]
            self.remove(old_node) # remove old node
        else: # key not found, add, check length & remove
            if len(self.cache) >= self.capacity:
                lru = self.tail.prev # remove from cache
                self.remove(lru) # remove from list
                del self.cache[lru.key]

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add(new_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)