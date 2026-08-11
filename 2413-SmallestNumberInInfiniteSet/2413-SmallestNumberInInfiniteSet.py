# Last updated: 8/11/2026, 12:01:37 PM
import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.smallest_num = 1
        self.add_back_heap = []
        self.add_back_set = set()

    def popSmallest(self) -> int:
        if self.add_back_heap:
            val = heapq.heappop(self.add_back_heap)
            self.add_back_set.remove(val)
            return val
        
        val = self.smallest_num
        self.smallest_num += 1
        return val

    def addBack(self, num: int) -> None:
        if num < self.smallest_num and num not in self.add_back_set:
            heapq.heappush(self.add_back_heap, num)
            self.add_back_set.add(num)
        

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)