import bisect
from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.mem = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mem[key + "_value"].append(value)
        self.mem[key + "_ts"].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if self.mem[key + "_ts"] == []:
            return ""
        if self.mem[key + "_ts"][0] > timestamp:
            return ""
        ind = bisect.bisect_right(self.mem[key+"_ts"], timestamp)
        return self.mem[key + "_value"][ind-1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)