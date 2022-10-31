from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = 1
        cur_max = 1
        res = max(nums)
        for x in nums:
            if x == 0:
                cur_max, cur_min = 1,1
            tmp_cur_max = x*cur_max
            cur_max = max(x*cur_max, x*cur_min, x)
            cur_min = min(tmp_cur_max, x*cur_min, x)
            res = max(res, cur_max, cur_min)
        return res