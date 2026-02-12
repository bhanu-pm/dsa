# least recently used would be evicted
# we need to maintain an order, most recently used = at left, lru = at right
# cache should stay within given capacity
# get:
    # return key if exist else -1
# put:
    # if key exist:
        # update key
    # else
        # if capacity there;
            # add key
            # stored +=1
        # else
            # evict lru
            # add key
# for O(1) lookups, we need a dict
# and this dict should have an order like doubly linked lists, for ease of access from both ends
# and modifiability


from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stored = 0
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key, last=False)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)
        else:
            if self.stored < self.capacity:
                self.cache[key] = value
                self.cache.move_to_end(key, last=False)
                self.stored += 1
            else:
                self.cache.popitem(last=True)
                self.cache[key] = value
                self.cache.move_to_end(key, last=False)
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)