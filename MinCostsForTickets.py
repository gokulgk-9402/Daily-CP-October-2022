from typing import List
import bisect

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        if len(days) == 1:
            return min(costs)

        mem = {}

        def dfs(index):
            if index in mem:
                return mem[index]
            if index >= len(days):
                mem[index] = 0
                return 0

            cost1 = dfs(index+ 1) + costs[0]
            cost7 = dfs(bisect.bisect(days, days[index]+6)) + costs[1]
            cost30 = dfs(bisect.bisect(days, days[index] + 29)) + costs[2]

            mem[index] = min(cost1, cost7, cost30)
            return mem[index]

        return dfs(0)