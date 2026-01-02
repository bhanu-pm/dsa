# Both get and put should run in O(1)
    # So, Hashmap + dll
        # hashmap points to the value in dll
        # dll maintains the order of usage
            # both get and put methods update the order of usage in DLL

# Only gets return the value
    # if item exists, return the 'get' value
    # else, return -1
    # put returns null

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key, last=False)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # Updating a value
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)
            return
            
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=True)
        self.cache[key] = value
        self.cache.move_to_end(key, last=False)
        # print(self.cache)
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)