class Solution:
    def maxValue(self, n: str, x: int) -> str:
        lst = list(n)
        length = len(lst)
        
        neg = n[0] == '-'
        x = str(x)

        for i in range(length):
            if (lst[i] < x and not neg) or (lst[i] > x and neg):
                lst[i] = x + lst[i]
                return ''.join(lst)

        return ''.join(lst) + x

