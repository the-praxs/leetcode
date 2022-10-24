class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0                                 # left pointer
        length = 0
        
        for right in range(len(s)):             
            while s[right] in charSet:           # if char is in set, remove char and move left pointer
                charSet.remove(s[left])          
                left += 1                        
                
            charSet.add(s[right])                # add char to set 
            length = max(length, right-left+1)
            
        return length