# Last updated: 8/11/2026, 6:41:04 PM
from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque()
        
    def ping(self, t: int) -> int:
        self.q.append(t)
        
        while t - self.q[0] > 3000:
            self.q.popleft()
            
        return len(self.q)
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)