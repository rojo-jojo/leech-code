from itertools import accumulate
from operator import mul
from typing import List
class Solution:
    def productExceptSelf(self, nums) -> List[int]:
        res =  [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

if __name__ == '__main__':
    stf = Solution()
    print(stf.productExceptSelf([1,2,3,4,5]))