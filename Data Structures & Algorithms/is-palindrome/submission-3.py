class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.alphCheck(s[l]):
                l += 1
            while l < r and not self.alphCheck(s[r]):
                r -= 1
            if(s[l].lower() != s[r].lower()):
                return False
            l += 1
            r -= 1
        return True

                    
    
    def alphCheck(self, s):
        return ("a" <= s <= "z" or "A" <= s <= "Z" or "0" <= s <="9")
        