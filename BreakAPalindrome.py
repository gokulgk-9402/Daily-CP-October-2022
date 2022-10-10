class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)

        if length == 1:
            return ""

        palindrome = list(palindrome)
        for i in range(length):
            if palindrome[i] != 'a':
                if length % 2 and i != length//2:
                    palindrome[i] = 'a'
                    return "".join(palindrome)
                elif length % 2 == 0:
                    palindrome[i] = 'a'
                    return "".join(palindrome)
                    
        palindrome[-1] = 'b'
        return "".join(palindrome)