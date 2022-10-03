from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        stack = [0]

        for num in target:
            maximum = 0
            while stack and stack[-1] >= num:
                maximum = max(maximum, stack.pop() - num)
            ans += maximum
            stack.append(num)
        
        while stack[-1]:
            ans += abs(stack.pop() - stack[-1])

        return ans