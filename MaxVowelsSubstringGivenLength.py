class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        curr = 0
        right = 0
        length = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        while right < k:
            if s[right] in vowels:
                curr += 1
            right += 1

        maximum = curr

        while right < length:
            if s[left] in vowels:
                curr -= 1
            if s[right] in vowels:
                curr += 1
            
            maximum = max(curr, maximum)
            left += 1
            right += 1

        return maximum