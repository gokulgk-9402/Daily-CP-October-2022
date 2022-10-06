class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:

        ans = []

        while a or b:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                is_a = ans[-1] == 'b'
            else:
                is_a = a>= b

            if is_a:
                a -= 1
                ans.append('a')
            else:
                b-= 1
                ans.append('b')

        return "".join(ans)