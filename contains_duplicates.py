from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        finder_dict = {}
        for x in nums:
            if finder_dict.get(x,0) == 1:
                return True
            finder_dict[x] = 1
        
        return False