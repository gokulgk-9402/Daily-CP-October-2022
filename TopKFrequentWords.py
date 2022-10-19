from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ctr = Counter(words)
        ans = []
        curr = 0
        print(ctr.items())
        for p in sorted(ctr.items(), key = lambda x: (-x[1], x[0])):
            # print(p)
            ans.append(p[0])
            curr += 1
            if curr == k:
                break

        return ans