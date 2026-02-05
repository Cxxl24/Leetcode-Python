from typing import Dict, List

class Solution:
    def twoSum(self, nums : List[int], target : int) -> List[int]:
        hashmap: Dict[int, int] = {}

        for i in range(len(nums)):
            if (target - nums[i]) in hashmap.values():
                return [hashmap[target - nums[i]], i]
            else: 
                hashmap[nums[i]] = i
