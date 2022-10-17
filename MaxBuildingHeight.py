class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n - 1

        restrictions.append([1, 0])
        restrictions.sort(key = lambda x: x[1] + x[0])
        index = 0
        max_height = 0

        while index < len(restrictions):
            pos, h = restrictions[index]
            index += 1
            while index < len(restrictions) and restrictions[index][1] - restrictions[index][0] >= h - pos:
                index += 1

            if index == len(restrictions):
                max_height = max(max_height, h + n - pos)
                break

            next_pos, next_h = restrictions[index]

            max_height = max(max_height, (h + next_h + next_pos - pos) // 2)

        return max_height