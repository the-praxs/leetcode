class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # HashMap to store array value : corresponding index
        
        for idx, val in enumerate(nums):
            # find difference between target and current value
            num = target - val

            # if difference is in hashmap, return index of difference and current index
            if num in hashmap:
                return [hashmap[num], idx]

            # else, add current value and index to hashmap
            hashmap[val] = idx
            
        return