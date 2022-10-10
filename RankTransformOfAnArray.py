class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        temp = sorted(arr)
        mem = {temp[0]: 1}

        length = len(temp)
        rank = 1
        for i in range(1, length):
            if temp[i] == temp[i-1]:
                continue
            
            rank += 1
            mem[temp[i]] = rank

        ans = []
        for ele in arr:
            ans.append(mem[ele])

        return ans
