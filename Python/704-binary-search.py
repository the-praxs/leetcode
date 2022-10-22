class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l<=r:
            '''
            Mid point is calculated using the formula:
            mid = left + (right-left)/2
            This means calculate the difference between left and right and divide it by 2,
            then add it to left (remaning distance from left to mid). Hence the mid point 
            is always rounded down. This is done to avoid overflow when left and right 
            are large numbers.
            '''
            mid = l + ((r - l) // 2)
            
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
            
        return -1