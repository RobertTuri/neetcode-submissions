class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [c.lower() for c in s if c.isalnum()]  
        n = len(clean)
        for i in range(n // 2):                         
            if clean[i] != clean[n - 1 - i]:            
                return False
        return True                                    