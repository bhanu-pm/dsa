# array of coordinates given
# calculate distances of each point from the origin
# map distances to respective index of coordinates, dict
# return all the k smallest distances' coordinates


import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distances
        distances = []
        mapping = dict()
        for idx, num in enumerate(points):
            x, y = num
            dist = math.sqrt((x**2)+(y**2))
            distances.append(dist)
            if dist not in mapping:
                mapping[dist] = []
            mapping[dist].append(idx)
        # heapify distances
        heapq.heapify(distances)
        final = []
        for i in range(k):
            dist = heapq.heappop(distances)
            if len(mapping[dist]) > 1:
                idx = mapping[dist].pop()
                final.append(points[idx])
            else:
                final.append(points[mapping[dist][0]])
        return final
