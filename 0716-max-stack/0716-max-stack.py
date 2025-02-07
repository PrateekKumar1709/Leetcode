from sortedcontainers import SortedDict
class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MaxStack:
    def __init__(self):
        # Initialize head and tail sentinels
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        # TreeMap to store value to nodes mapping
        self.value_to_nodes = SortedDict()
        
    def push(self, x: int) -> None:
        # Create new node
        node = Node(x)
        # Insert before tail
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        # Add to TreeMap
        if x not in self.value_to_nodes:
            self.value_to_nodes[x] = []
        self.value_to_nodes[x].append(node)
        
    def pop(self) -> int:
        if self.head.next == self.tail:
            return None
        # Get top node
        node = self.tail.prev
        val = node.val
        # Remove from doubly linked list
        self._remove_node(node)
        # Remove from TreeMap
        self.value_to_nodes[val].pop()
        if not self.value_to_nodes[val]:
            del self.value_to_nodes[val]
        return val
    
    def top(self) -> int:
        if self.head.next == self.tail:
            return None
        return self.tail.prev.val
    
    def peekMax(self) -> int:
        if not self.value_to_nodes:
            return None
        return self.value_to_nodes.peekitem(-1)[0]
    
    def popMax(self) -> int:
        if not self.value_to_nodes:
            return None
        # Get max value and its last node
        max_val = self.value_to_nodes.peekitem(-1)[0]
        node = self.value_to_nodes[max_val][-1]
        # Remove node
        self._remove_node(node)
        # Update TreeMap
        self.value_to_nodes[max_val].pop()
        if not self.value_to_nodes[max_val]:
            del self.value_to_nodes[max_val]
        return max_val
    
    def _remove_node(self, node):
        # Helper to remove node from doubly linked list
        node.prev.next = node.next
        node.next.prev = node.prev
