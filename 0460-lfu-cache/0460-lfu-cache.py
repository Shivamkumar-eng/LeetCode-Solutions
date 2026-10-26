from collections import defaultdict, OrderedDict
class LFUCache:
    def __init__(self, capacity: int):
        self.key_to_freq = {}
        self.freq_to_key = defaultdict(OrderedDict)
        self.key_to_val = {}
        self.min_freq = 0
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key in self.key_to_val:

            #updating frequency
            freq = self.key_to_freq[key]
            del self.freq_to_key[freq][key]


            if len(self.freq_to_key[freq]) == 0 and self.min_freq == freq:
                self.min_freq += 1
            self.key_to_freq[key] += 1
            
            self.freq_to_key[freq + 1][key] = True #this is how you append in an ordered dictionary

            return self.key_to_val[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_val:
            self.key_to_val[key] = value

            freq = self.key_to_freq[key]
            del self.freq_to_key[freq][key]
            if len(self.freq_to_key[freq]) == 0 and self.min_freq == freq:
                self.min_freq += 1
            self.key_to_freq[key] += 1
            self.freq_to_key[freq + 1][key] = True 
        else:
            if len(self.key_to_val) >= self.capacity:
                # deletion of the corresponding key from key_to_freq and all the three tbh just take the min_freq and 
                rem, _ = self.freq_to_key[self.min_freq].popitem(last=False)
                del self.key_to_freq[rem] # it should remove the same key
                del self.key_to_val[rem]
            # bro literally add the new value 
            self.key_to_val[key] = value
            self.key_to_freq[key] = 1
            self.min_freq = 1
            self.freq_to_key[1][key] = True


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
