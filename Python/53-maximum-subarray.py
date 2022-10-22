class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]                        # maxSum is the maximum sum of subarray
        currentSum = 0                          # currentSum is the sum of subarray

        for num in nums:
            currentSum = max(currentSum, 0)     # if currentSum is negative, set it to 0
            currentSum += num                   
            maxSum = max(maxSum, currentSum)        

        return maxSum