class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d = date.split('-')

        mem = {
            1 : 0,
            2 : 31,
            3 : 59,
            4: 90,
            5: 120,
            6: 151,
            7: 181,
            8: 212,
            9: 243,
            10: 273,
            11: 304,
            12: 334
        }
        y = int(y)
        m = int(m)
        d = int(d)

        ans = d
        ans += mem[m]

        if y % 100 == 0:
            if y % 400 == 0 and m > 2:
                ans += 1
        else:
            if y % 4 == 0 and m > 2:
                ans += 1

        return ans