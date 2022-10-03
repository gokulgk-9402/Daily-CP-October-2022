class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        
        i = 0

        length = len(colors)

        while i < length:
            j = i
            while j < length - 1 and colors[j] == colors[j + 1]:
                j += 1
            if i != j:
                ans += sum(neededTime[i:j+1]) - max(neededTime[i:j+1])
                i = j
            else:
                i += 1
        return ans