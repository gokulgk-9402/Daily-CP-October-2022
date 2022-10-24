from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def can_alloc(k):
            w = SortedList(workers[-k:])
            tries = pills
            
            for task in tasks[:k][::-1]:
                ind = w.bisect_left(task)
                if ind < len(w):
                    w.pop(ind)
                elif tries > 0:
                    ind2 = w.bisect_left(task - strength)
                    if ind2 < len(w):
                        w.pop(ind2)
                        tries -= 1
                else:
                    return False
                
            return len(w) == 0

        beg, end = 0, min(len(workers), len(tasks)) + 1

        while beg + 1< end:
            mid = (beg + end) // 2
            if can_alloc(mid):
                beg = mid
            else:
                end = mid
        
        return beg