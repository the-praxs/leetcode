class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()                       # Convert to lowercase
        s = ''.join(filter(str.isalnum, s)) # Remove non-alphanumeric characters
        
        l, r = 0, len(s)-1
        
        while l<r:
            if s[l] != s[r]:                # If the characters don't match, return False
                return False
            l+=1
            r-=1
        
        return True