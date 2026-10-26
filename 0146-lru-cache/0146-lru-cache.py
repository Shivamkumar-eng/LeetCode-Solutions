class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # maps key -> Node
        
        # Initialize dummy head and tail nodes to eliminate edge cases
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper function to remove a node from its current position
    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Helper function to insert a node right after the dummy head (Most Recently Used)
    def _insert_at_head(self, node: Node) -> None:
        first_node = self.head.next
        
        self.head.next = node
        node.prev = self.head
        
        node.next = first_node
        first_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Refresh node's location to the head since it was accessed
            self._remove(node)
            self._insert_at_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the existing node's value and refresh its position to head
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._insert_at_head(node)
        else:
            # Check capacity limits before adding a new pair
            if len(self.cache) >= self.capacity:
                # Evict the Least Recently Used node (right behind the dummy tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            
            # Insert the entirely new key-value pair
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._insert_at_head(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
