class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        i = 0

        while num:
            cur = num % 10
            num = num // 10

            if cur < 4:
                if i == 0:
                    ans = "I" * cur + ans
                elif i == 1:
                    ans = "X" * cur + ans
                elif i == 2:
                    ans = "C" * cur + ans
                else:
                    ans = "M" * cur + ans
            elif cur == 4:
                if i == 0:
                    ans = "IV" + ans
                elif i == 1:
                    ans = "XL" + ans
                elif i == 2:
                    ans = "CD" + ans
            elif cur == 5:
                if i == 0:
                    ans = "V" + ans
                elif i == 1:
                    ans = "L" + ans
                elif i == 2:
                    ans = "D" + ans
            elif cur < 9:
                if i == 0:
                    ans = "V" + (cur-5)*"I" + ans
                elif i == 1:
                    ans = "L" + (cur-5)*"X" + ans
                elif i == 2:
                    ans = "D" + (cur-5)*"C" + ans
            elif cur == 9:
                if i == 0:
                    ans = "IX" + ans
                elif i == 1:
                    ans = "XC" + ans
                elif i == 2:
                    ans = "CM" + ans

            i += 1

        return ans

            
                