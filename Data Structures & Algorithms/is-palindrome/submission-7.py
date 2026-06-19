class Solution:
    def isPalindrome(self, s: str) -> bool:
        paladins = ""
        for i in s:
            if i.isalnum():
                paladins += i.lower()
        return paladins[::-1] == paladins
           


