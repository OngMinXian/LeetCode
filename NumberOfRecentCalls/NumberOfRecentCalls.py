from collections import deque

class RecentCounter:

    def __init__(self):
        self.recent_calls = deque()

    def ping(self, t: int) -> int:
        self.recent_calls.append(t)
        while self.recent_calls[0] < (t - 3000):
            self.recent_calls.popleft()
        return len(self.recent_calls)

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(1)
param_2 = obj.ping(100)
param_3 = obj.ping(3001)
param_4 = obj.ping(3002)
ans = [param_1, param_2, param_3, param_4]; assert ans == [1, 2, 3, 3]; ans
