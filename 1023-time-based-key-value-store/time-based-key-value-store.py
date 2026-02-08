# hashmap, key (string) -> value (hashmap, key (timestamp int -> value (string))) HASHMAP HASHMAP SOLUTION
    # will timeout

# hashmap, key (string) -> value (ll in descending time,tuple of (timestamp, value)) HASHMAP LL SOLUTION

# if no val at req time, return FIRST AVAILABLE previous timestamp value

# set returns none
# if required timestamp:
    # get returns val
# elif prev timestamp exists:
    # get returns prev timestamp val
# else
    # return none


# set
    # create node
    # if key exists
        # add node to the top and make it new head
    # else
        # create keu

class Node:
    def __init__(self, val=(0, 0), next_add=None):
        self.val = val
        self.next = next_add

class TimeMap:
    def __init__(self):
        self.store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        node = Node(val=(timestamp, value))
        if key not in self.store:
            self.store[key] = node
        else:
            temp = self.store[key]
            self.store[key] = node
            node.next = temp
        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        ll = self.store[key]
        i = timestamp
        while ll and ll.val[0] > timestamp:
            ll = ll.next
        else:
            if ll:
                return ll.val[1]
            else:
                return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)