class TimeMap:

    def __init__(self):
        self.hash = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash:
            self.hash[key].append((timestamp, value))
        else:
            self.hash[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hash:
            # Do binary search as timestamp is strictly increasing
            search_lst = self.hash[key]
            low = 0
            high = len(search_lst) - 1
            res = ''
            while low <= high:
                middle = (low + high) // 2
                if search_lst[middle][0] <= timestamp:
                    res = search_lst[middle][1]
                    low = middle + 1
                elif search_lst[middle][0] > timestamp:
                    high = middle - 1
            return res
        else:
            return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)