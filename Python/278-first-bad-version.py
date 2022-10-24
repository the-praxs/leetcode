# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                right = mid                     # Search left half to find the first bad version
            else:
                left = mid + 1                  # Search right half to find the first bad version
                
        return left                             # Return the first bad version