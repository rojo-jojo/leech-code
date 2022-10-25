# Problem 1 - Two sums

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_a = {}
        for idx, x in enumerate(nums):
            if target - x in dict_a:
                return dict_a[target-x], idx
            dict_a[x] = idx