# input is the same

# get
    # return value or -1
    # +1 frequency
    # put it at the start of the dll of that frequency
    # update min frequency if that freq doesn't exist anymore

# put
    # return null
    # if key exists, update the value
        # +1 frequency
        # put it at the start of the dll of that freq
        # min frequency = 1
    # if key don't exist
        # if less than capacity after putting key
            # same as above
        # else
            # go to min frequency
            # list of keys w same frequency
            # oldest key (right most) is evicted
                # same put process as above

# ds
    # frequency map
        # frequency as key -> orderedDict of keys w that rrequency
    # normal cache
        # key -> [value, frequency]

from collections import OrderedDict
class LFUCache:
    def __init__(self, capacity: int):
        self.current_cap = 0
        self.capacity = capacity
        self.cache_od = dict()
        self.cache_map = dict()
        self.min_f = float('inf')

    def get(self, key: int) -> int:
        if key in self.cache_map:
            current_val, current_freq = self.cache_map[key]
            del self.cache_od[current_freq][key]

            # move the key to new freq & move key to front
            if current_freq+1 not in self.cache_od:
                self.cache_od[current_freq+1] = OrderedDict()
            self.cache_od[current_freq+1][key] = current_val
            self.cache_od[current_freq+1].move_to_end(key, last=False)
            
            # check for and update min freq
            if self.min_f == current_freq:
                if len(self.cache_od[current_freq]) == 0:
                    self.min_f += 1

            self.cache_map[key][1] += 1
            return current_val
        return -1

    def put(self, key: int, value: int) -> None:
        ####################### overwrite case
        if key in self.cache_map:
            current_freq = self.cache_map[key][1]
            self.cache_map[key] = [value, current_freq+1]

            del self.cache_od[current_freq][key]

            # move the key to new freq & move key to front
            if current_freq+1 not in self.cache_od:
                self.cache_od[current_freq+1] = OrderedDict()
            self.cache_od[current_freq+1][key] = value
            self.cache_od[current_freq+1].move_to_end(key, last=False)
            
            # check for and update min freq
            if self.min_f == current_freq:
                if len(self.cache_od[current_freq]) == 0:
                    self.min_f += 1

        ########################## non overwrite case
        else:
            ########### when cache is not full
            if self.current_cap < self.capacity:
                self.cache_map[key] = [value, 1]

                # add key to new freq & move key to front
                if 1 not in self.cache_od:
                    self.cache_od[1] = OrderedDict()
                self.cache_od[1][key] = value
                self.cache_od[1].move_to_end(key, last=False)

                self.min_f = 1
                self.current_cap += 1
            ########### when cache is full
            elif self.current_cap == self.capacity:
                last_key, last_value = self.cache_od[self.min_f].popitem(last=True)
                del self.cache_map[last_key]
                # if len(self.cache_od[self.min_f]) == 0:
                #     del self.cache_od[self.min_f]
                #     self.min_f = min(list(self.cache_od.keys()))

                # insert the new cache val
                self.cache_map[key] = [value, 1]

                # add key to new freq & move key to front
                if 1 not in self.cache_od:
                    self.cache_od[1] = OrderedDict()
                self.cache_od[1][key] = value
                self.cache_od[1].move_to_end(key, last=False)

                self.min_f = 1
        return

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)