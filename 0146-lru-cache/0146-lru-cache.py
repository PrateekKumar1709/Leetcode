class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # Initialize cache with capacity
        self.capacity = max(0, capacity)  # Handle negative capacity
        self.cache = {}  # HashMap for O(1) lookup
        
        # Initialize dummy head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node):
        # Remove node from doubly linked list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_node(self, node):
        # Add node right after head (most recently used)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _move_to_front(self, node):
        # Move existing node to front
        self._remove_node(node)
        self._add_node(node)
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move to front as it's most recently used
            self._move_to_front(node)
            return node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            # Add new key
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            
            # Evict least recently used if capacity exceeded
            if len(self.cache) > self.capacity:
                # Remove from both list and cache
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]
