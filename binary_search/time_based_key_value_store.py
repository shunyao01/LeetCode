class TimeMap:
    """
    Time-based key-value data structure that stores multiple values for the same key at different time stamps and retrieve at certain time stamp

    Time Complexity: O(log n)
    Space Complexity: O(n)
    """

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Add key value timestamp pair"""
        if key not in self.map: 
            self.map[key] = [(value, timestamp)]
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        """Retrieve key value pair with time <= timestamp"""
        # Key not found
        if key not in self.map: 
            return ""
        
        arr = self.map[key]
        i = self.bissect_right(arr, timestamp) # find the first element thats > timestamp

        if i == 0:
            return ""

        return arr[i-1][0]

    def bissect_right(self, blist, target) -> int:
        """Bisect right: return the index of first element bigger than target"""
        low, high = 0, len(blist) - 1

        while low <= high:
            mid = (low + high) // 2
            if blist[mid][1] <= target: 
                low = mid + 1
            else:
                high = mid - 1

        return low  # index of first element with timestamp > target

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# find 6, return 3
# find 3, return 2
# find 2, return 1 
# hm[key] = [1,2,4,5]