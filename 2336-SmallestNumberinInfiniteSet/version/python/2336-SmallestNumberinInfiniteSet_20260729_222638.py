# Last updated: 7/29/2026, 10:26:38 PM
1import heapq
2class SmallestInfiniteSet:
3
4    def __init__(self):
5        self.smallest_num = 1
6        self.add_back_heap = []
7        self.add_back_set = set()
8
9    def popSmallest(self) -> int:
10        if self.add_back_heap:
11            val = heapq.heappop(self.add_back_heap)
12            self.add_back_set.remove(val)
13            return val
14        
15        val = self.smallest_num
16        self.smallest_num += 1
17        return val
18
19    def addBack(self, num: int) -> None:
20        if num < self.smallest_num and num not in self.add_back_set:
21            heapq.heappush(self.add_back_heap, num)
22            self.add_back_set.add(num)
23        
24
25# Your SmallestInfiniteSet object will be instantiated and called as such:
26# obj = SmallestInfiniteSet()
27# param_1 = obj.popSmallest()
28# obj.addBack(num)