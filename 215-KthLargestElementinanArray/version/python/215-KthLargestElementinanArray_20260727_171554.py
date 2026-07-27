# Last updated: 7/27/2026, 5:15:54 PM
1import heapq
2class SmallestInfiniteSet:
3
4    def __init__(self):
5        self.curr_min = 1
6        self.added_back_heap = []
7        self.added_back_set = set()
8
9    def popSmallest(self) -> int:
10        if self.added_back_heap:
11            val =heapq.heappop(self.added_back_heap)
12            self.added_back_set.remove(val)
13            return val
14        
15        val = self.curr_min
16        self.curr_min += 1
17        return val
18
19    def addBack(self, num: int) -> None:
20        if num < self.curr_min and num not in self.added_back_set:
21            heapq.heappush(self.added_back_heap,num)
22            self.added_back_set.add(num)
23
24
25# Your SmallestInfiniteSet object will be instantiated and called as such:
26# obj = SmallestInfiniteSet()
27# param_1 = obj.popSmallest()
28# obj.addBack(num)