class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        nums.sort()
        
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:                  # Skip duplicates
                continue
                
            l, r = i+1, len(nums)-1
            
            while l<r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:                            # If the sum is greater than 0, decrement r
                    r -= 1
                elif threeSum < 0:                          # If the sum is less than 0, increment l
                    l += 1
                else:
                    sums.append([val, nums[l], nums[r]])    # If the sum is 0, add the triplet to the list
                    l += 1
                    while nums[l] == nums[l-1] and l < r:   # Skip duplicates
                        l += 1
                        
        return sums