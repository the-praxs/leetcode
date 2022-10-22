class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)                # Inititalize answer array with 1s
        prefix, postfix = 1, 1
        
        for i in range(len(nums)):              # Calculate prefix product
            answer[i] = prefix                  # Store prefix product in answer array
            prefix*=nums[i]                     # Update prefix product
            
        for i in reversed(range(len(nums))):    # Calculate postfix product
            answer[i]*=postfix                  # Multiply postfix product to answer array
            postfix*=nums[i]                    # Update postfix product
            
        return answer