from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            require = target - nums[i]
            if require in seen:
                return [seen[require],i]
        
            seen[nums[i]] = i

        return []
    