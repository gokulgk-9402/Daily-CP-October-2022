class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        times = []
        length = len(plantTime)

        for i in range(length):
            times.append([plantTime[i], growTime[i]])

        times.sort(key=lambda x: -x[1])

        ans = 0
        time = 0

        for i in range(length):
            time += times[i][0]
            ans = max(ans, time+times[i][1])

        return ans