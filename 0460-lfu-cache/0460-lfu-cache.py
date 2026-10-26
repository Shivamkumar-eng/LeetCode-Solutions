class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # Dummy head and tail nodes to easily append/remove elements
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    def append(self, node: Node) -> None:
        # Inserts a node right after the dummy head (Most Recently Used in this frequency group)
        first_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first_node
        first_node.prev = node
        self._size += 1

    def remove(self, node: Node) -> None:
        # Detaches an existing node from the list
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self._size -= 1

    def pop_tail(self) -> Node:
        # Removes the Least Recently Used node right before the dummy tail
        if self._size == 0:
            return None
        lru_node = self.tail.prev
        self.remove(lru_node)
        return lru_node

    def __len__(self) -> int:
        return self._size

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}        # maps key -> Node
        self.freq_map = {}     # maps frequency -> DoublyLinkedList
        self.min_freq = 0      # tracks global minimum frequency for eviction

    def _update_frequency(self, node: Node) -> None:
        """Helper to increment a node's frequency and move it to the correct list."""
        old_freq = node.freq
        new_freq = old_freq + 1
        node.freq = new_freq
        
        # 1. Remove node from the current frequency list
        self.freq_map[old_freq].remove(node)
        
        # If the minimum frequency list becomes empty, increment the global min_freq
        if old_freq == self.min_freq and len(self.freq_map[old_freq]) == 0:
            self.min_freq += 1
            
        # 2. Add node to the new frequency list
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DoublyLinkedList()
        self.freq_map[new_freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
            
        node = self.cache[key]
        self._update_frequency(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
            
        if key in self.cache:
            # Key exists: update its value and bump its usage frequency
            node = self.cache[key]
            node.value = value
            self._update_frequency(node)
        else:
            # Key does not exist: handle eviction if cache is full
            if len(self.cache) >= self.capacity:
                # Evict the LRU node from the minimum frequency list
                lru_list = self.freq_map[self.min_freq]
                evicted_node = lru_list.pop_tail()
                if evicted_node:
                    del self.cache[evicted_node.key]
            
            # Insert the new node (starts with a frequency of 1)
            new_node = Node(key, value)
            self.cache[key] = new_node
            
            self.min_freq = 1
            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            self.freq_map[1].append(new_node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
