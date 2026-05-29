# Last updated: 5/29/2026, 4:59:23 PM
1from collections import deque
2
3class RecentCounter:
4
5    def __init__(self):
6        self.queue = deque()
7
8
9    def ping(self, t: int) -> int:
10        self.queue.append(t)
11        while self.queue[0] < t-3000:
12            self.queue.popleft()
13        
14        return len(self.queue)
15
16
17# Your RecentCounter object will be instantiated and called as such:
18# obj = RecentCounter()
19# param_1 = obj.ping(t)